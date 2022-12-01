# while True:
#     print ('please type your name')
#     name = input()
#     if name == 'peter':
#         break
    
# print('thank you!')


while True:
    print ('please type your name')
    name = input()
    if name != 'peter':
        continue
    
    print ('please enter password')
    while True: 
        password = input()
        if password != '123':
            continue
        else: 
            break
        

print('thank you')
    
