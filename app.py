from flask import Flask, render_template
from main import main

app = Flask(__name__)


@app.route('/')
def hello_world():
    main()
    print('success')
    return render_template('index.html')


if __name__ == ' __main__':
    app.debug = True
    app.run()
