from flask import Flask, render_template

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

if __name__ == '__main__':
	app.run()

