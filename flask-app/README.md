# How to run
1. Within the directory `flask-app/python`, build the docker container `docker build --tag flask-app .`
2. Run the docker image locally on port 8000 `docker run -p 8000:8000 flask-app`

# How to run the tests
1. Make sure that the python-flask-app docker image is running
2. Within the directory `flask-app`, run `sh test_endpoints.sh`