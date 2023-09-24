import collections


class AiInfoManager:
    PATH = 'all_ai_tool.csv'
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

    def free_or_paid_is_most_reviewed(self):
        result = collections.Counter()
        for review, cost in zip(self.data['Review'], self.data['Free/Paid/Other']):
            if review:
                result.update({
                        'Free': 1 if cost == 'Free' else 0,
                        'Paid': 1 if cost == 'Paid' else 0,
                })
        return result.most_common(1)[0][0]

    def usable_with_most_free_tools(self):
        result = collections.defaultdict(list)
        for tool_name, cost, usable in zip(
            self.data['AI Tool Name'],
            self.data['Free/Paid/Other'],
            self.data['Usable For']
        ):
            if cost == 'Free':
                usable = [u.strip(' ') for u in usable.split(' / ') if u.strip()]
                for u in usable:
                    result[u].append(tool_name)
        top_usable = sorted(list(result), key=lambda x: len(x[1]))[0]
        return top_usable

    def get_filtered_tools(self, cost: str = None, task: str = None, category: str = None):
        result_intersection = set(self.data['AI Tool Name'])

        if cost:
            result = set()
            for tool_name, cost_ in zip(
                    self.data['AI Tool Name'],
                    self.data['Free/Paid/Other'],
            ):
                if cost == cost_:
                    result |= {tool_name}
            result_intersection &= result

        if task:
            result = set()
            for tool_name, usable in zip(
                    self.data['AI Tool Name'],
                    self.data['Usable For'],
            ):
                usable = [u.strip(' ') for u in usable.split(' / ') if u.strip()]
                if task in usable:
                    result |= {tool_name}
            result_intersection &= result

        if category:
            result = set()
            for tool_name, major_category in zip(
                    self.data['AI Tool Name'],
                    self.data['Major Category'],
            ):
                if category == major_category:
                    result |= {tool_name}
            result_intersection &= result

        return result_intersection


ai = AiInfoManager()
ai.read_data()
print(ai.free_or_paid_is_most_reviewed())
print(ai.usable_with_most_free_tools())
print(ai.get_filtered_tools(cost='Free', task='experiments', category='other'))



