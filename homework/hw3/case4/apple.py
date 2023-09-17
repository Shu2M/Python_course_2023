class Apple:
    STAGES_OF_MATURATION = [
        'Цветение',
        'Зеленое',
        'Красное',
    ]
    num_instances = 0

    def __init__(
            self,
            stage_of_maturation: str = STAGES_OF_MATURATION[0],
    ):
        self.__class__.num_instances += 1
        self.index = self.__class__.num_instances
        self.stage_of_maturation = stage_of_maturation

    def __del__(self):
        self.__class__.num_instances -= 1

    def __repr__(self):
        return (f'{self.__class__.__name__ }('
                f'{self.index!r}, '
                f'{self.stage_of_maturation!r}'
                f')')

    def is_ripen(self) -> bool:
        return True if self.stage_of_maturation == self.__class__.STAGES_OF_MATURATION[-1] else False

    def mature(self):
        if not self.is_ripen():
            current_stage_index = self.__class__.STAGES_OF_MATURATION.index(self.stage_of_maturation)
            self.stage_of_maturation = self.__class__.STAGES_OF_MATURATION[current_stage_index + 1]
