from flask import Flask, Response, request, __version__
app = Flask(__name__)

@app.route('/api/', defaults={'path': ''})
@app.route('/api/<path:path>')
def catch_all(path):
    qs = request.args.to_dict()
    return Response(f"path: {path} query: {qs}", mimetype='text/html')
