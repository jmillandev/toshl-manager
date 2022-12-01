from collections import defaultdict


class TotalDictCalculator:

    def __init__(self, data: list[dict]) -> None:
        if len(data) == 0:
            raise Exception("{self.__class__}.data needs at least one item")

        self.__number_fields = None
        self.data = data
        self.total = defaultdict(lambda: 0)

    def calculate(self)-> dict:
        """
        Returns:
            dict: A hash with the sum of the number data item's fields and
                '---' in other fields
        """
        for item in self.data[:-1]:
            for key in self._number_fields:
                self.total[key] += item[key]
        
        for key in self.data[-1]:
            if key in self._number_fields:
                self.total[key] += item[key]
                continue

            self.total[key] = "---"

    @property
    def _number_fields(self):
        if not self.__number_fields:
            item = self.data[0]
            self.__number_fields = (key for key in item if isinstance(item[key], int | float))
        return self.__number_fields
