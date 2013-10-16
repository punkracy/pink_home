from flask import render_template, send_from_directory
from app import app
import os
@app.route('/favicon.ico')
def favicon():
  return send_from_directory(os.path.join(app.root_path, 'static'), 'img/favicon.ico')

@app.errorhandler(404)
def page_not_found(e):
  return render_template('404.html'), 404

@app.route('/')
@app.route('/index')
def index():
  return render_template('index.html')
