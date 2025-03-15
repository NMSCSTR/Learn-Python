<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Login Form</title>
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap" rel="stylesheet">
  <style>
    body { font-family: 'Poppins', sans-serif; }
  </style>
</head>
<body>
  <div class="container col-sm-5 mt-5">
    <h2 class="text-center"><strong>Login Form</strong></h2>
    <form onsubmit="return handleLogin(event)">
      <div class="form-group">
        <label for="username">Username</label>
        <input type="text" class="form-control" id="username" required>
      </div>
      <div class="form-group">
        <label for="password">Password</label>
        <input type="password" class="form-control" id="password" required>
      </div>
      <button type="submit" class="btn btn-primary btn-block">Login</button>
    </form>
  </div>

  <script>
    function handleLogin(event) {
      event.preventDefault();
      window.location.href = 'welcome.html';
    }
  </script>
</body>
</html>
