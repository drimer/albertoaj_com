import re

from flask import Flask, render_template, render_template_string
from werkzeug.routing import BaseConverter

from library import template


def add_regex_support():
    class RegexConverter(BaseConverter):
        def __init__(self, url_map, *items):
            super(RegexConverter, self).__init__(url_map)
            self.regex = items[0]

    app.url_map.converters['regex'] = RegexConverter


app = Flask(__name__, template_folder='templates', static_path='/static')
add_regex_support()


@app.route("/")
def hello():
    return render_template_string(template.render_template('about.html'))


@app.route('/<regex(".*"):file_basename>.html')
def contact(file_basename):
    template_path = '%s.html' % file_basename
    return template.render_template(template_path)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=2323)
