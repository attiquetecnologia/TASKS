from urllib import request
from flask import (url_for, session, Blueprint, render_template)
from sqlalchemy.orm import joinedload
from . models import Project, TaskTime
bp = Blueprint('time', __name__)


@bp.route("/times/form", methods=("POST", ))
def form():
    # return render_template("lista.html"
    # , lista=lista
    # )
    
    return f"""Mensagem"""

@bp.route("/times/lista", methods=("GET", ))
def lista():
    query = TaskTime.query.options(joinedload('time'))
    lista = TaskTime.query.all()
    return render_template("projetos/tarefas/tempo/lista.html"
    , lista=lista
    )