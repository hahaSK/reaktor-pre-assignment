class PackageCls:

    def __init__(self, name, description) -> None:
        self.Name = name
        self.Description = description
        self.DependsList = list()
        self.ReverseDependencies = list()
        super().__init__()
