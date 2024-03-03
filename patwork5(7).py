       
def frequent_character(input_string):
    char_count={}
    
    for char in input_string :
        if char.isalpha(): #to consider only alphabetic characters
            char_count[char]=char_count.get(char , 0) + 1
            
    if not char_count:
                return None
            
    most_frequent_char=max(char_count, key=char_count.get)
    return most_frequent_char



if __name__ == "__main__":
    user_input = input("enter the string:")
    result = frequent_character(user_input)
    
    if result:
        print("Most frequent character:",result)
    else:
        print("No alphabetic character is found.")
