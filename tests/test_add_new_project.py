from models.project import Project
import string
import random

def random_projectname(prefix, maxlen):
    symbols = string.ascii_letters
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def test_add_new_project(app):
    app.session.login("administrator", "root")
    old_projects = app.project.get_project_list()
    project = Project(name=random_projectname("project_", 10))
    app.project.creation(project)
    new_projects = app.project.get_project_list()
    old_projects.append(project)
    old_projects == new_projects