import display.display_defualt as display_defualt
import display.display_steps as display_steps


def use_display(pathes, mode=1):
    print("in display handler")

    if mode == 1:
        display_defualt.DisplayDefualt().display()
    else:
        display_steps.DisplaySteps()
