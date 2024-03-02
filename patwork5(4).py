def unique_char(code_string):
    unique= set(code_string)
    return len(unique) 


if __name__ == "__main__":
    string_input = input("Enter the input:")
    result = unique_char(string_input)
    print(result)