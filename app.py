import os
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, 'movies.db'))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = database_file

db = SQLAlchemy(app)

class Movie(db.Model):
    movie_id = db.Column(db.Integer, primary_key=True)
    movie_title = db.Column(db.String(200))
    
    def __repr__(self):
        return "<Title: {}>".format(self.movie_title)

@app.route('/', methods=['GET','POST'])
def home():
    if request.form:
        movie = Movie(movie_title=request.form.get('title'))
        db.session.add(movie)
        db.session.commit()
    
    movie_list = Movie.query.all()
    return render_template('home.html', movie_list=movie_list)

@app.route('/update', methods=['POST']):
def update():
    old_title = request.form.get('old_title')
    new_title = request.form.get('new_title')
    
    movie = Movie.query.filter_by(movie_title=old_title).first()
    movie.movie_title = new_title
    db.session.commit()
    
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)