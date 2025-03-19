<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Factorial Calculator</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background-color: #f5f5f5;
      text-align: center;
      padding: 20px;
    }
    h1 {
      color: #333;
    }
    form {
      background-color: #fff;
      padding: 20px;
      margin: 20px auto;
      width: 60%;
      max-width: 400px;
      border-radius: 10px;
      box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    }
    input[type="number"] {
      width: 80%;
      padding: 8px;
      margin: 10px 0;
      border: 1px solid #ccc;
      border-radius: 5px;
    }
    button {
      background-color: #007bff;
      color: white;
      border: none;
      padding: 10px 15px;
      cursor: pointer;
      border-radius: 5px;
    }
    button:hover {
      background-color: #0056b3;
    }
    h2 {
      color: #333;
    }
    .result {
      background-color: #e9ecef;
      margin: 10px auto;
      width: 50%;
      padding: 10px;
      border-radius: 5px;
      font-weight: bold;
    }
  </style>
</head>
<body>
  <h1>Factorial Calculator</h1>

  <form method="POST">
    <label for="num">Enter a number:</label>
    <input type="number" name="num" min="0" required>
    <button type="submit" name="calculate">Calculate</button>
  </form>

  <?php
  function factorial($n) {
      if ($n == 0 || $n == 1) return 1;
      return $n * factorial($n - 1);
  }

  if (isset($_POST['calculate'])) {
      $num = intval($_POST['num']);
      $fact = factorial($num);

      // Generating factorial sequence (e.g., 5*4*3*2*1)
      $sequence = implode('*', range($num, 1));

      echo "<h2>Result:</h2>";
      echo "<div class='result'>Factorial of $num is $fact</div>";
      echo "<div class='result'>$sequence = $fact</div>";
  }
  ?>
</body>
</html>
