from flask import Flask, render_template
from main import main

app = Flask(__name__)


@app.route('/')
def hello_world():
    print('success')
    return render_template('index.html', filename='sample_movie.mp4')


@app.route('/create')
def create():
    main()
    return render_template('index.html', filename='movie.mp4')


if __name__ == ' __main__':
    app.debug = True
    app.run()
