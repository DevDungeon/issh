import curses
import curses.ascii
from os import system, environ
from os.path import join, expanduser, exists
import sys
from signal import signal, SIGINT, SIGTERM


class ISSH:

    def __init__(self, screen):
        print ('[*] Initializing ISSH')
        signal(SIGINT, self.shutdown)
        signal(SIGTERM, self.shutdown)

        self.hosts = list()
        self.ssh_config_path = join(expanduser("~"), ".ssh", "config")
        self.check_if_ssh_config_exists()
        self.load_ssh_hosts()
        self.active_choice = 0

        self.screen = screen
        self.screen.keypad(1)
        curses.curs_set(0)
        curses.noecho()
        curses.start_color()
        curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)

    def check_if_ssh_config_exists(self):
        if not exists(self.ssh_config_path):
            curses.endwin()
            print('No SSH config file detected at ' + self.ssh_config_path + '. Aborting.')
            sys.exit(1)

    def load_ssh_hosts(self):
        self.hosts = list()
        with open(self.ssh_config_path) as ssh_config:
            for line in ssh_config.readlines():
                line = line.rstrip()
                if len(line) == 0 or line[0] == ' ' or line[0] == '\t' or line.lstrip()[0] == '#':
                    continue
                try:
                    self.hosts.append(line.split()[1])
                except IndexError:
                    print('[-] Warning: Invalid host format detected on line: %s' % line)

    def run(self):
        self.input_loop()

    def print_options(self):
        self.screen.clear()
        num_header_rows = 2
        self.screen.addstr(0, 0, "Select an SSH host (Press H for help):")

        for i, host in enumerate(self.hosts):
            if i == self.active_choice:
                self.screen.addstr(i + num_header_rows, 0, " > %s" % (host), curses.color_pair(1) | curses.A_BOLD)
            else:
                self.screen.addstr(i + num_header_rows, 0, "   %s" % (host))
        self.screen.refresh()

    def input_loop(self):
        while True:
            self.print_options()

            try:
                char_ord = self.screen.getch()
                char = chr(char_ord).upper()

                if char == 'Q' or char_ord == curses.ascii.ESC:  # Esc or Q
                    self.shutdown()
                elif char == 'J' or char_ord == curses.KEY_DOWN:  # Down or J
                    if self.active_choice < len(self.hosts) - 1:
                        self.active_choice += 1
                elif char == 'K' or char_ord == curses.KEY_UP:  # Up or K
                    if self.active_choice > 0:
                        self.active_choice -= 1
                elif char == 'E':
                    self.launch_editor()
                elif char == 'R':  # Refresh screen
                    self.load_ssh_hosts()
                elif char == 'H':  # Print help screen
                    self.print_help_screen()
                elif char_ord == curses.ascii.LF or char == 'L' or char_ord == curses.KEY_RIGHT:  # Enter, L or Right
                    # Choice has been selected already, exit the menu system
                    break
            except Exception as e:
                print('[-] Invalid keypress detected.')
                print(e)

        # After breaking out of loop, ssh to the active target
        self.cleanup_curses()
        system('ssh %s' % self.hosts[self.active_choice])

    def cleanup_curses(self):
        self.screen.keypad(0)
        curses.curs_set(1)
        curses.echo()
        curses.endwin()

    def shutdown(self):
        self.cleanup_curses()
        sys.exit(0)

    def launch_editor(self):
        editor = environ.get('EDITOR')
        if editor is None:  # Default editors
            if sys.platform == 'win32':
                editor = 'notepad.exe'
            elif sys.platform == 'darwin':
                editor = 'nano'
            elif 'linux' in sys.platform:
                editor = 'vi'
        system("%s %s" % (editor, self.ssh_config_path))
        self.load_ssh_hosts()  # Reload hosts after changes

    def print_help_screen(self):
        self.screen.clear()

        self.screen.addstr(0, 0, "Help information:")
        self.screen.addstr(2, 0, "  H - This help screen")
        self.screen.addstr(3, 0, "  Q or ESC - Quit the program")
        self.screen.addstr(4, 0, "  E - Edit SSH config file")
        self.screen.addstr(5, 0, "  R - Reload SSH hosts from config file")
        self.screen.addstr(6, 0, "  Down or J - Move selection down")
        self.screen.addstr(7, 0, "  Up or K - Move selection up")
        self.screen.addstr(8, 0, "  Right or L or Enter - SSH to current selection")
        self.screen.addstr(10, 0, "Press any key to continue")

        # Wait for any key press
        self.screen.getch()


def main_wrapper(main_screen):
    issh = ISSH(main_screen)
    issh.run()


def main():
    curses.wrapper(main_wrapper)


if __name__ == '__main__':
    main()
