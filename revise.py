
print("hello i am an ai bot. Whats your name?")

name = input()

print(f"Nice to meet you, {name}! ")

print("How are you feeling today? good/bad")

mood = input().lower()

if mood == "good":
    print("Im glad to hear that")

elif mood == "bad":
    print("Im sorry to hear that. I hope your day gets better!")

else:
    print("I see, sometimes its hard to put our feelings into words. ")


print("Goodbye! It was nice talking to you ", name)    