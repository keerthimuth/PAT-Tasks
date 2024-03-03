def is_palindrome(kiki):
    new_string = ''.join(kiki.split()).lower()
    return new_string == new_string[::-1]

if __name__ == "__main__":
    keerthi = input("Enter the String:")
    result = is_palindrome(keerthi)
    
    if result:
        print("The given string is palindrome.")
        
    else:
        print("The given string in not palindrome.")
        