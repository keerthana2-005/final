# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask,render_template

# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)

anime_data = [
    {
        "title": "Solo Leveling",
        "writer": "Chungog",
        "art": "Redice Studio",
        "reads": "2.5B",
        "description": "One of the best action fantasy manhwa...",
        "image": "img1.webp"
    },
    {
        "title": "Tower of God",
        "creator": "Lee Jong Hui",
        "release": "2010–Present",
        "episodes": "197",
        "reads": "1.2B",
        "description": "Tower of God focuses on Twenty-Fifth Bam...",
        "image": "img2.webp"
    },
    {
        "title": "Hardcore Leveling Warrior",
        "creator": "Sehoon Kim",
        "description": "A story of a powerful player...",
        "image": "img3.webp"
    }
]

# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return render_template('home.html')
@app.route('/anime/<int:index>')
def get_anime(index):
    if 0 <= index < len(anime_data):
        return jsonify(anime_data[index]) # type: ignore
    return jsonify({'error': 'Anime not found'}), 404 # type: ignore

# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application 
    # on the local development server.
    app.run()
