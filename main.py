import requests
from flask import Flask,render_template, request,redirect,send_file
from  index import export_combine_jobs

app = Flask('remote_job_searching')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result')
def result():
    result = request.args.get('job')
    jobs = export_combine_jobs(result)
    count = len(jobs)
    return render_template('result.html',result=result,jobs=jobs,count=count)


app.run('')

