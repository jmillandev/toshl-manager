from cleo import Application

from toshl_manager.commands import (
    CleanLoans,
    CleanRoomieExpenses,
    ShowBugets,
    ShowLoans,
    ShowRoomieExpenses,
    TelegramBot
)

application = Application()
# TODO: Add commands should be dinamic
application.add(ShowLoans())
application.add(CleanLoans())
application.add(ShowRoomieExpenses())
application.add(CleanRoomieExpenses())
application.add(ShowBugets())
application.add(TelegramBot())

if __name__ == "__main__":
    application.run()
