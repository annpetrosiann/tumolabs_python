import random

def get_input(prompt):
    """Ask the player for a word/value."""
    return input(prompt).strip()


def hospital_story():
    print("\n--- Hospital Story ---")
    number = get_input("Type a number: ")
    time = get_input("Type a measure of time: ")
    transportation = get_input("Type a mode of transportation: ")
    adjective = get_input("Type an adjective: ")
    adjective2 = get_input("Type another adjective: ")
    noun = get_input("Type a noun: ")
    color = get_input("Type a color: ")
    body_part = get_input("Type a part of the body: ")
    verb = get_input("Type a verb: ")
    number2 = get_input("Type another number: ")
    noun2 = get_input("Type another noun: ")
    noun3 = get_input("Type a noun: ")
    body_part2 = get_input("Type another part of the body: ")
    verb2 = get_input("Type a verb: ")
    noun4 = get_input("Type a noun: ")
    adjective3 = get_input("Type an adjective: ")
    silly_word = get_input("Type a silly word: ")

    story = (
        f"It was about {number} {time} ago when I arrived at the hospital "
        f"in a {transportation}. The hospital is a/an {adjective} place, "
        f"there are a lot of {adjective2} {noun} here. There are nurses here "
        f"who have {color} {body_part}. If someone wants to come into my room "
        f"I told them that they have to {verb} first. I've decorated my room "
        f"with {number2} {noun2}. Today I talked to a doctor and they were "
        f"wearing a {noun3} on their {body_part2}. I heard that all doctors "
        f"{verb2} {noun4} every day for breakfast. The most {adjective3} "
        f"thing about being in the hospital is the {silly_word} {noun}!"
    )

    return story


def camping_story():
    print("\n--- Camping Story ---")
    name = get_input("Type a person's name: ")
    noun = get_input("Type a noun: ")
    feeling = get_input("Type an adjective (feeling): ")
    verb = get_input("Type a verb: ")
    feeling2 = get_input("Type another adjective (feeling): ")
    animal = get_input("Type an animal: ")
    verb2 = get_input("Type another verb: ")
    color = get_input("Type a color: ")
    ing_verb = get_input("Type a verb ending in -ing: ")
    adverb = get_input("Type an adverb ending in -ly: ")
    number = get_input("Type a number: ")
    time = get_input("Type a measure of time: ")
    color2 = get_input("Type another color: ")
    animal2 = get_input("Type another animal: ")
    number2 = get_input("Type another number: ")
    silly_word = get_input("Type a silly word: ")
    noun2 = get_input("Type another noun: ")

    story = (
        f"This weekend I am going camping with {name}. I packed my lantern, "
        f"sleeping bag, and {noun}. I am so {feeling} to {verb} in a tent. "
        f"I am {feeling2} we might see a(n) {animal}, I hear they're kind of "
        f"dangerous. While we're camping, we are going to hike, fish, and "
        f"{verb2}. I have heard that the {color} lake is great for "
        f"{ing_verb}. Then we will {adverb} hike through the forest for "
        f"{number} {time}. If I see a {color2} {animal2} while hiking, "
        f"I am going to bring it home as a pet! At night we will tell "
        f"{number2} {silly_word} stories and roast {noun2} around the campfire!!"
    )

    return story


def castle_story():
    print("\n--- Enchanted Castle Story ---")
    name = get_input("Type a person's name: ")
    adjective = get_input("Type an adjective: ")
    color = get_input("Type a color: ")
    animal = get_input("Type an animal: ")
    place = get_input("Type a place: ")
    adjective2 = get_input("Type another adjective: ")
    creature = get_input("Type a magical creature (plural): ")
    adjective3 = get_input("Type another adjective: ")
    creature2 = get_input("Type another magical creature (plural): ")
    room = get_input("Type a room in a house: ")
    noun = get_input("Type a noun: ")
    noun2 = get_input("Type another noun: ")
    noun3 = get_input("Type a noun (plural): ")
    adjective4 = get_input("Type another adjective: ")
    noun4 = get_input("Type a noun (plural): ")
    number = get_input("Type a number: ")
    time = get_input("Type a measure of time: ")
    ing_verb = get_input("Type a verb ending in -ing: ")
    adjective5 = get_input("Type another adjective: ")
    noun5 = get_input("Type another noun: ")

    story = (
        f"Dear {name}, I am writing to you from a {adjective} castle in an "
        f"enchanted forest. I found myself here one day after going for a ride "
        f"on a {color} {animal} in {place}. There are {adjective2} {creature} "
        f"and {adjective3} {creature2} here! In the {room} there is a pool "
        f"full of {noun}. I fall asleep each night on a {noun2} of {noun3} "
        f"and dream of {adjective4} {noun4}. It feels as though I have lived "
        f"here for {number} {time}. I hope one day you can visit, although "
        f"the only way to get here now is {ing_verb} on a {adjective5} {noun5}!!"
    )

    return story


def main():
    templates = [
        "Hospital",
        "Camping",
        "Enchanted Castle"
    ]

    print("Welcome to Python Station Project 1")
    print("\nChoose a story template:")

    # Loop through the list of templates to display the menu
    for index in range(len(templates)):
        print(f"{index + 1}. {templates[index]}")

    choice = get_input("\nEnter 1, 2, or 3: ")

    # Condition: check whether the user selected a valid option
    if choice not in ["1", "2", "3"]:
        print("Invalid choice. Please run the program again and choose 1, 2, or 3.")
        return

    # The selected template is chosen from a one-item list.
    selected_template = random.choice([choice])

    if selected_template == "1":
        story = hospital_story()
    elif selected_template == "2":
        story = camping_story()
    else:
        story = castle_story()

    print("\n" + "=" * 60)
    print("YOUR MAD LIBS STORY")
    print("=" * 60)
    print(story)
    print("=" * 60)


main()
