class EducationMaterials:
    def __init__(self, *args):
        self.materials = args or []

    def __len__(self):
        return len(self.materials)
