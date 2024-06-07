import os 
import secrets
from flask import Flask, render_template, url_for,flash,redirect,request , abort
from app.form import RegistrationForm,LoginForm,UpdateAccountForm,PostForm
from app import app , bcrypt , db
from app.models import User , Post
from flask_login import login_user , logout_user , current_user , login_required
from PIL import Image



@app.route("/")
def home():
    return render_template("home.html" ,posts = Post.query.all())

@app.route("/about")
def about():
    return render_template("about.html",title="About")

@app.route("/register",methods=["POST", "GET"])
def register():
    if current_user.is_authenticated :
        return redirect(url_for("home"))
    form = RegistrationForm()
    if form.validate_on_submit():
        hash_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data , email= form.email.data , password = hash_password)
        db.session.add(user)
        db.session.commit()
        
        flash(f"Your Account has been created!! You can Login Now.","success")
        return redirect(url_for('login'))
    
    return render_template("register.html", title = "Register",form=form)

@app.route("/login" , methods=["POST", "GET"])
def login():
    if current_user.is_authenticated :
        return redirect(url_for("home"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user and bcrypt.check_password_hash(user.password ,form.password.data):
            login_user(user,remember=form.remember.data)

            next_page = request.args.get('next')
                
            return redirect(next_page) if next_page else redirect(url_for("home"))
        else:
            flash('login unsuccessful. Please check username and password' , 'danger')

    return render_template("login.html", title = "Login",form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn

@app.route("/account" , methods =['POST' , 'GET'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
     if form.picture.data:
        picture_file = save_picture(form.picture.data)
        current_user.image_file = picture_file

        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash("Your Account has been Updated" ,'success')
    

        return redirect(url_for("account"))
    
    elif request.method == "GET":
        form.username.data = current_user.username
        form.email.data = current_user.email
    

    image_file = url_for('static' ,filename= 'profile_pics/' + current_user.image_file)

    return render_template("account.html" , tittle = "account" , image_file=image_file , form=form) 


@app.route("/new_post" , methods =['POST' , 'GET'] )
@login_required
def new_post():
    form = PostForm()
    
    if form.validate_on_submit():
        post = Post(title=form.title.data , content=form.content.data , author = current_user)
        db.session.add(post)
        db.session.commit()
        flash("Your Post has been created" ,'success')

        return redirect(url_for("home"))

    return render_template('create_post.html', legend = 'new post' ,title=new_post , form=form)

@app.route('/post/<int:post_id>')
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html' , title = post.title , post = post)

@app.route("/post/<int:post_id>/update", methods = ["POST", "GET"])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user: 
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash ("your post has been updated", "success")
        return redirect(url_for('post',post_id = post.id))
    elif request.method == "GET":
        form.title.data=post.title
        form.content.data=post.content
    return render_template("create_post.html",title="Update Post",form=form,legend="Update Post")


@app.route("/post/<int:post_id>/delete", methods = ["POST" , "GET"])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user: 
        abort(403)
    db.session.delete(post)
    db.session.commit()
    
    flash ("your post has been deleted", "success")
        
    return redirect(url_for('home'))
   
    

