import secrets
import string
import random


def outer():
    x = 'hello'

    def inner1():
        x = 'python'

        def inner2():
            nonlocal x  # this means it is closure - x inside inner2 refers to x in inner1
            x = 'monty'

        print(f"inner before {x}")  # output: inner before python --> here x is still python
        inner2()
        print(f"inner after {x}")  # outpt: inner after monty --> inside inner2() the globla to inner2 is x from inner1

    inner1()
    print(f"outer {x}")  # output: outer hello -->The x of most global is not modified
    # - nonlocal of inner2 only relates to inner1


outer()