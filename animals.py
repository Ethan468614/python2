class Bird(): 

    def __init__(self):
        print("Bird is ready")

    def whoisThis(self):
        print("Bird")

class Penguin(Bird):

    def __init__(self):

        super().__init__()
        print("Penguin is ready")


    def whoisthis(self):
        print("Penguin")    


    def run(self):
        print("Run faster")


peggy = Penguin() 
peggy.whoisthis()
peggy.run()          