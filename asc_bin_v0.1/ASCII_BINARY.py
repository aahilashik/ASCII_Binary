
while True:
    #Input from the User
    input_str = input("To Close the Program, Enter Quit \nEnter the ASCII Value : ")
    
    #To Quit the Program
    if ((input_str == "Quit")or(input_str == "quit")):
        break
    
    #Convert into Binary and Split into List
    binary = ' '.join(format(ord(q), 'b') for q in input_str)
    binary = binary.split()

    #Initialize the Required Elements
    individual_asc = []
    individual_bin = []
    asc_count = []
    bin_count = []
    
    #Total Number of Characters in Input
    N = len(input_str)
    
    #Search for Individual Elements for both ASCII and Binary
    for i in range(N):
        if not input_str[i] in individual_asc:
            individual_asc.append(input_str[i])
            individual_bin.append(binary[i])
            
    #Sort the Individual Elements for both ASCII and Binary
    individual_asc.sort()
    individual_bin.sort()
    
    #Total Number of Individual Characters
    n = len(individual_asc)
    
    #Count the Number of Occurences and Print the Details
    print("Summary : \n")
    for i in range(n):
        asc_count.append(input_str.count(individual_asc[i])) 
        bin_count.append(binary.count(individual_bin[i]))
        print("Binary : " + individual_bin[i] + "  Character : " + individual_asc[i] + "  ASCII : " + str(ord(individual_asc[i])) + "  Count : " + str(bin_count[i]))
    print("\n")
        
    
