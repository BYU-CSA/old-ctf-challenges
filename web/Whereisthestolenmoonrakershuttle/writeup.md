# Where is the Stolen Moonraker Shuttle? 

## Description
The Moonraker shuttle has disappeared, it is suspected that Hugo Drax stole it back after he gifted it to the British Government. Agent 007 is currently investigating, and has discovered access to the Drax Industries mainframe, but is lacking in his computer skills. Can you help 007 locate the stolen shuttle's location? 

## Solution
1. **Step 1**: Open the website in a web browser and explore
2. **Step 2**: you will notice at the top the the endpoint is `portal.php?filename=home.php`. you can insert a filename here to get it to open... hopefully. The PHP back-end for this is vulnrable to directory traversal. 
3. **Step 3**: there is a button at the bottom of the page. if you click on it you will notice that it tries to bring you to `shuttleLocation.php` It must have been moved. 
4. **Step 4**: go back to the homepage, and make a directory traversal payload in the URL bar to traverse to the flag. ``portal.php?filename=../../../shuttlelocation.php`` This will display the flag.  

The flag for this challenge is `byuctf{p4th-tr4v3rs4l_t0_f1nd_m0onr4k3r}`

## Lessons Learned
It is anticipated that the competitor will learn about how to find and modify a cookie for client side authentication. 

## Notes
the following is the code for the flag page in the event that the docker container needs to be reloaded. If it needs to be reloaded, in the new007 directory, create a file named `shuttlelocation.php`. uncomment the line in the `docker-compose.yml` file that says `command: sh -c "mv /var/www/html/shuttlelocation.php /var/shuttlelocation.php"` run the container using `docker-compose up -d`. Sometimes it fails to load the webpage. If it does, comment the line back out and run `docker-compose up -d` again and it should serve the webpage. 
```<!DOCTYPE html>
<html>
<head>
	<title>Drax Industries Mainframe</title>
	<style>
      body {
        background-color: black;
        color: white;
        font-family: 'Courier New', Courier, monospace;
      }
		h1, h2 {
			text-align: center;
			margin: 20px;
			font-weight: bold;
		}
		p {
			margin: 20px;
		}
		table {
			margin: 20px auto;
			border-collapse: collapse;
			border: 1px solid white;
		}
		th, td {
			padding: 10px;
			border: 1px solid white;
		}
		th {
			background-color: #d62d20;
		}
		tr:nth-child(odd) {
			background-color: #444444;
		}
		tr:nth-child(even) {
			background-color: #333333;
		}
	</style>
</head>
<body>
	<h1>Drax Industries Mainframe</h1>
	<h2>Stolen Moonraker Shuttle Location</h2>
	<p>Our surveillance team has identified the location of the stolen Moonraker shuttle. It is currently being stored in a secure hangar at the following coordinates:</p>
	<table>
		<tr>
			<th>Latitude</th>
			<th>Longitude</th>
			<th>Description</th>
		</tr>
		<tr>
			<td>3.4653° S</td>
			<td>62.2159° W</td>
			<td>Drax Industries Covert Launch Site - The Amazon</td>
		</tr>

	</table>
	<p>Drax Industries is determined to launch the shuttle into space and eliminate all human life on Earth. Our team of experts is working around the clock to complete the necessary modifications to the shuttle and ensure its successful launch. With your continued support, we will achieve our goal and create a new, superior people in space.</p>
    <p>byuctf{p4th-tr4v3rs4l_t0_f1nd_m0onr4k3r}</p>
</body>
</html>
```