from PyTerminalColor.TerminalColor import TerminalColor

if __name__ == '__main__':
    # create obj with default values
    colorize = TerminalColor(fgcolor='YELLOW', style='UNDERLINE')

    # override default values
    colorize.cprint(' TerminalCOLOR ', use_default=False, fgcolor='YELLOW', bgcolor='RED', style='BOLD')

    # using default values
    colorize.cprint('Author: Dhrumil Mistry\n')

    # print help
    help(TerminalColor)