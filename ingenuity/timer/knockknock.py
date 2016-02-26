import time
import threading

def interrupt(s):
    time.sleep(s)
    print('Moo !!!!!')
    threading._start_new_thread(interrupt, (s,))

def main():

    print('knock knock')
    a = input('')
    print('Interrupting cow.')
    threading._start_new_thread(interrupt, (3,))
    b = input('')

if __name__ == '__main__':
    main()


