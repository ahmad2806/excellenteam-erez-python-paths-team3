from m_parser import parse_command as p
import command_handler
import configrations
import sys


def get_command():
    user_command = input("enter your command\n")
    return p.parse(user_command)


def run(m_command):
    command_handler.run_command(m_command)
    pass


def main():
    configrations.file_path = sys.argv[1]
    configrations.image_path = sys.argv[2]

    while 1:
        print(configrations.commands)
        my_command = get_command()
        if my_command == 4:
            break

        run(my_command)


if __name__ == '__main__':
    main()
