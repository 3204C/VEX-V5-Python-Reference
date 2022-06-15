from __future__ import print_function
import builtins as __builtin__
import os
import sys

CompetitionState = input('Please enter the competition state. Please enter either "driver_control" or "autonomous":')

class Competition():
    def __init__(self, driver_control, autonomous):
        if CompetitionState == "driver_control":
            driver_control()
        elif CompetitionState == "autonomous":
            autonomous()
        else:
            print("Unknown Competition State")
            sys.exit(1)

class FontType():
    @staticmethod
    def MONO12():
        pass

    @staticmethod
    def MONO15():
        pass

    @staticmethod
    def MONO20():
        pass

    @staticmethod
    def MONO30():
        pass

    @staticmethod
    def MONO40():
        pass

    @staticmethod
    def MONO60():
        pass

    @staticmethod
    def PROP20():
        pass

    @staticmethod
    def PROP30():
        pass

    @staticmethod
    def PROP40():
        pass

    @staticmethod
    def PROP60():
        pass

class Color():
    @staticmethod
    def BLACK():
        pass

    @staticmethod
    def WHITE():
        pass

    @staticmethod
    def RED():
        pass

    @staticmethod
    def GREEN():
        pass

    @staticmethod
    def BLUE():
        pass

    @staticmethod
    def YELLOW():
        pass

    @staticmethod
    def ORANGE():
        pass

    @staticmethod
    def PURPLE():
        pass

    @staticmethod
    def CYAN():
        pass

    @staticmethod
    def TRANSPARENT():
        pass

class brain():
    class screen():
        @staticmethod
        def print(text):
            print(text)

        @staticmethod
        def set_cursor(ROW, COLUMN):
            pass

        @staticmethod
        def next_row():
            print("\n")

        @staticmethod
        def clear_screen():
            command = 'clear'
            if os.name in ('nt', 'dos'):
                command = 'cls'
            os.system(command)

        @staticmethod
        def clear_row(ROW=-1):
            pass

        @staticmethod
        def draw_pixel(X, Y):
            pass

        @staticmethod
        def draw_line(START_X, START_Y, END_X, END_Y):
            pass

        @staticmethod
        def draw_rectangle(X, Y, WIDTH, HEIGHT):
            pass

        @staticmethod
        def draw_circle(X, Y, RADIUS):
            pass

        @staticmethod
        def set_font(FONT_TYPE):
            pass

        @staticmethod
        def set_pen_width(PEN_WIDTH):
            pass

        @staticmethod
        def set_pen_color(COLOR):
            pass

        @staticmethod
        def set_fill_color(COLOR):
            pass

        @staticmethod
        def pressed(callback):
            callback()

        @staticmethod
        def released(callback):
            callback()

    class timer():
        @staticmethod
        def event(callback, time):
            callback()

def print(text):
    if text == r"\033[2J":
        command = 'clear'
        if os.name in ('nt', 'dos'):
            command = 'cls'
        os.system(command)
    __builtin__.print(text)


brain.screen.print("Hello World")
brain.screen.clear_screen()