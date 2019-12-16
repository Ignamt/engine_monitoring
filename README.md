# Python Base Repo - Flask

This repo is a project template for any kind of app or microservice. It's based on Flask and served with Gunicorn.

## Basic Python setup

The requirements are specified in the requirements.txt file, and the setup.py has the minimal arguments to install everything.To install the requirements, run `pip install -r requirements.txt` To install the repo as a module, run `pip install .` while standing on this repo's top-level.

Your app's code goes inside the src folder. It needs to be placed inside directories that contain an `__init__.py` file (which will become python modules and packages) which will make the code available from everywhere once you install the whole repo as a package.

You then need to implement your code directly onto the API or by registering blueprints. 


## Docker support

This repo also has a Dockerfile (to build a production-ready image) and a docker-compose for development.

In order to build the Docker image, you have to be at the top level directory, pass the current directory as context while specifying the path to the docker image with the following command:

```docker build . -f Docker/Dockerfile```

You can also specify a tag with the `-t <registry>/<image-name>:<tag>` option, replacing all the `<>` with values.

The image will copy everything in the repo (excluding the files specified in the `.dockerignore` file), upgrade pip and setuptools, install requirements and the current repo. It then sets the default run command to running gunicorn using the `gunicorn.conf.py` file.

You can run a "development-mode" with docker-compose. To do this you need to move into the `Docker` folder and run `docker-compose up`. The docker-compose.yaml file downloads a python:3.8 image, sets up the repo as a volume, binds the container's 8080 port to the host's 8080 port and runs the gunicorn command. With this setup, any changes you make to your code base will be updated live and will be present inside your container. It also defines the ENV variable to dev, which the gunicorn config file uses to enable the `reload` parameter.
