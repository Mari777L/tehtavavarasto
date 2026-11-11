import tomli
from urllib import request
from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        project_data = tomli.loads(content)
        project = project_data["project"]


        name = project["name"]
        description = project["description"]
        license = project["license"]

        authors = [
            author["name"]
            for author in project.get("authors", [])
        ]

        dependencies = project["dependencies"]
        dev_dependencies = project_data["dependency-groups"]["dev"]

        return Project(
        name,
        description,
        license,
        authors,
        dependencies,
        dev_dependencies
        )

        # deserialisoi TOML-formaatissa oleva merkkijono
        # ja muodosta Project-olio sen tietojen perusteella
        #return Project("Test name", "Test description", [], [])
