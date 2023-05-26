from flask import Flask, Response, request
app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def user(path):
    name = request.args.get('name')
    return Response(f"Hello {name}", mimetype='text/html')
