### REPLACEMENT TO SWITCH #####

def dow_switch_fn(dow):  #func thast returns day of week
    if dow==1:
        fn=lambda :print("Sunday")
    elif dow==2:
        fn=lambda :print("Monday")
    elif dow==3:
        fn=lambda :print("Tueday")
    elif dow==4:
        fn=lambda :print("Wednday")
    elif dow==5:
        fn=lambda :print("Thursday")
    elif dow==6:
        fn=lambda :print("Friday")
    elif dow==7:
        fn=lambda :print("Saturday")
    else:
        fn = lambda: print("Invalid day of week!")

    return fn()

#dow_switch_fn(1) #output: Sunday
#dow_switch_fn(100) #output: Invalid day of week!

def dow_switch_dict(dow):
    dow_dict = {
        1: lambda: print("Sunday"),
        2: lambda: print("Monday"),
        3: lambda: print("Tuesday"),
        4: lambda: print("Wednday"),
        5: lambda: print("Thursday"),
        6: lambda: print("Friday"),
        7: lambda: print("Saturday"),
        'default': lambda: print('Invalid Number!')
    }
    return dow_dict.get(dow,dow_dict['default'])()

#dow_switch_dict(1)
#dow_switch_dict(100)

### Final method is to use the single dispatch decorator pattern ###
def switcher(fn):
    registry = dict()
    registry['default']=fn

    def register(case):
        def inner(fn):
            registry[case]=fn
            return fn
        return inner

    def decorator(case):
        fn = registry.get(case,registry['default'])
        return fn()

    decorator.register=register
    return decorator

@switcher
def dow():
    return 'Invalid day of week!'

@dow.register(1)
def dow_1():
    return 'Sunday'

dow.register(2)(lambda :'Monday')
dow.register(3)(lambda :'Tuesday')
dow.register(4)(lambda :'Wednsday')
dow.register(5)(lambda :'Thursday')
dow.register(6)(lambda :'Friday')
dow.register(7)(lambda :'Saturday')

print(dow(1))   #output: Sunday
print(dow(100)) #output: Invalid day of week!


# def main():
#
# if __name__ == '__main__':
#     main()
