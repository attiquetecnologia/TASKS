from flask import (url_for, session, Blueprint, render_template)
from . models import Project
bp = Blueprint('project', __name__, url_prefix='/project')


@bp.route("/project", methods=("GET", ))
def lista():
    lista = Project.query.all()
    return render_template("lista.html"
    , lista=lista
    )