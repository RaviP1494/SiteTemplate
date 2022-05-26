from flask import Flask, request, render_template, redirect

app = Flask(__name__)

app.config['SECRET_KEY'] = "thisisthekey"

@app.route('/')
def home():
    return render_template('index.html')