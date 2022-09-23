from flask import (url_for, session, Blueprint, render_template)
from . models import Task
bp = Blueprint('task', __name__)

@bp.route("/tasks", methods=("GET", ))
def index():
    # return render_template("lista.html"
    # , lista=lista
    # )
    return "Projetos"

@bp.route("/tasks/lista", methods=("GET", ))
def lista():
    lista = Task.query.all()
    return render_template("projetos/tarefas/lista.html"
    , lista=lista
    )