class Apple:
    STAGES_OF_MATURATION = [
        'Цветение',
        'Зеленое',
        'Красное',
    ]
    apple_index = 0

    def __new__(cls, *args, **kwargs):
        cls.apple_index += 1
        return super().__new__(cls)

    def __init__(
            self,
            stage_of_maturation: str = STAGES_OF_MATURATION[0],
    ):
        self.index = self.__class__.apple_index
        self.stage_of_maturation = stage_of_maturation

    def __repr__(self):
        return (
            f'{self.__class__.__name__} {self.index}, стадия созревания: {self.stage_of_maturation}\n'
        )

    def is_ripen(self) -> bool:
        return True if self.stage_of_maturation == self.__class__.STAGES_OF_MATURATION[-1] else False

    def mature(self):
        if not self.is_ripen():
            current_stage_index = self.__class__.STAGES_OF_MATURATION.index(self.stage_of_maturation)
            self.stage_of_maturation = self.__class__.STAGES_OF_MATURATION[current_stage_index + 1]
