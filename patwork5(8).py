def are_anagrams(str1,str2):
    str1_cleaned=''.join(char.lower() for char in str1 if char.isalpha()) #removing space and changing all character to lower cases in case sensitive cases
    str2_cleaned=''.join(char.lower() for char in str2 if char.isalpha())

    return sorted(str1_cleaned)== sorted(str2_cleaned)#check if the sorted character in both the string are same



if __name__ == "__main__":
    str1 = input("Enter first string:")
    str2 = input("Enter second string:")
    
    result = are_anagrams(str1,str2)
    
    if result:
        print("The string are anagrams.")
    else:
        print("The string are not anagrams.")