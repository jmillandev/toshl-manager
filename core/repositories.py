from .budgets.repositories import BudgetRepositoryInterface
from .categories.repositories import CategoryRepositoryInterface
from .entries.repositories import EntryRepositoryInterface
from .tags.repositories import TagRepositoryInterface


class RepositoryInterface:

    def entries(self) -> EntryRepositoryInterface:
        raise NotImplementedError

    def budgets(self) -> BudgetRepositoryInterface:
        raise NotImplementedError

    def categories(self) -> CategoryRepositoryInterface:
        raise NotImplementedError
    
    def tags(self) -> TagRepositoryInterface:
        raise NotImplementedError
