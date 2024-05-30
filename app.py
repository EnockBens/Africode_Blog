from flask import Flask, render_template, url_for,flash,redirect
from form import RegistrationForm,LoginForm

app = Flask(__name__)
app.config ['SECRET_KEY'] = 'fc16444c9d60f0e0da50ea99cd684e47'
posts=[
    {"author":"Dolly chepkorir",
     "title":"Blog Post 1",
     "content":"First post content",
     "date_posted":"May 27,2024"},
     {"author":"Enock Benz",
     "title":"Blog Post 2",
     "content":"Second post content",
     "date_posted":"May 27,2024"},
     {"author":"Enock bett",
     "title":"Blog Post 3",
     "content":"Third post content",
     "date_posted":"May 27,2024"}
]

@app.route("/")
def home():
    return render_template("home.html",posts=posts)

@app.route("/about")
def about():
    return render_template("about.html",title="About")

@app.route("/register",methods=["POST", "GET"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!","success")
        return redirect(url_for('home'))
    return render_template("register.html", title = "Register",form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", title = "Login",form=form)

if __name__ == "__main__":
    app.run(debug=True , port = 5006)