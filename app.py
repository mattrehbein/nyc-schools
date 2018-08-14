from flask import Flask
from flask import request
from flask_sqlalchemy import SQLAlchemy
from flask import render_template
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///schools.db'
db = SQLAlchemy(app)

class School(db.Model):
  __tablename__ = 'schools'
  __table_args__ = {
    'autoload': True,
    'autoload_with': db.engine
  }
  dbn = db.Column(db.String, primary_key=True)

@app.route("/")
def hello():
  schools = School.query.all()
  return render_template("list.html", schools=schools)

@app.route("/schools/")
def schools():
  schools = School.query.all()
  return render_template("list.html", schools=schools)

@app.route("/schools/<dbn>/")
def school(dbn):
  school = School.query.filter_by(dbn=dbn).first()
  return render_template("show.html", school=school)

# @app.route("/search")
# def search():
#   name = request.args.get('query')
#   schools = School.query.filter(School.school_name.contains(name)).all()
#   return render_template("list.html", schools=schools)


# If this is running from the command line
# do something
if __name__ == '__main__':
  app.run(debug=True)



# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask import render_template
# app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///schools.db'
# db = SQLAlchemy(app)

# class School(db.Model):
#   __tablename__ = 'schools'
#   __table_args__ = {
#     'autoload': True,
#     'autoload_with': db.engine
#   }
#   dbn = db.Column(db.String, primary_key=True)

# @app.route("/")
# def hello():
#   return "Hello World!"

# @app.route("/schools")
# def schools():
#   schools = School.query.all()
#   return render_template("list.html", schools=schools)

# @app.route("/schools/<dbn>")
# def school(dbn):
#   school = School.query.filter_by(dbn=dbn).first()
#   return render_template("show.html", school=school)


# # If this is running from the command line
# # do something
# if __name__ == '__main__':
#   app.run(debug=True)


# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask import render_template
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///schools.db'
# db = SQLAlchemy(app)

# # THIS IS WHAT WE JUST COPIED AND PASTED
# # dbn is the unique school identifier column in our schools table in our schools.db
# class School(db.Model):
#   __tablename__ = 'schools'
#   __table_args__ = {
#     'autoload': True,
#     'autoload_with': db.engine
#   }
#   dbn = db.Column(db.String, primary_key=True)


# @app.route("/")
# def hello():
#     return "Hello World!"

# @app.route("/schools")
# def schools():
#     return "This is some schools"

# @app.route("/school")
# def school():
# 	school = School.query.first()
#     return render_template("show.html", name=school.school_name)


# # If this is running from the command line
# # do something
# if __name__ == '__main__':
#   	app.run(debug=True)


# MY PREV WITH SOME ADDITIONAL NOTES

# from flask import Flask
# # render_template lets us use an html template
# from flask_sqlalchemy import SQLAlchemy
# from flask import render_template
# #makes new Flask app:
# app = Flask(__name__)

# # routes are like API endpoints; they use /something to get to specific content on a site
# @app.route("/")
# def hello():
#     return "Hello World!"

# @app.route("/schools")
# def schools():
# 	return "This is some schools"

# @app.route("/school")
# def school():
# 	return render_template("show.html", name="Columbia High School")


# # If this is running from the command line
# # do something
# if __name__ == '__main__':
#   app.run(debug=True)