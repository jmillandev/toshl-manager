from toshl_manager.commands import ShowLoans, ShowRoomieExpenses, ShowBugets, CleanLoans
from cleo import Application

application = Application()
# TODO: Add commands should be dinamic
application.add(ShowLoans())
application.add(CleanLoans())
application.add(ShowRoomieExpenses())
application.add(ShowBugets())

if __name__ == '__main__':
    application.run()
