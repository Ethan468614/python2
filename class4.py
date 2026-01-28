class Employee():


    def __init__(self):
        print("Employee created")


    def __del__(self):
        print("Destructor called") 

    
def createobj():
    print("Making object...")
    obj = Employee()
    print("Function end...")
    return obj

print("Calling createobj() function...")
obj = createobj()
print("Program End...")