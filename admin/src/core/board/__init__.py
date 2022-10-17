from src.core.board.issue import Issue
from src.core.database import db

def list_issues():
    return Issue.query.all() #obtengo la lista de issues

def create_issue(**kwargs): #obtengo todos los valores 
    issue = Issue(**kwargs)
    db.session.add(issue)
    db.session.commit()