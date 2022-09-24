from flask import (url_for, session, Blueprint, render_template, request)
from sqlalchemy.orm import joinedload
from . models import Project, Task
from app import db
bp = Blueprint('task', __name__)

@bp.route("/times/add", methods=("GET", ))
def add():
    projects = Project.query.all()
    return render_template("projetos/tarefas/form.html", projects=projects)


@bp.route("/tasks/form", methods=("POST", ))
def form():
    data = {
        "task_name": request.form.get("task_name")
        ,"project_id": request.form.get("project_id")
        ,"status": request.form.get("status")
        ,"concluido": request.form.get("concluido")=="on" or False
    }
    task = Task(**data)
    db.session.add(task)
    db.session.commit()
    
    return f"""Mensagem"""

@bp.route("/tasks/lista", methods=("GET", ))
def lista():
    query = Task.query.options(joinedload('project'))
    lista = Task.query.all()
    return render_template("projetos/tarefas/lista.html"
    , lista=lista
    )