def good():
    a = 10

    def bad():
        nonlocal a
        print(a)
        a = 20

    bad()
    print(a)

good()