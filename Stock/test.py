class TestP:
    def notest(self):
        print("notest")

    def __test(self):
        print('yestest')


class TestC(TestP):
    def __init__(self):
        self.name = "yusong"


a = TestC()
a.notest()
a.__test()
