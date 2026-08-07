# Personal portfolio
A personal website developed with Flask, HTML, CSS and JavaScript. It includes a projects section, an about me, a functional contact form and a responsive design.

## Technologies
- Flask
- HTML
- CSS
- JavaScript

## Features
- Responsive design.
- Contact form with email integration.
- Projects showcase.
- About Me section.
- Clean and modern user interface.

## How to run locally
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`.
3. Before running the application, create a `.env` file based on `.env.example` and replace the placeholder values with your own credentials.

| Variable        | Description                                                                 |
|-----------------|-----------------------------------------------------------------------------|
| `SECRET_KEY`    | Secret key used by the Flask application.                                   |
| `MAIL_USERNAME` | Gmail account used to send emails.                                          |
| `MAIL_PASSWORD` | Gmail App Password associated with the Gmail account.                       |
| `MAIL_SENDER`   | Email address used as the sender.                                           |
| `MAIL_RECEIVER` | Email address that will receive messages submitted through the contact form.|
4. Run the application: `python ./frontend/app.py`.

## Live demo
[View live demo](https://federicoariel.pythonanywhere.com)