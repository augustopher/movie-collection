import os
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, 'movies.db'))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = database_file

db = SQLAlchemy(app)

@app.route('/', methods=['GET','POST'])
def home():
    if request.form:
        movie = Movie(movie_title=request.form.get('title'))
        db.session.add(movie)
        db.session.commit()
    
    movie_list = Movie.query.all()
    return render_template('home.html', movie_list=movie_list)

if __name__ == '__main__':
    app.run(debug=True)

class Movie(db.Model):
    movie_id = db.Column(db.Integer, primary_key=True)
    movie_title = db.Column(db.String(200))
    
    def __repr__(self):
        return "<Title: {}>".format(self.movie_title)