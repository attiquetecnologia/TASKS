from flask import (url_for, session, Blueprint, render_template, request)
from . models import Project
from datetime import datetime, timedelta

bp = Blueprint('report', __name__)

@bp.route("/reports", methods=("GET", ))
def index():
    return render_template("projetos/index.html")

@bp.route("/reports/lista", methods=("GET", ))
def lista():
    lista = Project.query.all()
    def calc_time(tasks):
        tempo = timedelta(days=0, seconds=0)
        for t in tasks:
            task_tempo = timedelta(days=0, seconds=0)
            for l in t.times:
                task_tempo = task_tempo+(l.end_time-l.start_time)
                tempo = tempo+(l.end_time-l.start_time)
            tasks[tasks.index(t)].total = task_tempo

        media = tempo/len(tasks) # somatorio/total elementos
        return (tempo, media)

    for l in lista:
        calculo = calc_time(l.tasks)
        lista[lista.index(l)].total = calculo[0]
        lista[lista.index(l)].media = calculo[1]

    return render_template("reports/lista.html", lista=lista)