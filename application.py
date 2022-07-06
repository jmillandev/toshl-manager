from toshl_manager.commands import ExportLoans
from cleo import Application

application = Application()
application.add(ExportLoans())

if __name__ == '__main__':
    application.run()
