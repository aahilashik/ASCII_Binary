from pynput import keyboard
import os

find = ""

def on_press(key):
    global find
    try:
        find += (key.char)
        print(key.char, end = "")

    except AttributeError:
        if ((key == keyboard.Key.space)):
            find += " "
        if ((key == keyboard.Key.enter)):
            f=open("Words.txt","a+")
            f.write(find + "\n")
            print("\nMessange Sent : " + find)
            find = ""
            f.close()
        
def on_release(key):
    #print('{0} released'.format(key))
    if key == keyboard.Key.esc:
        print("\nTerminated")
        try:
            os.remove("Words.txt")
        except:
            pass
        return False

# Collect events until released
try:
    os.remove("Words.txt")
except:
    pass
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()