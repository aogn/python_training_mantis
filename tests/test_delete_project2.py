from models.project import Project

def test_delete_project(app):
    app.session.login("administrator", "root")
    if len(app.project.get_project_list()) == 0:
        app.project.creation(Project(name="New_for_delete"))
    old_projects = app.soap.project_list("administrator", "root")
    project = old_projects[0]
    app.project.delete_first_project()
    new_projects = app.soap.project_list("administrator", "root")
    old_projects.remove(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)