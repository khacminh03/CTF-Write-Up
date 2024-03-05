import base64
 
def reverse_string(s):
    return s[::-1]
 
 
def scramble_flag(flag):
    scrambled = ''
    for i, char in enumerate(flag):
        if i % 2 == 0:
            scrambled += chr(ord(char) + 1)
            continue
        scrambled += chr(ord(char) - 1)
    return scrambled
 
 
def main():
    secret_flag = scramble_flag(reverse_string(base64.b64decode('Q0hIe3B5dGhvbjJFeGlfUmV2ZXJzZV9FTmdpbmVyaW5nfQ==')).decode())
    print('Welcome to PyReverser!')
    print('Please enter a word or phrase:')
    user_input = input()
    generated_value = scramble_flag(reverse_string(user_input.upper()))
    print('Generated value:', generated_value)
    print('Can you find the hidden flag?')
    reversed_flag = reverse_string(secret_flag)
    print('Reversed flag:', reversed_flag)
 
if __name__ == '__main__':
    main()
