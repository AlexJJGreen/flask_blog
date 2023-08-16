from flask import request, jsonify, render_template, redirect, url_for
from app import db
from . import bp


@bp.route("/")
@bd.route("/index")
def tracker_index():
    return render_template("index.html", page_title="Trackers")
