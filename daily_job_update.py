import os
import json
import flask
from flask import render_template, request, redirect, url_for, json

app = flask.Flask(__name__)
app.config.from_pyfile('config.py')

job_updates = {}

@app.route('/')
def home():
	global job_updates
	if not job_updates:
		with open('data/placeholder_data.json', 'r') as json_file:
			job_updates = json.load(json_file)
	return render_template('job_update.html', job_updates=job_updates)

@app.route('/internal/', methods=['GET', 'POST'])
def internal_job_input():
	if request.method == 'POST':
		date = request.form['today_date']
		name = request.form['name']
		status = request.form['status']
		project_name = request.form['project_name']

		if date not in job_updates:
			job_updates[date] = []
		job_updates[date].append({
			'type': 'internal',
			'name': name,
			'status': status,
			'project_name': project_name
			})

		return redirect(url_for('home'))
	return render_template('input_internal.html')

@app.route('/external/', methods=['GET', 'POST'])
def external_job_input():
	if request.method == 'POST':
		date = request.form['today_date']
		project_name = request.form['project_name']
		members = request.form['member_name']
		location = request.form['location']
		ride = request.form['ride_no']
		funds = request.form['funds']
		time = request.form['time']

		if date not in job_updates:
			external_job_updates[date] = []
		job_updates[date].append({
			'type': 'external',
			'project_name': project_name,
			'members': members,
			'location': location,
			'ride': ride,
			'funds': funds,
			'time': time
			})

		return redirect(url_for('home'))
		
	return render_template('input_external.html')

@app.route('/wip/')
def wip():
    with open('data/wip_2023.json', 'r') as json_data:
        data = json.load(json_data)
    return render_template("wip.html", data=data)

if __name__ == '__main__':
	app.run()

