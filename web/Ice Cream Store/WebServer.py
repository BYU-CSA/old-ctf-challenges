from flask import Flask, request, make_response
from urllib.parse import urlparse

FLAG = "byuctf{dirb_is_the_loml}"
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    page = """
<html>
<head>
    <title>Jurassic Ice Cream Shop!</title>
</head>
<body style="text-align:center;">
    <br><br>
    <h1 style="font-weight: bold">Welcome to the Jurassic Park ice cream shop! We have lots of flavors, so feel free to look around! </h1>
    <p> We have... <p>
    <ul>
    <li> /chocolate </li>
    <li> /vanilla </li>
    <li> /strawberry </li>
    <li> and more! </li>
    </ul>
    <br><br><br>
<img src="https://garden.spoonflower.com/c/7838834/p/f/m/tHy8SeUoitZt0Aci-93aLSAdUQhp7ClN7KYJgS2Ea1qyi5dwH61_Ig/(small%20scale)%20trex%20icecream%20cones%20-%20dinosaur%20icecream%20-%20black%20stripes%20C18BS.jpg">    


    <h2 style="font-weight: bold"> THIS MONTH'S FEATURED FLAVOR: Dinosaur Egg! </h2>
    <img  width="600" height="400" src="https://www.udfinc.com/wp-content/uploads/2020/06/UDF_DinosaurEgg_Scoop_Pint.png">
    <p style="color: green"> "Our delicious Vanilla ice cream goes green to create this prehistoric treat. Grab a spoon and dig in—the egg-shaped candy-coated cake pieces are as fun to find as they are to eat."</p>
<!-- https://www.udfinc.com/ice-cream/dinosaur-egg/ -->       
</body>
</html>
    """
    return page

@app.route('/vanilla',methods = ['GET'])
def link():
    # get user input
        page = """
<html>
<head>
    <title>ICE CREAM</title>
</head>
<img src="https://www.yourhomebasedmom.com/wp-content/uploads/2017/07/vanilla-ice-cream-recipe-squarejpg.jpg">

</body>
</html>
        """
        return page

@app.route('/chocolate',methods = ['GET'])
def worm():
    # get user input
        page = """
<html>
<head>
    <title>ICE CREAM</title>
</head>
<img src="https://www.thespruceeats.com/thmb/T_Mru3-k0Zl9fqDaprCn2bjhek4=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/easy-chocolate-ice-cream-recipe-1945798-hero-01-45d9f26a0aaf4c1dba38d7e0a2ab51e2.jpg">

</body>
</html>
        """
        return page

@app.route('/strawberry',methods = ['GET'])
def strawberry():
    # get user input
        page = """
<html>
<head>
    <title>ICE CREAM</title>
</head>
<img src="https://www.thespruceeats.com/thmb/kpuMkqk0BhGMTuSENf_IebbHu1s=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/strawberry-ice-cream-10-0b3e120e7d6f4df1be3c57c17699eb2c.jpg">

</body>
</html>
        """
        return page


@app.route('/flag',methods = ['GET'])
def flag():
    # get user input
        page = """
<html>
<head>
    <title>ICE CREAM</title>
</head>
<p> 1 -  byuctf{ </p>

</body>
</html>
        """
        return page

@app.route('/zimbra',methods = ['GET'])
def zimbra():
    # get user input
        page = """
<html>
<head>
    <title>ICE CREAM</title>
</head>
<p> 2 -  d </p>

</body>
</html>
        """
        return page

@app.route('/2013',methods = ['GET'])
def twentythirteen():
    # get user input
        page = """
<html>
<head>
    <title>ICE CREAM</title>
</head>
<p> 3 - i </p>

</body>
</html>
        """
        return page

@app.route('/admin',methods = ['GET'])
def admin():
    # get user input
        page = """
<html>
<head>
    <title>ICE CREAM</title>
</head>
<p> 4 - rb_ </p>

</body>
</html>
        """
        return page 

@app.route('/zeus',methods = ['GET'])
def zeus():
    # get user input
        page = """
<html>
<head>
    <title>ICE CREAM</title>
</head>
<p> 5 - is_the_ </p>

</body>
</html>
        """
        return page

@app.route('/mojo',methods = ['GET'])
def mojo():
    # get user input
        page = """
<html>
<head>
    <title>ICE CREAM</title>
</head>
<p> 6 - lo </p>

</body>
</html>
        """
        return page     

@app.route('/tuscany',methods = ['GET'])
def tuscany():
    # get user input
        page = """
<html>
<head>
    <title>ICE CREAM</title>
</head>
<p> 7 - ml} </p>

</body>
</html>
        """
        return page                  


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=40008)