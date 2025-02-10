# How to run the app as an api via Docker
1. Within the directory `flask-app/python`, build the docker container `docker build --tag flask-app .`
2. Run the docker image locally on port 8000 `docker run -p 8000:8000 flask-app`

# How to run the app as an api without Docker
1. Create a virtual python environment (see *How to create and deactivate a python virtual environment*)
2. Enter `python3 app.py`

# How to run the tests via your command line
1. Create a virtual python environment (see *How to create and deactivate a python virtual environment*)
2. Enter `python3 tests.py`.

# How to create and deactivate a python virtual environment via your command line
This assumes that you have a unix like system.

1. Assuming you use a unix like system, ensure python3 and python3-venv is installed `apt-get install python3 python3-venv`
2. Create a new python virtual environment `python3 -m venv potatoenv`
3. Activate your new virtual environment `source potatoenv/bin/activate`
4. Install the python dependencies into your virtual environment `pip3 install -r requirements.txt`
5. When you are done with everything, enter `deactivate` to exit your virtual environment