from toshl_manager.commands import ShowLoans, ShowRoomieExpenses
from cleo import Application

application = Application()
# TODO: Add commands should be dinamic
application.add(ShowLoans())
application.add(ShowRoomieExpenses())

if __name__ == '__main__':
    application.run()
