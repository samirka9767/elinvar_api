

To be able to run the project install Python >=3.5 on your machine

Create python environment inside the project folder:

    Inside the elinvar_api folder run:

            python3 -m venv .venv

    Then activate the env with:

            source .venv/bin/activate

To install all the necessary libraries/models run requirements.txt file:

    pip install -r requirements.txt


The project runs with Flask, for that few environment variables need to be set up:

    Go inside the api folder and in console do the following:

        export FLASK_APP=application.py
        export FLASK_ENV=development

        To run the application:
            flask run

Note: if you quit the terminal, every time to run the project with flask the environment variables need to be set up first, before doing flask run

To run the tests in cli, use the following command:

    python3 -m unittest tests/*.py





