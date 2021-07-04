from flask import Blueprint, render_template, request, json, jsonify
from flaskblog import db
from flaskblog.models import Post
from flask_sqlalchemy import SQLAlchemy
import sqlite3

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)

@main.route("/about")
def about():
    return render_template('about.html', title='About')

##Start Ishan tasks
@main.route('/api/health')
def health():
    health = {
    "status": "ok"
}

    return jsonify(health)



#@main.route('/testing', methods=['GET'])
#def testing():
 #   posts = Post.query.order_by(Post.date_posted.desc())
    #return render_template("testing.html", post=post)
  #  return render_template('home.html', posts=posts)
#Returning static html page

#@main.route('/testing2', methods=["GET"])
#def testing2():
    #user = User.query.filter_by(Email=request.form['email']).first()
 #   user = session['username'] = username.data

  #  return user
#Werkzeug error


@main.route("/api/posts")  
def view():  
     con = sqlite3.connect("site.db")  
     con.row_factory = sqlite3.Row  
     cur = con.cursor()  
     cur.execute("SELECT * FROM post")   
     rows = cur.fetchall()  
     return render_template("table_posts.html",rows = rows)
     #print(rows)

@main.route("/api/users")  
def table_users():  
     con = sqlite3.connect("site.db")  
     con.row_factory = sqlite3.Row  
     cur = con.cursor()  
     cur.execute("SELECT * FROM user")   
     rows = cur.fetchall()  
     return render_template("table_users.html",rows = rows)
     #print(rows)

#@main.route("/api/users/all")  
#def table_posts():  
 #    con = sqlite3.connect("site.db")  
  #   con.row_factory = sqlite3.Row  
   #  cur = con.cursor()  
    # cur.execute("SELECT * FROM user")   
    # rows = cur.fetchall()  
    # return render_template("table_posts.html",rows = rows)
     #print(rows)
##End Ishan tasks


