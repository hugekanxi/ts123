#-*- coding: UTF-8 -*-
def trim(s):
    length = len(s)

    if length > 0:
        for i in range(length):
            if s[i] != ' ':
                break;
        j = length - 1;
        while s[j] == ' ' and j >= i:
            j -= 1
        s = s[i:j + 1]

    return s


def trim2(s):
    if s[0:1]!=' ' and s[-1:0]!=' ':
        return s
    elif s[0]==' ' and s[-1]==' ':
        return  s[1:-1]
    elif s[:1]==' ':
        return s[1:]
    else:
        return s[:-1]

print trim(' hello ')
print trim2(' hello ')

L='1hhh2'
print L[-1]

L='chenhu'
print L[1:-1]


# Test:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
