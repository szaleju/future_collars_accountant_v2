import sys
from lib.accountant import Command, Account, Warehouse
from lib.accountant import updateAccountAndWarehouse

command = Command()
account = Account()
warehouse = Warehouse()

command.readFromFile()
command.commandsFromSingleActions()

# sys.argv = [saldo.py, in.txt, howMuch, comment]
command.listOfCommands.insert(-1, ['saldo', int(sys.argv[2]), sys.argv[3]])

updateAccountAndWarehouse(command, account, warehouse)
command.printSingleCommandsLikeInputFile()