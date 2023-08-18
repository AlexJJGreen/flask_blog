from flask import request, jsonify, render_template, redirect, url_for
from app import db
from . import bp


@bp.route("/index")
def index():
    return render_template("index.html", page_title="Trackers")


@bp.route("/PE_workout")
def PE_workout():
    return render_template("PE_workout.html", page_title="PE Workout")
