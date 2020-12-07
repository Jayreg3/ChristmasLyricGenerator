from flask import Flask, request, make_response
from flask_cors import CORS

app = Flask(__name__)
app.config["DEBUG"] = True

CORS(app)

# Home page
@app.route('/')
def home():
    return ("<h1>Christmas Lyric Genetator</h1>"
     + "<p>This site is a small API for generating new christmas lyrics from a model trained on Billboard 100 Christmas songs.</p>"
     + "<p>Reference the endpoint /new to get 50 lines of original text followed by 30 lines of generated christmas lyrics, separated by '|'.</p>")

# A route to return the generated Christmas text
@app.route('/new', methods=['GET'])
def api_all():
    import generator
    # Allows GET requests from any origin with the Content-Type
    # header and caches preflight response for an 3600s
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': '*',
    }
    return (generator.generateLyrics(), 200, headers)
    # response = make_response(generator.generateLyrics())
    # response.headers['Access-Control-Allow-Origin'] = '*'
    # return response

# https://cloud.google.com/appengine/docs/standard/python3/building-app/writing-web-service
if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(port=8080, host="127.0.0.1", debug=True)