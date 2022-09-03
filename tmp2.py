def good():
    out = ["good"]
    def bad():
        print(out)
    bad()
    print(out)
good()