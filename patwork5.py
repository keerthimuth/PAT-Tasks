
def count_vowels(string): #converting the string into lowercase for case insensitive
        string =string.lower()
    
        total_vowel=0  #initializing counts for each vowels
        count_a=0
        count_e=0
        count_i=0
        count_o=0
        count_u=0
    
        for char in string: #iterating each character in the string
             if char in 'aeiou': #to check if the char is vowel or not
                    total_vowel += 1 #incremeting total count
        
                    if char == 'a': #incrementing individual count
                     count_a += 1
                    elif char =='e':
                     count_e += 1
                    elif char =='i':
                     count_i += 1
                    elif char =='o':
                     count_o += 1
                    elif char =='u':
                     count_u += 1
            
        print("Total vowels in the string are:",total_vowel) #printing the output
        print("Individual count :")
        print("A:",count_a)
        print("E:",count_e)
        print("I:",count_i)
        print("O:",count_o)
        print("U:",count_u)
            
          
          
input_string  = "Guvi Geeks Network Private Limited" #input string 
count_vowels(input_string) #calling the function with input string


