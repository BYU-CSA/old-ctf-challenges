from flask import Flask, request, make_response
from urllib.parse import urlparse
from flask import send_from_directory
import os

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    page = """
<html>
    <head>
        <title>steggibois</title>
	  <link rel="icon" type="image/png" href="favicon.png" />
    </head>
    <body>
        <h1>HAVE YOU EVER READ ABOUT STEGGIBOIS????</h1>
    </body>
    <p>Stegosaurus (/ˌstɛɡəˈsɔːrəs/;[1] lit. 'roof-lizard') is a genus of herbivorous, four-legged, armored dinosaur from the Late Jurassic, characterized by the distinctive kite-shaped upright plates along their backs and spikes on their tails. Fossils of the genus have been found in the western United States and in Portugal, where they are found in Kimmeridgian- to early Tithonian-aged strata, dating to between 155 and 145 million years ago. Of the species that have been classified in the upper Morrison Formation of the western US, only three are universally recognized: S. stenops, S. ungulatus and S. sulcatus. The remains of over 80 individual animals of this genus have been found. Stegosaurus would have lived alongside dinosaurs such as Apatosaurus, Diplodocus, Brachiosaurus, Ceratosaurus, and Allosaurus; the latter two may have preyed on it.

        They were large, heavily built, herbivorous quadrupeds with rounded backs, short fore limbs, long hind limbs, and tails held high in the air. Due to their distinctive combination of broad, upright plates and tail tipped with spikes, Stegosaurus is one of the most recognizable kinds of dinosaurs. The function of this array of plates and spikes has been the subject of much speculation among scientists. Today, it is generally agreed that their spiked tails were most likely used for defense against predators, while their plates may have been used primarily for display, and secondarily for thermoregulatory functions. Stegosaurus had a relatively low brain-to-body mass ratio. It had a short neck and a small head, meaning it most likely ate low-lying bushes and shrubs. One species, Stegosaurus ungulatus, is one of the largest known of all the stegosaurians, reaching 7 metres (23 ft) in length and 3.8 metric tons (4.2 short tons) in body mass, and some specimens indicate an even larger body size.
        
        Stegosaurus remains were first identified during the "Bone Wars" by Othniel Charles Marsh at Dinosaur Ridge National Landmark. The first known skeletons were fragmentary and the bones were scattered, and it would be many years before the true appearance of these animals, including their posture and plate arrangement, became well understood. Despite its popularity in books and film, mounted skeletons of Stegosaurus did not become a staple of major natural history museums until the mid-20th century, and many museums have had to assemble composite displays from several different specimens due to a lack of complete skeletons. Stegosaurus is one of the better-known dinosaurs, and has been featured in film, postal stamps, and many other types of media.</p>
    <p>The quadrupedal Stegosaurus is one of the most easily identifiable dinosaur genera, due to the distinctive double row of kite-shaped plates rising vertically along the rounded back and the two pairs of long spikes extending horizontally near the end of the tail. S. stenops reached 6.5 m (21.3 ft) in length and 3.5 metric tons (3.9 short tons) in body mass, while S. ungulatus reached 7 m (23.0 ft) in length and 3.8 metric tons (4.2 short tons) in body mass.[28] Some large individuals may have reached 7.5 m (25 ft) in length and 5.0–5.3 metric tons (5.5–5.8 short tons) in body mass.[29][30]

        Most of the information known about Stegosaurus comes from the remains of mature animals; more recently, though, juvenile remains of Stegosaurus have been found. One subadult specimen, discovered in 1994 in Wyoming, is 4.6 m (15.1 ft) long and 2 m (6.6 ft) high, and is estimated to have weighed 1.5-2.2 metric tons (1.6-2.4 short tons)[31] while alive. It is on display in the University of Wyoming Geological Museum</p>
    </html>
    """
    return page


@app.route('/favicon.png')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.png', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=40012)