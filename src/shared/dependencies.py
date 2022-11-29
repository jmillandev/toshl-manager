from dependency_injector.providers import Singleton
from dependency_injector.containers import DeclarativeContainer
from libs.tosh_finances.buggets.repository import BuggetToshlRepository


class Container(DeclarativeContainer):

    budget_repository = Singleton(BuggetToshlRepository)
