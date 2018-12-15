from m_parser import parse_command as p
import command_handler
import configrations


def get_command():
    user_command = input("enter your command")
    return p.parse(user_command)


def run(m_command):
    print("in run")

    command_handler.run_command(m_command)
    pass


def main():
    print("in main")
    while 1:
        print(configrations.commands)
        my_command = get_command()
        run(my_command)


if __name__ == '__main__':
    main()
