# Flask-Lab

Structure:
- app.py
- requirements.txt
- templates/
- static/
- notebooks/
- models/

How to run (Windows PowerShell):
1. conda create -n flasklab python=3.10 -y
2. conda activate flasklab
3. pip install -r requirements.txt
4. python app.py
5. Open http://127.0.0.1:5000

How to deploy files:
- Put your trained model file as `models/model.pkl`
- Put notebooks (converted to HTML) in `notebooks/` to view them
