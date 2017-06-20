# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 22:34:38 2017

@author: onomatopeia
"""

import lorem
import random 
import os
import datetime
import configparser
import mysql.connector


def get_config():
    base_dir = os.path.dirname(os.path.dirname(__file__))
    config = configparser.ConfigParser()
    config.read(os.path.join(base_dir, 'db', 'settings.ini'))
    return config

def get_database_connection():
    config = get_config()
    database = config.get('mysql','database')
    user = config.get('mysql','user')
    password = config.get('mysql','password')
    host = config.get('mysql','host')
    charset = config.get('mysql','charset')
    buffered = config.get('mysql','buffered')
    return mysql.connector.connect(user=user, password=password, host=host, database=database,
                                   charset=charset, buffered=buffered)

class DataAccessObject(object):

    def __init__(self):
        self.connection = None
        self.cursor = None

    def __enter__(self):
        print('entering dao')
        self.connection = get_database_connection()
        self.cursor = self.connection.cursor()
        return self

    def close(self):
        try:
            self.cursor.close()
        except ReferenceError:
            pass

        self.connection.close()

    def __exit__(self, *err):
        print('exiting dao')
        self.close()

    def commit(self):
        self.connection.commit()

    def rollback(self):
        self.connection.rollback()

    def execute(self, query, data):
        self.cursor.execute(query, data)
        if self.cursor.with_rows:
            rows = self.cursor.fetchall()
            return rows
        return self.cursor.lastrowid
        
        
    def select(self):
        return self.execute('SELECT title, content, author, post_date FROM posts')
        
    


def create_test_data(num=10, author = 'Jenny'):
    
    top = "INSERT INTO POSTS(TITLE,AUTHOR,POST_DATE,CONTENT) VALUES\n"  
    lines = []
    csv_lines = []

    today = datetime.datetime.now()
    for i in range(num):
        paragraph = lorem.text()
        paragraph = "<br />".join(paragraph.split("\n"))
        post_date = today - datetime.timedelta(days=random.randint(1, 365))
        title = lorem.sentence()
        lines.append('("{}","{}","{}","{}")'.format(title, author, post_date.strftime("%Y-%m-%d %H:%M:%S"), paragraph))
        csv_lines.append('{},{},{},{}\n'.format(title, author, post_date.strftime("%Y-%m-%d %H:%M:%S"), paragraph))
        
    with open(os.path.join('db','test_data.sql'), 'w', newline='') as outfile:
        outfile.writelines([top, ',\n'.join(lines)])
    with open(os.path.join('db','test_data.csv'),'w') as outfile:
        outfile.writelines(csv_lines)
        
        
if __name__ == '__main__':
    create_test_data()