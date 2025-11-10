from urllib import request
import tomli
from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        content = request.urlopen(self._url).read().decode("utf-8")
        data = tomli.loads(content)

        tool = data.get("tool", {})
        poetry = tool.get("poetry", {})

        name = poetry.get("name", "")
        description = poetry.get("description", "-")
        license_ = poetry.get("license")

        raw_authors = poetry.get("authors", []) or []
        authors = []
        for a in raw_authors:
            if isinstance(a, dict):
                authors.append((a.get("name") or "").strip())
            else:
                authors.append(str(a).strip())

        deps_map = poetry.get("dependencies", {}) or {}
        dependencies = list(deps_map.keys())

        group = poetry.get("group", {}) or {}
        dev = group.get("dev", {}) if isinstance(group, dict) else {}
        dev_deps_map = dev.get("dependencies", {}) if isinstance(dev, dict) else {}
        dev_dependencies = list(dev_deps_map.keys())

        return Project(
            name=name,
            description=description,
            dependencies=dependencies,
            dev_dependencies=dev_dependencies,
            license=license_,
            authors=authors,
        )
