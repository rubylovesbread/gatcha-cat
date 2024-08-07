from flask import Flask
import main

app = Flask(__name__)

@app.route('/')
def hello_world():
    main()
    return 'Hello, World!'