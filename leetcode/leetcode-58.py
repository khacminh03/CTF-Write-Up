def lengthOfLastWord(s):
    word = s.strip().split()
    return len(word[len(word) - 1])
word = input()
print(lengthOfLastWord(word))