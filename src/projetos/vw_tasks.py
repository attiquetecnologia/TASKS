from flask import (url_for, session, Blueprint, render_template, request)
from sqlalchemy.orm import joinedload
from . models import Project, Task
from app import db
bp = Blueprint('task', __name__)

@bp.route("/tasks/add", methods=("GET", ))
def add():
    projects = Project.query.all()
    return render_template("projetos/tarefas/form.html", projects=projects)

@bp.route("/tasks/edit/<int:id>", methods=("GET", ))
def edit(id):
    record = Task.query.filter_by(id=id).first()
    projects = Project.query.all()
    return render_template("projetos/tarefas/form.html", record=record, projects=projects)


@bp.route("/tasks/form", methods=("POST", ))
def form():
    if request.form.get("id"):
        record = Task.query.filter_by(id=request.form.get("id")).first()
        # data['id'] = request.form.get("id")
        # task = Task(**data)
        record.task_name = request.form.get("task_name")
        record.project_id = request.form.get("project_id")
        record.status = request.form.get("status")
        record.concluido = request.form.get("concluido")=="on" or False
    else:
        task = Task(**{
            "task_name": request.form.get("task_name")
            ,"project_id": request.form.get("project_id")
            ,"status": request.form.get("status")
            ,"concluido": request.form.get("concluido")=="on" or False
            })
        db.session.add(task)

    db.session.commit()
    return f"""<p class="alert alert-success">Dados inseridos com sucesso!<p>"""

@bp.route("/tasks/lista", methods=("GET", ))
def lista():
    query = Task.query.options(joinedload('project'))
    lista = Task.query.all()
    return render_template("projetos/tarefas/lista.html"
    , lista=lista
    )