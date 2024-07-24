# Flask Blog Application

This is a simple blog application built using Flask, a popular Python web framework. The application allows users to register, log in, create posts, update their profile, and reset their password.

## Features

- User registration and authentication
- User profiles with profile pictures
- Post creation, editing, and deletion
- Pagination for posts
- Email notifications for password resets

## Getting Started

To clone and use this application, follow these steps:

1. Install Python 3.x and pip (Python package manager)
2. Create a virtual environment (optional but recommended)
3. Clone the repository: `git clone https://github.com/your-username/flask-blog-app.git`
4. Navigate to the project directory: `cd flask-blog-app`
5. Install dependencies: `pip install -r requirements.txt`
6. Set up the database:
   - Create a new SQLite database: `touch app.db`
   - Initialize the database: `python run.py db init`
   - Migrate the database: `python run.py db migrate`
   - Upgrade the database: `python run.py db upgrade`
7. Run the application: `python run.py`
8. Access the application in your browser at http://localhost:5000

## Contributing

Contributions are welcome! To contribute to the project, follow these steps:

1. Fork the repository: https://github.com/your-username/flask-blog-app
2. Create a new branch for your changes: `git checkout -b your-feature-branch`
3. Make your changes and commit them: `git commit -am 'Add your feature'`
4. Push your changes to your fork: `git push origin your-feature-branch`
5. Create a pull request on the original repository

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/your-username/flask-blog-app/blob/main/LICENSE) file for more information.

## Acknowledgments

This application was built using the following resources:

- [Flask Documentation](https://flask.palletsprojects.com/en/2.0.x/)
- [Flask-WTF](https://flask-wtf.readthedocs.io/en/stable/)
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
- [Flask-Login](https://flask-login.readthedocs.io/en/latest/)
- [Bootstrap](https://getbootstrap.com/)
- [Font Awesome](https://fontawesome.com/)
- [Gravatar](https://en.gravatar.com/)
- [Email-Validator](https://email-validator.readthedocs.io/en/latest/)
- [Flask-Mail](https://pythonhosted.org/Flask-Mail/)
- [Flask-Bcrypt](https://flask-bcrypt.readthedocs.io/en/latest/)
- [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/)
- [Flask-Bootstrap](https://pythonhosted.org/Flask-Bootstrap/)
- [Flask-Moment](https://flask-moment.readthedocs.io/en/latest/)
- [Pillow](https://pillow.readthedocs.io/en/stable/)
- [Python-dotenv](https://github.com/theskumar/python-dotenv)
- [Flask-CKEditor](https://flask-ckeditor.readthedocs.io/en/latest/)
- [Flask-Admin](https://flask-admin.readthedocs.io/en/latest/) (optional)

