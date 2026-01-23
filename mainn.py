import random
import string

choise = int(input("Enter a number: "))
var2 = string.ascii_lowercase + string.ascii_uppercase + string.digits

var = ''
for i in range(choise):
    var += random.choice(var2)

print('generated password is:', var)

