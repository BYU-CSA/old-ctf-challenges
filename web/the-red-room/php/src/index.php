<!DOCTYPE html>
<html>
<head>
	<title>Red Room Login</title>
	<style>
		body {
			background-color: #d83434;
			color: white;
			font-family: Arial, sans-serif;
			font-size: 18px;
			line-height: 1.5;
			padding: 50px;
			text-align: center;
		}

		h2 {
			margin-bottom: 30px;
		}

		form {
			display: inline-block;
			margin: 0 auto;
			text-align: left;
			background-color: #000000;
			padding: 20px;
			border-radius: 10px;
			box-shadow: 0px 0px 10px 5px rgba(0, 0, 0, 0.4);
		}

		label {
			display: block;
			margin-bottom: 10px;
		}

		input[type="text"], input[type="password"] {
			display: block;
			margin-bottom: 20px;
			padding: 10px;
			width: 100%;
			border-radius: 5px;
			border: none;
			font-size: 18px;
			color: #000000;
		}

		input[type="submit"] {
			background-color: #d83434;
			color: white;
			font-size: 18px;
			padding: 10px 20px;
			border: none;
			border-radius: 5px;
			cursor: pointer;
			transition: background-color 0.3s ease;
		}

		input[type="submit"]:hover {
			background-color: #e44f4f;
		}

	</style>
</head>
<body>
	<h2>Red Room Login</h2>
	<form method="post">
		<label for="username">Username:</label>
		<input type="text" name="username" id="username" required>
		<label for="password">Password:</label>
		<input type="password" name="password" id="password" required>
		<input type="submit" value="Submit">
	</form>

	<?php
		// Check if username and password are submitted
		if (isset($_POST['username']) && isset($_POST['password'])) {
			$username = $_POST['username'];
			$password = $_POST['password'];

			// Hard-coded credentials for the login
			$valid_username = "admin";
			$valid_password = "salvatrucha";

			// Check if the username and password are valid
			if ($username == $valid_username && $password == $valid_password) {
				echo "byuctf{did_black_widow_just_bow_to_hydra?}";
			} else {
				echo "Invalid username or password. Please try again";
			}
		}
	?>
</body>
</html>
