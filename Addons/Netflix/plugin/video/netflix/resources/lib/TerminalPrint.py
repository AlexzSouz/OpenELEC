# Authors: [Alex.H, JackSparrow]
# https://stackoverflow.com/users/1084917/jacksparrow
# https://stackoverflow.com/questions/287871/print-in-terminal-with-colors-using-python/34443116#34443116

class Terminal:
    def PrintRed(prt): print("\033[91m {}\033[00m".format(prt))
    def PrintGreen(prt): print("\033[92m {}\033[00m".format(prt))
    def PrintYellow(prt): print("\033[93m {}\033[00m".format(prt))
    def PrintLightPurple(prt): print("\033[94m {}\033[00m".format(prt))
    def PrintPurple(prt): print("\033[95m {}\033[00m".format(prt))
    def PrintCyan(prt): print("\033[96m {}\033[00m".format(prt))
    def PrintLightGray(prt): print("\033[97m {}\033[00m".format(prt))
    def PrintBlack(prt): print("\033[98m {}\033[00m".format(prt))