import controller


def run_command(m_command):
    print("in run command")
    if m_command == 1:
        controller.create_filters()
    elif m_command == 2:
        print("in command 2")
        controller.display_filters()
    elif m_command == 3:
        controller.change_filter()
    elif m_command == 4:
        controller.set_mode()
