alphabet = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ"+ \
            "[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
def decode_secret(secret):
    rotate_const = 47
    decoded = ""
    for c in secret:
        index = alphabet.find(c)
        original_index = (index + rotate_const) % len(alphabet)
        decoded = decoded + alphabet[original_index]

    print(decoded)

decode_secret("A:4@r%uL`M-^M0c0AbcM-MFE02fh3e4a5N")
#Flag: picoCTF{1|\/|_4_p34|\|ut_a79b6c2d}