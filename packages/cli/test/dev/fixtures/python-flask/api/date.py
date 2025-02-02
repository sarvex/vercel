from flask import Flask, Response
from datetime import datetime
app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def date(path):
    d = datetime.now().isoformat()
    return Response(f"Current date is {d}", mimetype='text/html')
