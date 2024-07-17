**Flask Random Name Generator**

This is a simple Python Flask application that generates random names and assigns them to subwebsites you visit on localhost. The names and their corresponding URLs are stored in a Redis database.

***Installation***

To get started, you need to have Python, Flask, and Redis installed on your system. Follow these steps to set up the project:

Clone the repository:
    
    git clone https://github.com/Nisgames/flask-demo.git
    cd flask-demo

Create and activate a virtual environment:
    
    python3 -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`

Install the dependencies:
    
    pip install -r requirements.txt

***By default, the application will be accessible at http://localhost:5000.***
Visit the root URL:
    Open a web browser and go to http://localhost:5000. This will redirect you to a subwebsite with a randomly generated name.

Endpoints

    /: Redirects to a subwebsite with a randomly generated name.
    /<name>: Displays the name of the subwebsite and stores it in the Redis database.

