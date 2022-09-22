from flask import (url_for, session, Blueprint, render_template)
from . models import Project
bp = Blueprint('project', __name__)

@bp.route("/projects", methods=("GET", ))
def index():
    # return render_template("lista.html"
    # , lista=lista
    # )
    return "Projetos"

@bp.route("/projects/lista", methods=("GET", ))
def lista():
    lista = Project.query.all()
    return render_template("lista.html"
    , lista=lista
    )