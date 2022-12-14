from flask import (url_for, session, Blueprint, render_template, request)
from sqlalchemy.orm import joinedload
from . models import Project, Task, TaskTime
from app import db

from datetime import datetime, timedelta

bp = Blueprint('task', __name__)

@bp.route("/task", methods=("GET", ))
def index():
    
    return render_template("projetos/tarefas/index.html")


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
    try:
        if request.form.get("id"):
            record = Task.query.filter_by(id=request.form.get("id")).first()
            # data['id'] = request.form.get("id")
            # task = Task(**data)
            record.task_name = request.form.get("task_name")
            record.project_id = request.form.get("project_id")
            record.nivel = request.form.get("nivel")
            record.concluido = request.form.get("concluido")=="on" or False
        else:
            task = Task(**{
                "task_name": request.form.get("task_name")
                ,"project_id": request.form.get("project_id")
                ,"nivel": request.form.get("nivel")
                ,"concluido": request.form.get("concluido")=="on" or False
                })
            db.session.add(task)
        db.session.commit()
        return f"""<p class="alert alert-success">Dados inseridos com sucesso!<p>"""
    except Exception as ex:
        return f"""<p class="alert alert-danger">Problemas!{ex}<p>"""

@bp.route("/tasks/lista", methods=("GET", ))
def lista():
    open_task = TaskTime.query.filter_by(end_time=None).first()
    query = Task.query.options(joinedload('project'))
    lista = Task.query.all()
    
    def calc_time(line):
        tempo = timedelta(days=0, seconds=0, microseconds=0)
        for l in line.times:
            tempo = tempo+(l.end_time-l.start_time)
        return tempo

    for l in lista:
        lista[lista.index(l)].total = calc_time(l)

    return render_template("projetos/tarefas/lista.html"
    , lista=lista, open_task=open_task
    )