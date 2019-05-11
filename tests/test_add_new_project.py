from models.project import Project

def test_add_new_project(app):
    app.session.login("administrator", "root")
    project = Project(name="Test32w2ewwe")
    app.project.creation(project)
    l = app.project.get_project_list()
    print(l)