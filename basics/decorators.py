print( "Hello decorators!")

def mydecorator( f):
    decor = "+"
    def pretty():
        print( decor * 30)
        f()
        print( decor * 30)
    return pretty

def myfun():
    print( "Hello!")

@mydecorator
def myfun2():
    print( "World!")

mydecorator(myfun)()
myfun2()





