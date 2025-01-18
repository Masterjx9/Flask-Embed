## This is an example of how to use Flask with the Flask-Embed library.
from flask import Flask
from flask_embed import Embed
app = Flask(__name__)
embed = Embed()

@app.route('/')
def hello_world():
    return embed.render_template('index.html', embed=embed)

if __name__ == '__main__':
    app.run(debug=True)