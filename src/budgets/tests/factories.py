from factory import Factory, Faker, Iterator, LazyAttributeSequence
from src.budgets.value_objects import Budget, BudgetFrequency

class BudgetFactory(Factory):
    class Meta:
        model = Budget

    id = LazyAttributeSequence(lambda _obj, number: number)
    name = Faker('name')
    limit = Faker('pyfloat', min_value=2_000, right_digits=2)
    amount = Faker('pyfloat', max_value=1_000, right_digits=2)
    planned = Faker('pyfloat', max_value=1_000, right_digits=2)
    date_from = Faker('date_between', start_date='-15d')
    date_to = Faker('future_date', end_date='+15d')
    rollover = False
    rollover_amount = 0
    frequency = Iterator(BudgetFrequency)
    categories = []
