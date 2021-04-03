from flask import Flask , render_template ,request, redirect,flash ,url_for ,session
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///blog.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Blog(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(500), nullable=False)
    subject = db.Column(db.String(500), nullable=False)
    msg = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.name}- {self.email}-{self.subject}-{self.msg}"
@app.route('/')
def hello_world():
    # return 'Hello, World!'
    return render_template('index.html')
@app.route('/blog')
def blog():
    return render_template('blog.html')
@app.route('/blog/1')
def blog1():
    return render_template('blog1.html')
@app.route('/blog/2')
def blog2():
    return render_template('blog2.html')
@app.route('/gallery')
def gallery():
    return render_template('gallery.html')
@app.route('/contact',methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        msg = request.form['msg']
        blog = Blog(name=name,email=email,subject=subject,msg=msg)
        db.session.add(blog)
        db.session.commit()
       
       

    return render_template('contact.html')
@app.route('/admin')
def admin():
    blog = Blog.query.all()
    
    return render_template('admin.html',blog=blog)

if __name__ == "__main__":
 
    
    app.run(debug = True)