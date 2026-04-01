import re, random
from colorama import Fore, init


init(autoreset=True)

destinations = {"beachs": ["Bali", "Maldives", "Phuket" ], "mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas"], "cities":["Tokyo", "Paris", "New York"]}

jokes = ["Why don't programmers like nature? It has too many bugs.", "Why did the computer go to the doctor? Because it had a virus!", "Why do travelers always feel warm? Because of all their hot spots!"]

def normalize_input(text):
    return re.sub(r"\s+", "", text.strip().lower())


def recommend_destination(): 
    suggestion = random.choice(destinations[preference])

    print(Fore.GREEN + f"Travel Bot: How about {suggestion}?")
    print(Fore.CYAN + "Travel Bot: DO you like it yes/no")
    answer = input(Fore.YELLOW + "You: ").lower()

    if answer == "yes":
        print(Fore.GREEN + f"Travel Bot: Awesome! Enjoy! {suggestion}")

    elif answer == "no":
        print(Fore.RED + "Travel Bot: Lets try another .")
        recommend_destination()

    else: 
        print(Fore.RED + "Travel Bot: I'll suggest again.")
        recommend_destination()

    else: 
    print(Fore.RED + "Travel Bot: Sorry, I don't have that type of destination")
    recommend_destination()


