import os, time

prev = ""

while True:
    #Input from the User
    #input_str = input("To Close the Program, Enter Quit \nEnter the ASCII Value : ")
    
    #To Quit the Program
    #if ((input_str == "Quit")or(input_str == "quit")):
    #    break
    
    if os.path.isfile("Words.txt"):
        f = open ('Words.txt',"r")
        lineList = f.readlines()
        f.close()
    else:
        lineList = []
        input_str = ""
    if not (len(lineList) == 0):
        input_str = lineList[-1]
        
    
    if not len(lineList)==0:
        #Clear the Screen for Every Change in Message
        os.system("cls")
        
        #Initialize the Required Elements
        individual_asc = []
        individual_bin = []
        asc_count = []
        
        
        word = []
        [[word.append(w) for w in e.split()] for e in lineList]
        
        #Total Number of Characters in Input
        N = len(word)
        
        #Search for Individual Elements for both ASCII and Binary
        for i in range(N):
            if not word[i] in individual_asc:
                individual_asc.append(word[i])
                binary = ''.join(format(ord(q), '08b') for q in word[i])
                individual_bin.append(binary)
                
        #Sort the Individual Elements for both ASCII and Binary
        individual_asc.sort()
        individual_bin.sort()
        
        #Total Number of Individual Characters
        n = len(individual_asc)
        
        #Count the Number of Occurences and Print the Details
        print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n")
        print("Summary : \n")
        for i in range(n):
            asc_count.append(word.count(individual_asc[i]))
            print("Word : " + individual_asc[i] + "      Count : " + str(asc_count[i]) + "     Binary : " + individual_bin[i])
        print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_\n")
    else:
        os.system("cls")
        print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n")
        print("Summary : \n")
        print("Word : " + " - - - - " + "      Count : " + " - - - - " + "     Binary : " + " - - - - ")
        print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_\n")
    time.sleep(2)

            