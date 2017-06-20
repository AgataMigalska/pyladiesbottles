<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="">
    <!--<link rel="icon" href="favicon.ico">-->

    <title>Blog</title>

    <!-- Bootstrap core CSS -->
    <link href="/static/css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="/static/css/style.css" rel="stylesheet">
  </head>

  <body>

    <div class="blog-masthead">
      <div class="container">
        <nav class="nav blog-nav">
          <a class="nav-link" href="/">Home</a>
          <a class="nav-link active" href="/blog">Blog</a>
          <a class="nav-link" href="/about">About</a>
        </nav>
      </div>
    </div>

    <div class="blog-header">
      <div class="container">
        <h1 class="blog-title">Messages in the Bottle</h1>
        <p class="lead blog-description">Mostly inspirational stuff</p>
      </div>
    </div>

    <div class="container">

      <div class="row">

        <div class="col-sm-8 blog-main">
          %for idx, post in enumerate(posts):
          <div class="blog-post">
            <h2 class="blog-post-title">{{post['title']}}</h2>
            <p class="blog-post-meta">{{post['date']}} by <a href="#">{{post['author']}}</a></p>

            <p>{{post['post']}}</p>
          </div><!-- /.blog-post -->
          %end

          <nav class="blog-pagination">
            <a class="btn btn-primary" href="#">Older</a>
            <a class="btn btn-secondary disabled" href="#">Newer</a>
          </nav>
    
          <div class="blog-newentry">
              <a class="btn btn-primary" href="/post">Add new entry</a>
          </div>
          
        </div><!-- /.blog-main -->

      </div><!-- /.row -->

    </div><!-- /.container -->

    <footer class="blog-footer">
      <p>Blog template built for <a href="https://getbootstrap.com">Bootstrap</a> by <a href="https://twitter.com/mdo">@mdo</a>.</p>
      <p>
        <a href="#">Back to top</a>
      </p>
    </footer>


    <!-- Bootstrap core JavaScript
    ================================================== -->
    <script src="/static/js/bootstrap.min.js"></script>
  </body>
</html>