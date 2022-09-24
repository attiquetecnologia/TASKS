from urllib import request
from flask import (url_for, session, Blueprint, render_template)
from sqlalchemy.orm import joinedload
from . models import Task
bp = Blueprint('task', __name__)

@bp.route("/tasks/form", methods=("POST", ))
def form():
    # return render_template("lista.html"
    # , lista=lista
    # )
    
    return f"""Mensagem"""

@bp.route("/tasks/lista", methods=("GET", ))
def lista():
    query = Task.query.options(joinedload('project'))
    lista = Task.query.all()
    return render_template("projetos/tarefas/lista.html"
    , lista=lista
    )