class myclass:


    __car = 27

    def __privmeth(self):
        print("Im inside myclass")




    def hello(self) :
        print("Pravite variable value", myclass.__car)


fos = myclass()
fos.hello()
fos.__privmeth()
