import os
import flask
from flask import render_template, request, redirect, url_for,json

app = flask.Flask(__name__)
app.config.from_pyfile('config.py')

job_updates = {'external': [], 'internal': []}

@app.route('/')
def home():
	return render_template('job_update.html', job_updates=job_updates)

@app.route('/internal/', methods=['GET', 'POST'])
def internal_job_input():
	if request.method == 'POST':
		date = request.form['today_date']
		name = request.form['name']
		status = request.form['status']
		if not request.form['project_name']:
			project_name = None
		else:
			project_name = request.form['project_name']

		job_updates['internal'].append({
			'date': date,
			'project_name': project_name,
			'name': name,
			'status': status
			})
		return redirect(url_for('home'))
	return render_template('input_internal.html')

@app.route('/external/', methods=['GET', 'POST'])
def external_job_input():
	if request.method == 'POST':
		date = request.form['today_date']
		project_name = request.form['project_name']
		members = request.form['member_name']
		ride = request.form['ride_no']
		funds = request.form['funds']
		time = request.form['time']

		job_updates['external'].append({
			'date': date,
			'project_name': project_name,
			'members': members,
			'ride': ride,
			'funds': funds,
			'time': time
			})
		return redirect(url_for('home'))
		
	return render_template('input_external.html')

@app.route('/wip/')
def wip():
    data = []
    with open('data/wip_2023.json', 'r') as json_data:
        data = json.load(json_data)
    return render_template("wip.html", data=data)

if __name__ == '__main__':
	app.run()

