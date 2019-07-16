from flask import Flask, request, jsonify, render_template, redirect
import os
import json
import pusher
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
