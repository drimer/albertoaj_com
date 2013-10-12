from flask import Flask, render_template
from werkzeug.routing import BaseConverter


app = Flask(__name__, template_folder='templates', static_path='/static')


class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]


app.url_map.converters['regex'] = RegexConverter


@app.route("/")
def hello():
    return render_template('about.html')


@app.route('/<regex(".*"):file_basename>.html')
def contact(file_basename):
    return render_template('%s.html' % file_basename)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=2323)
