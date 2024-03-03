def no_words(str1):
    words = str1.split()
    return len(words)



if __name__ == "__main__":
    str1 =input("Enter the string:")
    result=no_words(str1)
    
    print("Numbe of words in the given string:",result)