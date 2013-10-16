from flask import Flask, render_template, send_from_directory

app = Flask(__name__)
from app import views
