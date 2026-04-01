
print("hello i am an ai bot. Whats your name?")

name = input()

print(f"Nice to meet you, {name}! ")

print("How are you feeling today? good/bad")

mood = input().lower()

if mood == "good":
    print("Im glad to hear that")

elif mood == "bad":
    print("Im sorry to hear that. I hope your day gets better!\n")
    print("I suggest you to do something you enjoy or talk to a friend or have a cup of tea.\n")
    print("And also watch the sky, the birds and nature for around 10 - 20 minutes.")
          
    

else:
    print("I see, sometimes its hard to put our feelings into words. ")


print("Goodbye! It was nice talking to you ", name)    