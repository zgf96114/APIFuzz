"""This module created for APIFuzz
All kinds of Mutators defined
Initial version 0.01 , created on Jun 24th, 2024 by Gaofeng Zhou from Harman China system team.
"""
import random
import os
import string
import numpy as np

seednumber = os.urandom(10)
random.seed(seednumber)

def mutator_int(num: int=1, min: int=-2147483648, max: int=2147483647) ->list:
    if isinstance(num, int) and isinstance(min, int) and isinstance(max, int) and int(max) > int(min):
         if num ==1:
            for _ in range(0, (max - min + 1) ** 2, 1):
                nums_list = random.sample(range(int(min), int(max)), int(num))
                yield nums_list
         else:
            for _ in range(0, (max-min+1)**num, 1):
                nums_list = random.sample(range(int(min),int(max)),int(num))
                yield nums_list
    else:
         raise ("You inputed the wrong values for numbers, min and max.")

def mutator_bytes(len: int=200) ->list:
    for _ in range(256**int(len)):
        num_bytes = random.randint(0, int(len))
        yield os.urandom(num_bytes)

def mutator_chinese(len: int=200) ->list:
    chars_list =[]
    for muts in range(6603*int(len)):
        num = random.randint(0, int(len))
        for _ in range(num):
            head = random.randint(0xb0, 0xf7)
            body = random.randint(0xa1, 0xfe)
            code = f'{head:x}{body:x}'
            try:
                chars_list.append(bytes.fromhex(code).decode('gb2312'))
            except UnicodeDecodeError:
                pass
            #print(chars_list)
        yield ''.join([_ for _ in (chars_list)])

def mutator_strings(len: int=200) ->list:
    letters = string.printable
    for mus in range(100*int(len)):
        num_char = random.randint(0, int(len))
        chars = ''.join(random.choice(letters) for _ in range(num_char))
        yield chars

def mutator_float(num: int=1, min: float=-4194304.0, max: float=4194304.0, step: float= 0.01) ->list:
    if isinstance(num, int) and isinstance(min, float) and isinstance(max, float) and float(max) > float(min):
        for ites in range(30):
            for _ in np.arange(min, max, float(step)):
                rnd = random.randint(0, 15)
                templist = []
                for temp in range(num):
                    templist.append(round(random.uniform(min, max), rnd))
                nums_list = random.sample(templist, num)
                yield nums_list
    else:
        raise ("You inputed the wrong values for numbers, min and max.")



# if __name__ == '__main__':
#     # yy= mutator_float(2, -10.0, 10.0)
#     # print(next(yy))
#     # print(next(yy))
#     # print(next(yy))
#     # tt = mutator_float()
#     # print(next(tt))
#     # print(next(tt))
#     w = mutator_bytes(50)
#     print(next(w))
#     # i = mutator_strings()
#     # print(next(i))
#     pp = mutator_int(1,-20, 20)
#     print(next(pp))
#
#     cc = mutator_chinese(20)
#     print(next(cc))

