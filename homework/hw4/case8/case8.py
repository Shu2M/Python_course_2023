import collections
import datetime


class UfoInfoManager:
    PATH = 'nlo.csv'
    DELIMITER = ','

    def __init__(self, path: str = None):
        self.path = path or self.__class__.PATH
        self.data = collections.defaultdict(list)

    def read_data(self) -> None:
        with open(self.path, 'r') as ufo_data:
            keys = ufo_data.readline().strip().split(self.__class__.DELIMITER)
            for data_line in ufo_data.readlines():
                values = data_line.strip().split(self.__class__.DELIMITER)
                for key, value in zip(keys, values):
                    self.data[key].append(value)

    def get_country_with_most_observations(self) -> str:
        return collections.Counter(self.data['country']).most_common(1)[0][0]

    def get_most_often_ufo_month(self) -> str:
        months = list()
        for date_string in self.data['datetime']:
            date_string = date_string.split()[0]
            date_obj = datetime.datetime.strptime(date_string, '%m/%d/%Y')
            months.append(date_obj.strftime("%B"))
        return collections.Counter(months).most_common(1)[0][0]


ufo = UfoInfoManager()
ufo.read_data()
most_ufo_country = ufo.get_country_with_most_observations()
most_month = ufo.get_most_often_ufo_month()
print(most_ufo_country)
print(most_month)

