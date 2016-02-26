import threading
import time

story = ['a', 'b', 'c', 'd', 'e']

def tell_story(count):

    time.sleep(5)
    print(story[count])

    if not count + 1 == len(story):
        threading._start_new_thread(tell_story, (count + 1,))

while True:

    a = input()
    if a == 'start':
        threading._start_new_thread(tell_story, (0,))
