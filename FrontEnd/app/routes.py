from flask import render_template, send_file
from flask import Flask, flash, request, redirect, url_for
from app import app
import os
from os.path import join

basedir = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    target = os.path.join(basedir, 'audio_upload/')
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)
    
    for file in request.files.getlist("file"):
        filename = file.filename
        print(filename)
        destination = "/" + target + filename
        print(destination)
        file.save(destination)
    return render_template("uploaded_file.html")