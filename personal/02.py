# def f():
    
#     result = 0 
#     for  i in range (4): 
#         result = i ** 2
    
#     return result

# print (f())

# quiz1
def print_pattern(n):
    word = "abcdefghijklmnopqrstuvwxyz"
    
    for character in range (0, len(word)):
        
        word_no = ord(word[character])
        for i in range (0,5):
            for j in range (0, i+1):
                showword = chr(word_no)
                print(showword, end=' ')
            
            return(n)

print_pattern(5)