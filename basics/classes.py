print( "Hello classes!")

class Programmer:
    def __init__(self, age, name, lang):
        self.age = age
        self.name = name
        self.lang = lang
    def string(self):
        return self.name + " (" + str( self.age) + "): " + self.lang

tomek = Programmer( 20, "Tomek", "C++")
piotrek = Programmer( 25, "Piotrek", "Java")

print( tomek.string())
tomek.test = '007'
print( tomek.test)
