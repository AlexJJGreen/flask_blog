from flask import Blueprint

bp = Blueprint(
    "trackers",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/static",
)

from . import routes
