from app import db

class Project(db.Model):
    project_status = {1:"Iniciado", 2: "Parado", 3:"Pausado", 4:"Concluído" }
    id = db.Column(db.Integer, primary_key=True)
    project_name = db.Column(db.String(80), nullable=False)
    manager = db.Column(db.String(80), nullable=False)
    manager_email = db.Column(db.String(120), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    finish_date = db.Column(db.DateTime)
    status = db.Column(db.Integer, nullable=False)
    tasks = db.relationship('Task', backref='project', lazy=True)


    def __repr__(self):
        return f'''<Project {self.project_name}>'''

class Task(db.Model):
    task_status = {1:"Urgente|Importante", 2: "Urgente|Não Importante", 3:"Não Urgene|Importante" }
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(80), nullable=False)
    status = db.Column(db.Integer, nullable=False)
    concluido = db.Column(db.Boolean)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'),
        nullable=False)

    times = db.relationship('TaskTime', backref='task', lazy=True)
    
    def __repr__(self):
        return f'''<Task {self.task_name} - Project {self.project_id}>'''


class TaskTime(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime)
    task_id = db.Column(db.Integer, db.ForeignKey('task.id'),
        nullable=False)
    
    def __repr__(self):
        return f'''<{self.start_time} - {self.end_time} - Task {self.task_name} - Project {self.project_name}>'''