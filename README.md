# FLASK-REACT (Docker edition)

This template has been created as a tool to speed up the process of creation and hosting of a fullstack app.

DISCLAIMER : THIS TEMPLATE HAS BEEN CREATED FOR PERSONNAL USE AS A SIDE PROJECT IT DOES NOT NECESSERILY FEATURES THE BEST DEVLOPMENT PRACTICES. ITS ONLY GOAL IS TO PROVIDE SOME BOILERPLATE CODE FOR A FAST DEPLOYMENT OF A SIMPLE FULLSTACK APP.



# TEMPLATE SETUP PROCEDURE

This setup procedure is suitable for a freshly cloned folder (from git) on a fresh machine.

REQUIREMENTS :

=> PYTHON 3.10.4 OR LATER ;

=> NODE.JS 16.XX.X OR LATER ;

=> NPM 8.15.0 OR LATER ;

All other required packages and dependencies will be installed during the setup process. You'll find the full list of required packages in the requirement.txt and package.json files.



# A - Environement setup

Upon downloading of this template the first step is to ensure the correct environment is set up.


A.1 - Flask environement setup

It is highly recommended to use this app in a virtual environement to ensure a proper python dependency management :

=> Go in the main app directory and run the command :

$ pip3 install pipenv       (if not already installed)

$ pipenv shell

=>Then all the packages the project needs to work have to be installed. The list of theses packages resides in the requirement.txt file (or Pifile see note). To install all packages from the requirement.txt file use the command :

$ pipenv install -r ./requirements.txt


A.2 - Javascript environement setup

All javascript dependencies are listed in the package.json file in the frontend folder.

=>To install all javascript dependencies, navigate to the frontend directory and run the command :
    
$ npn install

This command will install all dependencies listed in the package.json file



# B - Launching the developpement environement

Both Django and React have their own develpmentevironement that need to be launched in order tu run the code.


B.1 - Flask

=> (Option 1) Flask developement server 

To launch the Flask web server be sure to have the virtual environment up and running then naviguate in the backend directory and use the command :

$ python3 server.py

This command will launch the python server that will be avaiblable at the following address (local) : 127.0.0.1:5000

In this template Flask is configured to serve the React app on the root address however this features requires to generate a live build. Without a live build the root adress (127.0.0.1:8000) leads to nothing. If you want to generate a live build manually, refer to the "manual live build" section of this document.

=> (Option 2) Gunicorn production server  

Although gunicorn will be used as a production server it is possible to use it instead of the stock Flask dev server.

To launch the gunicorn server for production use the following command in the backend directory of the app :

$ gunicorn wsgi:app --bind 0.0.0.0:8000


B.2 - React

To launch the react devlopment environment simply use the following command in the frontend directory :

npm start

The React development environement has it's own webserver accessible at the address :

localhost:3000

In this template Flask is configured to serve the React app on its root address however this require a live build. While on a development build use the localhost address.


# C - Creation of the .env file

WIP 


# UPDATING DEPENDENCIES

# A. Python dependencies

If you wish to install new Python dependencies this requirement.txt file will NOT update itself automatically to update it use the following command :

$ pip freeze > requirement.txt


# B. Node dependencies

The package.json update itself automatically when new dependencies are installed.


# DESCRIPTION OF THE MAIN COMPONENTS OF THE APP

WIP

# DOCKER IMAGE BUILDING PROCEDURE

# A. Creating a react live build

Generating a manual live build is quite straight forward :
=> The first step requires to naviguate with the console in the frontend directory and run the command :

$ npm run build

This command will bundle all the react code into static files and store them into a "build" folder in the root  directory.

The Flask app is setup to serve the index.html file and all other static file from the build folder on its root address.


# B. Updating the dockerfile

In order to move to a developpement build it's necessary to transfer the ENV variables to the container.

WIP


# C. Building and running the image

The app is composed of two containers. The main app container and the nginx container. To launch both containers concurrently use the following command :

$ docker-compose up -d

To bring the app down use this command :

$ docker-compose down 
