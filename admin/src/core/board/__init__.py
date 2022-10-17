from src.core.board.issue import Issue
from src.core.database import db
from src.core.board.labels import Label

def list_issues():
    return Issue.query.all() #obtengo la lista de issues

def create_issue(**kwargs): #obtengo todos los valores 
    issue = Issue(**kwargs)
    db.session.add(issue)
    db.session.commit()

    return issue

#a un issue le asigno un nuevo usuario
def assign_user(issue, user):
    issue.user = user
    db.session.add(issue)
    db.session.commit()

    return issue

def assign_labels(issue, labels):
    issue.labels.extend(labels)
    db.session.add(issue)
    db.session.commit()

    return issue

def create_label(**kwargs):
    label = Label(**kwargs)
    db.session.add(label)
    db.session.commit()

    return label