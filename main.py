import os
from flask import Flask, render_template, redirect
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

"""
{% extends 'base.html' %}
{% block _style %}{% endblock %}
{% block title %}{% endblock %}
{% block landing %}{% endblock %}
{% block content %}{% endblock %}

"""

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/2')
def template_2():
    return render_template('index2.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html', error=e), 404

@app.errorhandler(405)
def method_not_allowed(e):
    return render_template('error.html', error=e), 405

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('error.html', error=e), 500






if __name__=='__main__':
    # app.run(debug=True)
    app.run()