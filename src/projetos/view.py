from flask import (url_for, session, Blueprint, render_template, request)
from . models import Project
from datetime import datetime, timedelta

bp = Blueprint('project', __name__)

@bp.route("/projects", methods=("GET", ))
def index():
    return render_template("projetos/index.html")

@bp.route("/projects/add", methods=("GET", ))
def add():
    return render_template("projetos/form.html")

@bp.route("/projects/edit/<int:id>", methods=("GET", ))
def edit(id):
    record = Project.query.filter_by(id=id).first()
    
    return render_template("projetos/form.html", record=record)


@bp.route("/projects/form", methods=("POST", ))
def form():
    from app import db
    try:
        if request.form.get("id"):
            record = Project.query.filter_by(id=request.form.get("id")).first()
            # data['id'] = request.form.get("id")
            # task = Project(**data)
            record.project_name = request.form.get("project_name")
            record.manager = request.form.get("manager")
            record.manager_email = request.form.get("manager_email")
            record.status = request.form.get("status")
            record.start_date = request.form.get("start_date")
            record.end_date = request.form.get("end_date")
        else:
            task = Project(**{
                "project_name": request.form.get("project_name")
                ,"manager": request.form.get("manager")
                ,"manager_email": request.form.get("manager_email")
                ,"status": request.form.get("status")
                ,"start_date": request.form.get("start_date")
                ,"end_date": request.form.get("end_date")
                })
            db.session.add(task)
        db.session.commit()
        return f"""<p class="alert alert-success">Dados inseridos com sucesso!<p>"""
    except Exception as ex:
        return f"""<p class="alert alert-danger">Problemas!{ex}<p>"""


@bp.route("/projects/lista", methods=("GET", ))
def lista():
    lista = Project.query.all()
    def calc_time(tasks):
        tempo = timedelta(days=0, seconds=0, microseconds=0)
        for t in tasks:
            for l in t.times:
                tempo = tempo+(l.end_time-l.start_time)
        return tempo

    for l in lista:
        lista[lista.index(l)].total = calc_time(l.tasks)

    return render_template("projetos/lista.html", lista=lista)