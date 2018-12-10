from flask import Flask
import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from config import Config

UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = set(['wav'])

app = Flask(__name__)
app.config.from_object(Config)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

from app import routes