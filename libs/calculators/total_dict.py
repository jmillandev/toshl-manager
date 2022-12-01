from collections import defaultdict


class TotalDictCalculator:

    def __init__(self, data: list[dict]) -> None:
        if len(data) == 0:
            raise Exception("{self.__class__}.data needs at least one item")

        self.__number_fields = None
        self.data = data
        self._total = defaultdict(lambda: 0)

    def calculate(self) -> dict:
        """
        Returns:
            dict: A hash with the sum of the number data item's fields and
                '---' in other fields
        """
        if len(self._total) == 0:
            self._set_number_fields()
            self._set_not_number_fields()

        return dict(self._total)

    def _set_number_fields(self) -> None:
        for item in self.data:
            for key in self._number_fields:
                self._total[key] += item[key]

    def _set_not_number_fields(self) -> None:
        for key in self.data[0]:
            if key in self._number_fields:
                continue
            self._total[key] = "---"

    @property
    def _number_fields(self):
        if not self.__number_fields:
            item = self.data[0]
            self.__number_fields = set(
                {key for key in item if isinstance(item[key], int | float)})
        return self.__number_fields
