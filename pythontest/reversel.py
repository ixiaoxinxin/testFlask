string = 'abcdef'
def string_reverse5(string):
    #return ''.join(string[len(string) - i] for i in range(1, len(string)+1))
    return ''.join(string[i] for i in range(len(string)-1, -1, -1))
print  ''.join(string[i] for i in range(len(string)-1, -1, -1))


def string_reverse3(string):
    if len(string) <= 1:
        return string
    return string_reverse3(string[1:]) + string[0]
print string_reverse3(string[1:]) + string[0]