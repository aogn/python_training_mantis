from models.project import Project
from random import randrange

def test_delete_project(app):
    app.session.login("administrator", "root")
    if len(app.project.get_project_list()) == 0:
        app.project.creation(Project(name="New_for_delete"))
    old_projects = app.project.get_project_list()
    project = old_projects[0]
    app.project.delete_first_project()
    new_projects = app.project.get_project_list()
    old_projects.remove(project)
    new_projects == old_projects
