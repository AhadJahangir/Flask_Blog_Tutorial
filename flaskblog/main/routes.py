from flask import Blueprint, render_template, request, json, jsonify
from flaskblog import db
from flaskblog.models import Post
from flask_sqlalchemy import SQLAlchemy
import sqlite3

main = Blueprint('main', __name__)

#Sets route for home page and html template
#Lists 5 most recent blog posts on home page
@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)

#Sets route for about page and html template
@main.route("/about")
def about():
    return render_template('about.html', title='About')

#Sets route for an api endpoint returning JSON 
@main.route('/api/health')
def health():
    health = {
    "status": "ok"
}

    return jsonify(health)

#Sets route to see all blog posts from api endpoint
@main.route("/api/posts")  
def view():  
     con = sqlite3.connect("site.db")  
     con.row_factory = sqlite3.Row  
     cur = con.cursor()  
     cur.execute("SELECT * FROM post")   
     rows = cur.fetchall()  
     return render_template("table_posts.html",rows = rows)

#Sets route to see all users from api endpoint
@main.route("/api/users")  
def table_users():  
     con = sqlite3.connect("site.db")  
     con.row_factory = sqlite3.Row  
     cur = con.cursor()  
     cur.execute("SELECT * FROM user")   
     rows = cur.fetchall()  
     return render_template("table_users.html",rows = rows)


