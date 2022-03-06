import day8src as src
print(src.logo)
# import math
# #Write your code below this line 👇
# def paint_calc(height, width, cover):
#     print('you need',math.ceil(height*width/cover), 'cans')

# #Write your code above this line 👆
# # Define a function called paint_calc() so that the code below works.   

# # 🚨 Don't change the code below 👇
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)

#Write your code below this line 👇
# def prime_checker(number):
#     if number == 2 or 3 or 5 or 7:
#         print('this prime number')
    
#     elif number%2 ==0 or number%3==0 or number%5==0 or number%7==0:
#         print('this is not prime number')
#     else: 
#         print ('this is prim number')

# def prime_check(number):
#     it_prime=True
#     for n in range(2,number):
#         if number%n==0:
#             it_prime=False
#     if it_prime:
#         print('it is a prime number')
#     else:
#         print('it is not a prime number')



# #Write your code above this line 👆
    
# #Do NOT change any of the code below👇
# n = int(input("Check this number: "))
# # prime_checker(number=n)
# prime_check(number=n)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def ceiser_fun(plain_text,shift_number,direction_type):
    output_text=''
    shift_number%=len(alphabet)
    for letter in plain_text:
        if letter in alphabet:
            i=alphabet.index(letter)
            if direction_type=='encode':
                i2=i+shift_number
                i2%=len(alphabet)
            elif direction_type=='decode':
                i2=i-shift_number
            output_text+=alphabet[i2]

            # if i2<len(alphabet): # if letter in the first of list
            #     output_text+=alphabet[i2]
            # elif i2>=len(alphabet): # if letter in the last list
            #     i3=i2%len(alphabet)
            #     output_text+=alphabet[i3]
        else: # if letter is not alphabet, will be writtern as it
            output_text+=letter

    print(output_text)

again=True
while again:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    ceiser_fun(text,shift,direction)
    ask_again=input('do you need to encode or decode again?: yes or no; ').lower()
    if ask_again=='no':
        again=False
print('GoodBye:) ')

# def encode(plain_text,shift_number):
#     encode_word2=''
#     for char in plain_text:
#         if char in alphabet:
#             i=alphabet.index(char)
#             i2=i+shift_number
#             if i2<len(alphabet):
#                 encode_word2+=alphabet[i2]
#             elif i2>len(alphabet):
#                 i3=i2%len(alphabet)
#                 encode_word2+=alphabet[i3]
            
#         else:
#             encode_word2+=char
#             # encode_list.append(char)
#     # encode_word=''
#     # print(encode_word.join(encode_list))
#     print(encode_word2)
   

# def decode(plain_text,shift_number):
#     decode_list=[]
#     for char in plain_text:
#         if char in alphabet:
#             i=alphabet.index(char)
#             i2=i-shift_number
#             if i2>=0:
#                 decode_list.append(alphabet[i2])
#             elif i2<0:
#                 decode_list.append(alphabet[len(alphabet)+i2])
#         else:
#             decode_list.append(char)
#     decode_word=''
#     print(decode_word.join(decode_list))
    

# if direction=='encode':
#     encode(text,shift)
# elif direction=='decode':
#     decode(text,shift)
