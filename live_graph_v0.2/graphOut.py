import random    
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import os, time

#           %matplotlib qt

# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
Fs = 24
f1 = 6
xs = [x for x in range(121)]
ys = [2.5*np.sin(1.0 * np.pi * f1 * x / Fs) + 2.5 for x in range(121)]
prev = ""
word = ""

def animate(i, xs, ys):
    global prev, word
    if os.path.isfile("Words.txt"):
        f = open ('Words.txt',"r")
        lineList = f.readlines()
        f.close()
    else:
        lineList = []
        word = ""
    if not (len(lineList) == 0):
        word = lineList[-1]
        word = word.rstrip()
        
    if (word == "") or (word == "\n"):
        temp = ys[0]
        for x in range(120):
            ys[x] = ys[x+1]
        ys[119] = temp
        xs = xs[:120]
        ys = ys[:120]
        ax.clear()
        ax.plot(xs, ys)
        # Format plot
        plt.xticks(rotation=45, ha='right')
        plt.subplots_adjust(bottom=0.30)
        plt.title('Input - ASCII : Output - Waiting... ')
        plt.ylabel('Voltage (Volts)')
         
    if not word == prev:
        try:
            os.remove("Volts.txt")
        except:
            pass
        prev = word
        binary = ''.join(format(ord(q), '08b') for q in word)
        print("Word : " + word + "  Binary : " + binary)
        # Add x and y to lists
        for i in range(len(binary)):
            xs.append(i)
            ys.append(random.choice([0, 1, 2, 3, 4, 5]))

        xs = xs[-(len(binary)):]
        ys = ys[-(len(binary)):]
        ax.clear()
        ax.plot(xs, ys)
            
        v = open ('Volts.txt',"a+")
        v.write(str(ys))
        v.close()
    
        # Format plot
        plt.xticks(rotation=45, ha='right')
        plt.subplots_adjust(bottom=0.30)
        plt.title('Input - ASCII : Output - Max 5V ')
        plt.ylabel('Voltage (Volts)')
    time.sleep(2)
    
ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=1000)
plt.show()