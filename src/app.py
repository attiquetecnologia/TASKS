import os
import click
from flask.cli import with_appcontext
from flask import (Flask, render_template)
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev'
        ,SQLALCHEMY_DATABASE_URI=f"sqlite:///{app.root_path}/databases/tarefas.db" #"sqlite:///"+os.path.join("databases", "test.db")
        ,SQLALCHEMY_TRACK_MODIFICATIONS=True
        ,ENV="production"
        ,DEBUG=True
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    
    db.init_app(app)
    app.cli.add_command(init_db_command)

    @app.route("/")
    @app.route("/index")
    def index():
        return render_template("index.html")
    
    # blueprint
    from projetos import view, vw_tasks, vw_time, vw_report
    app.register_blueprint(view.bp)
    app.register_blueprint(vw_tasks.bp)
    app.register_blueprint(vw_time.bp)
    app.register_blueprint(vw_report.bp)

    return app

def init_db():
    db.drop_all()
    db.create_all()
    # db.reflect()


@click.command("init-db")
@with_appcontext
def init_db_command():
    """Clear existing data and create new tables."""
    
    init_db()
    click.echo("Initialized the database.")
   
if __name__ == "__main__":
    create_app().run()