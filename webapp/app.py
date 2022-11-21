'''
    app.py
    Ryan Dunn and Kyle Machalec
    Updated Nov 20th
    A small Flask application to support our website. 
'''
import flask
import argparse
import api

app = flask.Flask(__name__, static_folder='static', template_folder='templates')
app.register_blueprint(api.api, url_prefix='/api')

@app.route('/')
def home():
    return flask.render_template('index.html')

@app.route('/data_analysis')
def graphs():
    return flask.render_template('data_analysis.html')

@app.route('/about_us')
def aboutUs():
    return flask.render_template('about_us.html')

@app.route('/natural_disasters')
def search():
    return flask.render_template('search_results.html', )

if __name__ == '__main__':
    parser = argparse.ArgumentParser('A disaster application, including API & DB')
    parser.add_argument('host', help='the host to run on')
    parser.add_argument('port', type=int, help='the port to listen on')
    arguments = parser.parse_args()
    app.run(host=arguments.host, port=arguments.port, debug=True)
