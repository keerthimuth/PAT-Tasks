def print_pyramid(n): #function to print pyramid of numbers
    for i in range(1, n + 1): #to print leading space
        for j in range(n - i):
         print(" ", end=" ")
        for k in range(1, i + 1): #to print ascending order
            print(k, end=" ")
        for l in range(i -1, 0 , -1): #to print descending order
            print(l, end=" ")
            
        print() #move to the next line for the next row
    
num = 20 #set the desired number of rows for the pyramid
print_pyramid(num) #call the function to print the pyramid

