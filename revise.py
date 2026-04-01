def chat_bot():
    name = input("Hello! I am an AI bot. What's your name?\n> ").strip()
    print(f"\nNice to meet you, {name}!")

    
    print("How are you feeling today?")
    mood = input("(e.g., good, bad, tired, excited, anxious)\n> ").strip().lower()
    
    print() 

    
    if "good" in mood or "great" in mood or "happy" in mood:
        print("I'm so glad to hear that! Keep riding that positive wave!")

    elif "bad" in mood or "sad" in mood:
        print("""I'm sorry to hear that. I hope your day gets better!
I suggest you do something you enjoy, talk to a friend, or have a cup of tea.
Also, try watching the sky, the birds, and nature for around 10 - 20 minutes.""")

    elif "tired" in mood or "exhausted" in mood:
        print("Make sure you're getting enough rest! Taking a quick nap or just stepping away from your screen for a bit can do wonders.")

    elif "excited" in mood:
        print("That's awesome!, But calm down a bit, you don't want to burn out. Try to channel that excitement into something productive or creative!")

    elif "anxious" in mood or "stressed" in mood:
        print("Take a deep breath. Try to focus on just one small thing at a time. You've got this, and it's okay to take a break.")

    else:
        
        print("I see. Feelings can be complicated, and sometimes it's hard to put them into words. Whatever you're experiencing, it's valid.")

    print(f"\nGoodbye! It was nice talking to you, {name}.")

if __name__ == "__main__":
    chat_bot()