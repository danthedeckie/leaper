#!/usr/bin/python

from time import sleep

from tkwindow import do_gui
from mouse import mouseinfo
import leapmouse


def main():
    ''' main entry point '''
    do_gui(mouseinfo)

    leapthread = leapmouse.do_init()

    leapthread.join()

if __name__ == '__main__':
    main()
