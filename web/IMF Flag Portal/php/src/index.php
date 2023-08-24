<!DOCTYPE html>
<html>
  <head>
    <title>**CLASSIFIED**</title>
    <style>
      body {
        background-color: black;
        color: white;
        font-family: Arial, sans-serif;
        padding: 20px;
      }

      h1 {
        font-size: 36px;
        text-align: center;
        margin-top: 0;
        margin-bottom: 30px;
      }

      p {
        font-size: 18px;
        line-height: 1.5;
        margin-bottom: 20px;
      }

      .code {
        font-family: monospace;
        font-size: 24px;
        background-color: #333;
        padding: 10px;
        border-radius: 5px;
        margin-bottom: 30px;
        width: 95%
      }

      .button {
        display: inline-block;
        background-color: #007bff;
        color: white;
        font-size: 18px;
        padding: 10px 20px;
        border-radius: 5px;
        text-decoration: none;
        margin-right: 10px;
      }

      .button:hover {
        background-color: #0056b3;
      }
    </style>
  </head>
  <body>
    <h1>IMF Flag Portal</h1>
    <p>Welcome to the IMF flag portal. Your mission, should you choose to accept it, is to use the correct request to put the unencrypted message below:</p>
    <div class="code">
    <?php 
        if ($_SERVER['REQUEST_METHOD'] == 'PUT') {
            echo "byuctf{spo0o0o0o0o0o0o0o0o0o0o0o0o0o0o0f3d-w3b-r3qu3st}";
        }
        elseif ($_SERVER['REQUEST_METHOD'] == 'SPOUTINGWHALE') {
            echo "The Spoutingwhale was here";
        }
        elseif ($_SERVER['REQUEST_METHOD'] == 'spoutingwhale') {
            echo "The Spoutingwhale was here";
        }
        else echo "******************************************************";
    ?>    

      
    </div>
    <p>Good luck, agent. You'll need it.</p>
    <p>Remember, in the world of espionage, nothing is what it seems. Trust no one, and always keep your wits about you.</p>

  </body>
</html>
