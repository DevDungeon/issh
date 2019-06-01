import curses
from os import system
from os.path import join, expanduser, exists
import sys
from signal import signal, SIGINT, SIGTERM


class ISSH:


    def __init__(self):
        signal(SIGINT, self.shutdown)
        signal(SIGTERM, self.shutdown)

        self.ssh_config_path = join(expanduser("~"), ".ssh", "config")
        self.check_if_ssh_config_exists()
        self.load_ssh_hosts()
        self.active_choice = 0

        self.screen = curses.initscr()
        curses.curs_set(0)
        self.screen.keypad(1)
        curses.noecho()
        curses.start_color()
        curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)


    def check_if_ssh_config_exists(self):
        if not exists(self.ssh_config_path):
            print('No SSH config file detected. Aborting.')
            sys.exit(1)


    def load_ssh_hosts(self):
        self.hosts = []
        with open(self.ssh_config_path) as ssh_config:
            for line in ssh_config.readlines():
                line = line.rstrip()
                if len(line) == 0 or line[0] == ' ' or line[0] == '\t':
                    continue
                try:
                    self.hosts.append(line.split()[1])
                except IndexError:
                    print('[-] Warning: Invalid host format detected on line: %s' % line)

    def run(self):
        self.input_loop()


    def print_options(self):
        num_header_rows = 2
        self.screen.addstr(0, 0, "Select an SSH host:")

        for i, host in enumerate(self.hosts):
            if i == self.active_choice:
                self.screen.addstr(i + num_header_rows, 0, " > %s" % (host), curses.color_pair(1) | curses.A_BOLD)
            else:
                self.screen.addstr(i + num_header_rows, 0, "   %s" % (host))
        self.screen.refresh()


    def input_loop(self):
        while True:
            self.print_options()

            char_ord = self.screen.getch()
            char = chr(char_ord).upper()
            if char == 'Q' or char_ord == 27:  # Esc or Q
                self.shutdown()
            elif char == 'J' or char_ord == 258:  # Down or J
                if self.active_choice < len(self.hosts) - 1:
                    self.active_choice += 1
            elif char == 'K' or char_ord == 259:  # Up or K
                if self.active_choice > 0:
                    self.active_choice -= 1
            elif char_ord == 10 or char == 'L' or char_ord == 261:  # Enter key or L or Right
                break

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


if __name__ == '__main__':
    issh = ISSH()
    issh.run()
