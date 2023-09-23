import re


class FileSearcher:
    def __init__(self, path: str):
        self.path = path
        self.file_lines = list()

    def read_file(self) -> None:
        with open(self.path) as file:
            self.file_lines = file.readlines()

    def search_for(self, pattern: str) -> list[str]:
        coincidences = list()
        for line in self.file_lines:
            coincidence = re.findall(pattern, line)
            if coincidence:
                coincidences.extend(coincidence)
        return coincidences


fs = FileSearcher('test.csv')
fs.read_file()
res = fs.search_for('sen')
print(res)
