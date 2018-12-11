from configrations import commands
from m_parser import parse_command as p


def get_command():
    print(commands)
    user_command = input("enter your command")
    return p.parse(user_command)



def run(m_command):
    pass


def main():

    while 1:
        my_command = get_command()
        run(my_command)


if __name__ == '__main__':
    main()
