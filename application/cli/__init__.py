from cleo import Application


from .budgets import ListBugets
from .loans import ListLoans, CleanLoans
from .roomie_expenses import ListRoomieExpenses, CleanRoomieExpenses

if __name__ == "__main__":
    application = Application()
    
    # TODO: Add commands should be dinamic
    application.add(ListLoans())
    application.add(CleanLoans())
    application.add(ListRoomieExpenses())
    application.add(CleanRoomieExpenses())
    application.add(ListBugets())

    application.run()
