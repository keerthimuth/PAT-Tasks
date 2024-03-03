def common_substring(str1,str2):
    m=len(str1)
    n=len(str2)
    
    table = [[0] * (n+1) for _ in range(m+1)]
    max_length =0
    end_position=0
    
    for i in range(1,m+1):
        for j in range(1,n+1):
            if str1[i-1]==str2[j-1]:
                table[i][j]==table[i-1][j-1]+1
                if table[i][j]>max_length:
                    max_length = table[i][j]
                    end_position = 0
                    
                else:
                    table[i][j]=0
            
    common_string =str1[end_position - max_length:end_position]
    return common_string
            


if __name__ == "__main__":
    str1 = input("Enter the first string:")
    str2 = input("Enetr the second string:")
    
    result=common_substring(str1,str2)
    
    if result:
        print("Longest common Substring:",result)
    else:
        print("No common longest Substring.")