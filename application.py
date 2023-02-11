from flask import Flask,render_template,request
import scraper
import requests

applications = Flask(__name__)

app = applications



@app.route('/',method=['GET'])
def homepage():
    return render_template('index.html')

@app.route('/scrape',method=['GET', 'POST'])
def scrapper();
    channel = request.form['content'].replace(" ","")
    obj = scraper(channel)
    obj.scrape()
