import sys
filename = sys.argv[1]
  
def encrypt_string(string):
    enc_string = ''
    for char in string:
        if char.isalpha():
            char_num = (sum(ord(i) for i in char))
            if (char_num >= 65) and (char_num <= 90):    # Uppercase Letter
                char_num -= 65
                char_num += 13
                char_num = char_num % 26
                char_num += 65
            elif (char_num >= 97) and (char_num <= 122): # Lowercase Letter
                char_num -= 97
                char_num += 13
                char_num = char_num % 26
                char_num += 97
            char_num = chr(char_num)
            enc_string = enc_string + char_num
        else:
            enc_string = enc_string + char
    return enc_string

lines = open(filename)
for line in lines:
    line = line.strip()
    print(encrypt_string(line))
