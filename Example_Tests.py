def func1():
    x = 5
    def func2():
        nonlocal x
        x += 6
        print(x)
    func2()
    print(x)
func1()