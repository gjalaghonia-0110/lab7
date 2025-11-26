# auto obfuscated (like pyarmor would do)

import base64 as _0b
import codecs as _0c

_=lambda __:_0b.b64decode(_0c.encode(__,'rot_13')).decode()
__=lambda ___:eval(compile(_(___),'<λ>','exec'))or globals()

# encoded fib
_0=('ZnVuY3Rpb25zPXt9CmZ1bmN0aW9uc1snZmliJ109bGFtYmRhIG46MCBpZiBuPD0wIGVsc2UgMSBpZiBu'
    'PT0xIGVsc2UgKGxhbWJkYSBhLGI6W2EuYXBwZW5kKGFbLTFdK2FbLTJdKSBmb3IgXyBpbiByYW5nZShu'
    'LTEpXSBvciBhWy0xXSkoWzAsMV0sW10p')

# working version
exec(compile('''
_=[lambda n:0 if n<=0 else 1 if n==1 else _[0](n-1)+_[0](n-2) if n<10 else (lambda p,c:[[p:=c,c:=p+c][1] for _ in range(n-1)][-1])(*[0,1])]
__=[lambda n:1 if n<=1 else (lambda r:[r:=r*i for i in range(2,n+1)][-1])(1)]
'''.replace(':=',':='),'','exec'))

# wrappers
def _0x1f3a(n):
    if n <= 0: return 0
    if n == 1: return 1
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b

def _0x2b7c(n):
    r = 1
    for i in range(2, n + 1):
        r *= i
    return r if n > 0 else 1

# strings
_s1 = bytes([70^0,105^0,98^0,111^0,110^0,97^0,99^0,99^0,105^0]).decode()
_s2 = bytes([70,97,99,116,111,114,105,97,108]).decode()

if __name__ == (lambda:__import__('__main__').__name__)():
    print(_s1 + (chr(58)))
    [print(f'{(lambda x:x)(_)}'+chr(45)+chr(62)+f'{_0x1f3a(_)}') for _ in range((5<<1))]
    print(chr(10) + _s2 + chr(58))
    [print(f'{_}'+chr(33)+chr(61)+f'{_0x2b7c(_)}') for _ in range(1,(1<<3))]

