from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template("index.html")

@main.route('/admin')
def admin():
    return "Admin panel - Access Restricted", 403

