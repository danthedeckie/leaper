#!./.virtualenv/bin/python

from time import sleep

from tkwindow import do_gui
import leapmouse


def main():
    ''' main entry point '''
    do_gui()

    leapthread = leapmouse.do_init()

    leapthread.join()

if __name__ == '__main__':
    main()
