To use this code you need python 3.9+ and Mongodb installed in your system
First create a virtualenv
<code>python -m venv venv</code>
<code>Source venv/bin/activate</code> For Unix system
<code>Source venv/Script/activate</code> For Windows system
To install the required dependencies
<code>pip install -r app/requirements.txt</code>

To run the database script to create the database collection and insert data:
<code>python db_script.py</code>

To run the FastAPI to test the APIs:
<code>cd app</code>
<code>python main.py</code>

Then open your browser and visit:
<code>http://127.0.0.1:8000/docs</code>