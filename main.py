import requests
from flask import Flask,render_template, request,redirect,send_file
from  index import export_combine_jobs
from  datas.save import save_file

app = Flask('remote_job_searching')

server = app.server

db = {}
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result')
def result():
    result = request.args.get('job')
    try:
         
        if result:
            result = result.lower()
            searched_job = db.get(result)
            if searched_job:
                jobs = []
                jobs = searched_job
            else:
                jobs = export_combine_jobs(result)
                db[result] = jobs
        else:
            raise Exception()
    except:
        return redirect('/error')
    return render_template('result.html',result=result,jobs=jobs,count=len(jobs))

@app.route('/export')
def export_file():
    try:
        word = request.args.get('word')
        if not word:
            raise Exception()
        word = word.lower()
        jobs = db.get(word)
        if not jobs:
            raise Exception()
        save_file(jobs)
        return send_file('jobs.csv')
    except:
        return redirect('/error')

@app.route('/error')
def error():
    return render_template('error.html')

# app.run('')


