from labyrinth import make
from player import new
import commands
import sys

size = input('\nWelcome, starting a new game. Please enter labyrinth size (4-10):')
size = int(size)

if (size <4) | (size >10):
    print('Invalid labyrinth size. Game Terminated')
    exit()

print('\nGame started! Labyrinth of size', size, 'is generated. Play with either of the following commands - "go-up", "go-down", "go-left", "go-right", "skip" or "show"')
lib, x, y = make(size)
plyr = new(int(x), int(y))

command_manager = commands.CommandManager()
finished = False
message = ""
args = []
cmd = None
try:
    while not finished:
        user_input = input("$> ")

        cmd, args, message = command_manager.parse_user_input(user_input)
        if cmd == None:
            print(message)
            continue
        (finished, message) = commands.CommandManager.eval_command(cmd, args, lib, plyr)
        if message != "": print(message)
    print("End of Game !")
except:
    print("Unexpected error:", sys.exc_info()[0])
