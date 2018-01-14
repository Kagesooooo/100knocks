from flask import Flask, render_template, request, redirect, url_for
import numpy as np
import pymongo

client = pymongo.MongoClient()
db = client.testdb
collection = db.artist

app = Flask(__name__)

@app.route('/')
def index():
    title = "ようこそ"
    return render_template('index.html',title=title)

@app.route('/post', methods=['GET', 'POST'])
def post():
    title = "こんにちは"
    if request.method == 'POST':
        name = request.form['name']
        list0 = []
        for i in collection.find({'name':name}).sort('rating.count',-1).limit(10):
            list0.append(i)
        if list0 == []:
            for i in collection.find({'aliases.name':name}).sort('rating.count',-1).limit(10):
                list0.append(i)
        if list0 == []:
            for i in collection.find({'tags.value':name}).sort('rating.count',-1).limit(10):
                list0.append(i)
        return render_template('index.html', list0=list0, title=title)
    else:
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
