class Project:
    def __init__(
        self,
        name,
        description,
        dependencies,
        dev_dependencies,
        license=None,
        authors=None,
    ):
        self.name = name
        self.description = description
        self.dependencies = dependencies or []
        self.dev_dependencies = dev_dependencies or []
        self.license = license
        self.authors = authors or []

    def __str__(self):
        lines = []
        lines.append(f"Name: {self.name}")
        lines.append(f"Description: {self.description}")
        if self.license:
            lines.append(f"License: {self.license}")
        lines.append("")

        if self.authors:
            lines.append("Authors:")
            for a in self.authors:
                lines.append(f"- {a}")
            lines.append("")

        lines.append("Dependencies:")
        if self.dependencies:
            for d in self.dependencies:
                lines.append(f"- {d}")
        else:
            lines.append("-")
        lines.append("")

        lines.append("Development dependencies:")
        if self.dev_dependencies:
            for d in self.dev_dependencies:
                lines.append(f"- {d}")
        else:
            lines.append("-")

        return "\n".join(lines)
