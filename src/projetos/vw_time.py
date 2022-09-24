from urllib import request
from flask import (url_for, session, Blueprint, render_template)
from sqlalchemy.orm import joinedload
from . models import Project, TaskTime
bp = Blueprint('task', __name__)

@bp.route("/times/add", methods=("GET", ))
def add():
    projects = Project.query.all()
    return render_template("projetos/tarefas/form.html", projects=projects)

@bp.route("/tasks/form", methods=("POST", ))
def form():
    # return render_template("lista.html"
    # , lista=lista
    # )
    
    return f"""Mensagem"""

@bp.route("/tasks/lista", methods=("GET", ))
def lista():
    query = TaskTime.query.options(joinedload('task'))
    lista = TaskTime.query.all()
    return render_template("projetos/tarefas/tempo/lista.html"
    , lista=lista
    )