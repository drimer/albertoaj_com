import re

import flask


BASE_URL = 'http://www.albertoaj.com/'


def render_template(template_path):
    in_str = flask.render_template(template_path)

    out_str = re.sub(r'(<img.*src=")([a-z/])(.*)(")',
                     r'\1%s\2\3\4' % BASE_URL,
                     in_str)

    out_str = re.sub(r'(<a.*href=")([a-z/])(.*)(")',
                     r'\1%s\2\3\4' % BASE_URL,
                     out_str)

    return out_str
