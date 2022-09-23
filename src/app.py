import os
from flask import (Flask, render_template)
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev'
        ,SQLALCHEMY_DATABASE_URI="sqlite:///"+os.path.join("databases", "test.db")
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
    # db.create_all()

    @app.route("/")
    @app.route("/index")
    def index():
        return render_template("index.html")
    
    # blueprint
    from projetos import view, vw_tasks
    app.register_blueprint(view.bp)
    app.register_blueprint(vw_tasks.bp)

    return app

if __name__ == "__main__":
    create_app().run()