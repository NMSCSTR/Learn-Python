<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Odd or Even Checker</title>
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
    ul {
      list-style-type: none;
      padding: 0;
    }
    li {
      background-color: #e9ecef;
      margin: 5px auto;
      width: 50%;
      padding: 10px;
      border-radius: 5px;
    }
  </style>
</head>
<body>
  <h1>Odd or Even Checker</h1>

  <form method="POST">
    <label for="nValue">Enter N:</label>
    <input type="number" name="nValue" min="1" required>
    <button type="submit" name="submitN">Submit</button>
  </form>

  <?php
      if (isset($_POST['submitN'])) {
          $n = intval($_POST['nValue']);
          echo "<form method='POST'>";
          echo "<input type='hidden' name='nValue' value='$n'>";

          for ($i = 1; $i <= $n; $i++) {
              echo "<label>Enter number $i:</label>";
              echo "<input type='number' name='numbers[]' required><br><br>";
          }

          echo "<button type='submit' name='check'>Check Numbers</button>";
          echo "</form>";
      }

      if (isset($_POST['check'])) {
          $numbers = $_POST['numbers'];

          echo "<h2>Results:</h2>";
          echo "<ul>";
          foreach ($numbers as $num) {
              $result = ($num % 2 === 0) ? 'EVEN' : 'ODD';
              echo "<li>$num = $result</li>";
          }
          echo "</ul>";
      }
  ?>
</body>
</html>
