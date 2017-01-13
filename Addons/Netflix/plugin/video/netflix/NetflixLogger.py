from enum import Enum
from resources.lib.TerminalPrint import Terminal

class NetflixLogger:
    def __init__(self):
        self.Type = LoggerType.Verbose
        
    def Verbose(self, message):
        Terminal.PrintLightGray(str(LoggerType.Verbose) + ":" + message)

    def Warning(self, message):
        Terminal.PrintYellow(str(LoggerType.Warning) + ":" + message)

    def Error(self, message):
        Terminal.PrintRed(str(LoggerType.Error) + ":" + message)

class LoggerType(Enum):
    Verbose = 1
    Warning = 2
    Error = 3