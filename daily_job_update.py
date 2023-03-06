import json
import flask
from flask import render_template, request, redirect, url_for, json

app = flask.Flask(__name__)
app.config.from_pyfile('config.py')

working_date = []
external_jobs = {}
internal_jobs = {}

@app.route('/')
def home():
	global external_jobs, internal_jobs
	if not external_jobs:
		with open('data/placeholder_external.json', 'r') as external_json:
			external_jobs = json.load(external_json)
	if not internal_jobs:
		with open('data/placeholder_internal.json', 'r') as internal_json:
			internal_jobs = json.load(internal_json)
	# if external_jobs and internal_jobs:
	# 	job_updates = {'external': external_jobs, 'internal': internal_jobs}
	# 	with open('data/job_updates.json', 'w') as jobs_json:
	# 		json.dump(job_updates, jobs_json)

	working_date = list(set(list(external_jobs.keys()) + list(internal_jobs.keys())))

	return render_template('job_update.html',
		working_date=working_date,
		external_jobs=external_jobs,
		internal_jobs=internal_jobs
		)

@app.route('/internal/', methods=['GET', 'POST'])
def internal_job_input():
	global internal_jobs
	if request.method == 'POST':
		date = request.form['today_date']
		name = request.form['name']
		status = request.form['status']
		project_name = request.form['project_name']

		if date not in internal_jobs:
			internal_jobs[date] = []
		internal_jobs[date].append({
			'type': 'internal',
			'name': name,
			'status': status,
			'project_name': project_name
			})
		return redirect(url_for('home'))

	return render_template('input_internal.html')

@app.route('/external/', methods=['GET', 'POST'])
def external_job_input():
	global external_jobs
	if request.method == 'POST':
		date = request.form['today_date']
		project_name = request.form['project_name']
		members = request.form['member_name']
		location = request.form['location']
		ride = request.form['ride_no']
		funds = request.form['funds']
		time = request.form['time']

		if date not in external_jobs:
			external_jobs[date] = []
		external_jobs[date].append({
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

