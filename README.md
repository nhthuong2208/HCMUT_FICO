# HCMUT_FICO

HCMUT_FICO is a software designed for Bank to check user's eligibility for a loan. It uses machine learning Model using Gradient Boosting method and Flask for frontend and backend

## How to run

Firstly, install and activate virtual environment package for your machine (this is used for MacOS). To install ```virtualenv``` run:
```bash
pip install virtualenv
```

Go to the project and create virtual environment
```bash
virtualenv venv
```
Then, activate the virtual environment
```bash
source venv/bin/activate
```

Sencondly, install all dependencies in ```requirements.txt``` file:
```bash
pip install requirements.txt
```

Finally, run the project
```bash
python run.py
```

To view the frontend of the web, change the url to http://127.0.0.1:5000/view
