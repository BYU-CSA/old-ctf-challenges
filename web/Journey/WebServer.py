from flask import Flask, request, make_response
from urllib.parse import urlparse

FLAG = "byuctf{C00KIES_SHOULDNT_AUTHENTICATE_CLIENTSIDE!}"
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    page = """
<html>
<head>
    <title>JOURNEY</title>
</head>
<body style="text-align:center;">
    <br><br>
    <h1 style="font-weight: bold">Welcome to the PALEOLITHIC era!</h1>
    <p style="color: blue">We are so excited you have come to take a look at our JURASSIC PARK!
    <br><br><br>
<div style="background-image: url('https://m.media-amazon.com/images/I/71BkE7Jet7L.jpg');">    
<iframe width="560" height="315" src="https://www.youtube.com/embed/D8zlUUrFK-M" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

    <h2 style="font-weight: bold"> THIS MONTH'S FEATURED DINOSAUR: The Fearsome ELASMOSAURUS </h2>
    <img  width="600" height="400" src="https://scitechdaily.com/images/Plesiosaur-Elasmosaurus.jpg">
    <p style="color: red"> Elasmosaurus (/ɪˌlæzməˈsɔːrəs, -moʊ-/;[1]) is a genus of plesiosaur that lived in North America during the Campanian stage of the Late Cretaceous period,
     about 80.5 million years ago. The first specimen was discovered in 1867 near Fort Wallace, Kansas, US, and was sent to the American paleontologist Edward 
     Drinker Cope, who named it E. platyurus in 1868. The generic name means "thin-plate reptile", and the specific name means "flat-tailed". Cope originally
      reconstructed the skeleton of Elasmosaurus with the skull at the end of the tail, an error which was made light of by the paleontologist Othniel Charles 
      Marsh, and became part of their "Bone Wars" rivalry. Only one incomplete Elasmosaurus skeleton is definitely known, consisting of a fragmentary skull,
       the spine, and the pectoral and pelvic girdles, and a single species is recognized today; other species are now considered invalid or have been moved
        to other genera. </p>
</div>        
</body>
</html>
    """
    resp = make_response(page)
    resp.set_cookie('role', 'FD6C')
    return resp 


@app.route('/flag',methods = ['GET'])
def link():
    # get user input
    role = request.cookies.get('role')
    if role == "25>:?":
        page = """
<html>
<head>
    <title>JOURNEY</title>
</head>
<p> Hey Admin, did you need the magic phrase for the food for the dinosaur's? The phrase is: byuctf{C00KIES_SHOULDNT_AUTHENTICATE_CLIENTSIDE}</p>

</body>
</html>
        """
        return page
    else:
        return "Not authorized."  





if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=40007)