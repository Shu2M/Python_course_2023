from human import Human
import random


class Student(Human):
    def __init__(
            self,
            knowledge: list = None,
            *args,
            **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.knowledge = knowledge or []

    def __len__(self):
        return len(self.knowledge)

    def take(self, new_knowledge: str):
        self.knowledge.append(new_knowledge)

    def forget_knowledge(self):
        if self.knowledge:
            index = random.randrange(len(self))
            self.knowledge.pop(index)
