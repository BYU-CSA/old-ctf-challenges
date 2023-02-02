from flask import Flask, request
from urllib.parse import urlparse

FLAG = "byuctf{D3F4U1T_6R3D3NT1AL5_4_IOT}"
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    page = """
<html>
<head>
    <title>IOT</title>
</head>
<body style="text-align:center;">
    <br><br>
    <h1>INTERNET OF THINGS</h1>
    <p>This homeowner has decided to hide their special flag inside of their..... Samsung smart refrigerator? Strange. See if you can connect to their device over wifi and access the flag. 
    <br><br><br>
    <h2>Login</h2>
    <form action="/adminflag" method="POST">
        <input type="password" name="password" placeholder="Password">
        <input type="submit" value="Submit">
    </form>
    <img src="https://cf-images.us-east-1.prod.boltdns.net/v1/static/66036796001/ec4f1b93-891c-462b-aabd-85bf4d2fdf42/aadd285e-ff2d-4ed4-b02f-85749d889539/1280x720/match/image.jpg">
</body>
</html>
    """
    return page


@app.route('/adminflag',methods = ['POST'])
def link():
    # get user input
    try:
        password = request.form['password']
    except:
        return "No Form Submitted"

    if password == "1111122222":
        page = f"""
<html>
<head>
    <title>IOT</title>
</head>
<body style="text-align:center;">
    <br><br>
    <h1>INTERNET OF THINGS</h1>
    <p> This is what happens if you don't change the default credentials for your smart devices! </p>
    <p>This is the flag for this house: {FLAG} </p>

</body>
</html>
        """
        return page
    else:
        return "Invalid Credentials"



    # if all checks are passed, then 'urmom' is in the fragment!
    return FLAG


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=40006)