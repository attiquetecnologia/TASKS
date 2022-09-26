from datetime import datetime
from urllib import request
from flask import (url_for, session, Blueprint, render_template)
from sqlalchemy.orm import joinedload
from . models import Task, TaskTime
bp = Blueprint('time', __name__)


@bp.route("/times/form", methods=("POST", ))
def form():
    # return render_template("lista.html"
    # , lista=lista
    # )
    
    return f"""Mensagem"""

@bp.route("/times/lista/<int:task_id>", methods=("GET", ))
def lista(task_id=None):
    query = TaskTime.query.options(joinedload('time'))
    if task_id:
        lista = TaskTime.query.filter_by(task_id=task_id).all()
    else:
        lista = TaskTime.query.all()
    return render_template("projetos/tarefas/tempo/lista.html"
    , lista=lista
    )

@bp.route("/times/start/<int:task_id>", methods=("GET", ))
def start(task_id):
    from app import db
    try:
        task = Task.query.filter_by(id=task_id, concluido=True).first()
        if task: return f"""Tarefa {task.task_name} ({task.id}) já concluída!"""

        open_time = TaskTime.query.filter_by(end_time=None).first()
        if open_time: return f"""Tarefa {open_time.task} ({open_time.task_id}) está iniciada! Finalize-a primeiro!"""

        time = TaskTime(start_time=datetime.now(), task_id=task_id)
        db.session.add(time)
        db.session.commit()
        return f"""Tarefa {task_id} iniciada"""
    except Exception as ex:
        return f"""Problemas ao iniciar a tarefa {task_id} -> {ex}"""

@bp.route("/times/stop/<int:task_id>/<int:id>", methods=("GET", ))
def stop(task_id, id=None):
    from app import db
    try:
        time = TaskTime.query.filter_by(id=id,task_id=task_id, end_time=None).first()
        time.end_time=datetime.now()
        time.task_id=task_id

        db.session.add(time)
        db.session.commit()
        return f"""Tarefa {task_id} finalizada"""
    except Exception as ex:
        return f"""Problemas ao iniciar a tarefa {task_id} -> {ex}"""        

@bp.route("/times/restart/<int:task_id>", methods=("GET", ))
def restart(task_id):
    from app import db
    try:
        task = Task.query.filter_by(id=task_id, concluido=True).first()
        if not task: 
            return f"""Tarefa {task.task_name} ({task.id}) ainda está aberta!"""
        else:
            task.concluido=False

        db.session.add(task)
        db.session.commit()
        return f"""Tarefa {task_id} reiniciada"""
    except Exception as ex:
        return f"""Problemas ao reiniciar a tarefa {task_id} -> {ex}"""