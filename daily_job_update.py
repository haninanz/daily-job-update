import os
from flask import Flask, json, render_template

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('job_update.html')

@app.route('/internal/')
def internal_job_input():
	return render_template('input_internal.html')

@app.route('/external/')
def external_job_input():
	return render_template('input_external.html')

@app.route('/wip/')
def wip():
    data = []
    with open('data/wip_2023.json', 'r') as json_data:
        data = json.load(json_data)
    return render_template("wip.html", data=data)

if __name__ == '__main__':
	app.run()

