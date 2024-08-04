check = [
3910918,
3921698,
3921709,
3820578,
3921671,
3893657,
3911025,
3932159,
3820987,
3820987,
3895614,
3822653,
3919793,
3913160,
3822626,
3896081,
3911023,
3910936,
3813209,
3869603,
3813122,
3913158,
3921672,
3810527,
3871544,
3871506,
3893694,
3919755,
3893639,
3895583,
3893664,
3895813]
def solve(b):
    b = callNextTick(b)
    b = callSetTimeout(b)
    b = callImmediate(b)
    return b

def solve1(b):
    b = callImmediate(b)
    b = callNextTick(b)
    b = callSetTimeout(b)
    return b


def callNextTick(a):
    a = a ^ ((a >> 6) | (a << 2))
    return a ^ ((a >> 5) | (a << 3))

def callImmediate(a):
    return a ^ ((a >> 7) | (a << 1))

def callSetTimeout(a):
    return a ^ ((a >> 4) | (a << 4))

flag = []
for i in range(0, len(check)):
    for k in range(0x0, 0x7f):
        c = solve(k ^ (2303 - i))
        d = solve1(k ^ (2303 - i))
        if c == check[i]:
            flag.append(chr(k))
            break
        elif d == check[i]:
            flag.append(chr(k))
            break

print("".join(flag[::-1]))
