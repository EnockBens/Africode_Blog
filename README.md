# Price Tracker

This is a Flask web application that tracks and compares prices of items from Kilimall, Jiji, and Jumia. Users can register, log in, update their accounts, and post content. The application includes web scraping logic to fetch the latest prices of items from the three e-commerce websites.

## Features

- User Registration
- User Login
- Update Account Information
- Password Reset
- Search and Compare Item Prices
- Post Content

## Requirements

- Python 3.6 or higher
- Flask
- Flask-WTF
- Flask-Login
- Flask-SQLAlchemy
- Flask-Bcrypt
- Flask-Mail
- Requests
- BeautifulSoup4

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/pricetracker.git
    cd pricetracker
    ```

2. **Create a virtual environment**:
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Set up environment variables**:
    Create a `.env` file in the root directory and add the following environment variables:
    ```env
    FLASK_APP=run.py
    FLASK_ENV=development
    SECRET_KEY=your_secret_key
    SQLALCHEMY_DATABASE_URI=sqlite:///site.db
    MAIL_SERVER=smtp.googlemail.com
    MAIL_PORT=587
    MAIL_USE_TLS=1
    MAIL_USERNAME=your_email
    MAIL_PASSWORD=your_password
    ```

5. **Run the application**:
    ```sh
    flask run
    ```

6. **Navigate to the application**:
    Open your web browser and go to `http://127.0.0.1:5000/`.

## Usage

### User Registration

1. Go to the Registration page.
2. Fill out the registration form with a username, email, and password.
3. Submit the form to create a new account.

### User Login

1. Go to the Login page.
2. Enter your email and password.
3. Click the Login button to access your account.

### Update Account Information

1. Go to the Update Account page.
2. Update your username, email, and profile picture as needed.
3. Click the Update button to save changes.

### Password Reset

1. Go to the Request Password Reset page.
2. Enter your email address.
3. Submit the form to receive a password reset link.
4. Follow the instructions in the email to reset your password.

### Search and Compare Item Prices

1. On the homepage, enter the name of the item you want to search for.
2. Click the Search button.
3. View the search results with the latest prices from Kilimall, Jiji, and Jumia.

### Post Content

1. Go to the Create Post page.
2. Enter a title and content for your post.
3. Submit the form to create a new post.

## Directory Structure

