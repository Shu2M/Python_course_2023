class Student:
    def __init__(self, knowledge: list = None):
        self.knowledge = knowledge or []

    def take(self, new_knowledge: str):
        self.knowledge.append(new_knowledge)
