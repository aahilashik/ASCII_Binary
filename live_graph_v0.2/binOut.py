import os, time
while True:
    try:
        w = open ('Words.txt')
        lineList = w.readlines()
        w.close()
        v = open ('Volts.txt')
        voltList = v.readlines()
        v.close()
    except:
        lineList = []
        voltList = []
        word = ""
        volt = ""
    
    if not (len(lineList) == 0):
        os.system("cls")
        word = lineList[-1]
        word = word.rstrip()
        binary = ''.join(format(ord(q), '08b') for q in word)
        try:
            volt = "".join(i for i in voltList[0] if i in ["0","1","2","3","4","5","6","7","8","9"])
        except:
            volt = "404"
        print("\n\nWord : " + word + "\n\nBinary : " + binary + "\n\nVolts : " + volt)
    else :
        os.system("cls")
        print("\n\nWord : " + " - - - - " + "\n\nBinary : " + " - - - - " + "\n\nVolts : " + " - - - - ")
        
    time.sleep(2)