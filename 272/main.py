
def gen(x):
    switch = False
    for i in x:
        for c in i:
            if c == '"':
                if switch:
                    yield "''"
                else:
                    yield "``"
                switch = not switch
            else:
                yield c

import sys
print("".join(gen(sys.stdin)),end="")

