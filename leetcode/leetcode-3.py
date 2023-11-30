def longestString(string):
    longest_string = ""
    max_length = 0
    
    for i in range (len(string)):
        seen_chars = set()
        current_substring = ""
        current_length = 0
        
        for j in range (i, len(string)):
            if (string[j] not in seen_chars):
                seen_chars.add(string[j])
                current_substring += string[j]
                print("current substring: " + current_substring)
                current_length += 1
        
        if (current_length > max_length):
            max_length = current_length
            longest_string = current_substring
        
    print("Longest string: " + longest_string)

string = input("Nhập chuỗi: ")
longestString(string)
