import os

__version_info__ = (0, 0, 9)
__version__ = "0.0.9"

def setup(app):
    app.require_sphinx("1.6")
    theme_path = os.path.abspath(os.path.dirname(__file__))
    app.add_html_theme("sphinx_integral_theme", theme_path)
    return {"version": __version__, "parallel_read_safe": True}