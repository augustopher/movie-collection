import os
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, movies.db))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = database_file

db = SQLAlchemy(app)

@app.route('/', methods=['GET','POST'])
def home():
    if request.form:
        print(request.form)
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)

class Movie(db.Model):
    self.movie_id = db.Column(db.Integer, primary_key=True)
    self.movie_title = db.Column(db.String(200))
    
    def __repr__(self):
        return "<Title: {}>".format(self.movie_title)