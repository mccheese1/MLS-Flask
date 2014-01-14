MLS app using flask

run 'pip install -r requirements.txt' in virtual environment to add flask, flask-wtf, and mysql-connector/python
	(requirements.txt is located in the same folder as this file)


running 'run.py' in the python intrepreter will start the server with debug = true, which allows code updates while the server is running.
this also allows code execution on the server, so this option should not be used in production environments. Instead, run 'runp.py' in 
production environments, this has debug = false (and will display a http 500 error if a code error happens to occur.)

app/static folder contains css/js/image files.

app/template folder contains all jinja2 templates

tmp folder contains logs (which are enabled when debug is set to false)
