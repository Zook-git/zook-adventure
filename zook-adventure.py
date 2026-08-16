#!/usr/bin/env python3
"""
========================================
           ZOOK ADVENTURE
========================================
A tiny text-based adventure game.
"""

import sys
import time
import random


def slow_print(text, delay=0.015):
    for ch in text:
        print(ch, end="", flush=True)
        time.sleep(delay)
    print()


def header():
    print("=" * 40)
    print("           ZOOK ADVENTURE")
    print("=" * 40)


def pause():
    input("\n(press Enter to continue) ")


def get_choice(prompt, options):
    """options: dict like {'1': 'Explore', '2': 'Rest'}"""
    while True:
        print(f"\n{prompt}")
        for key, label in options.items():
            print(f"{key}. {label}")
        choice = input("> ").strip()
        if choice in options:
            return choice
        print("Hmm, that's not an option. Try again.")


def game_over(message, win=False):
    print()
    header()
    slow_print(message)
    if win:
        slow_print("\n*** YOU SURVIVED THE FOREST ***")
    else:
        slow_print("\n*** GAME OVER ***")
    print("=" * 40)
    sys.exit(0)


def intro():
    header()
    slow_print("You wake up in a dark forest.")
    slow_print("The air is cold, and you don't remember how you got here.")


def start():
    intro()
    choice = get_choice("What do you do?", {
        "1": "Explore",
        "2": "Rest",
        "3": "Quit",
    })

    if choice == "1":
        explore()
    elif choice == "2":
        rest()
    else:
        slow_print("\nYou decide the forest isn't worth it. Goodbye.")
        sys.exit(0)


def rest():
    slow_print("\nYou sit against a tree and close your eyes for a while.")
    roll = random.random()
    if roll < 0.4:
        slow_print("You wake up feeling refreshed... but something is missing.")
        slow_print("Your bag has been stolen while you slept!")
        pause()
        explore(has_bag=False)
    else:
        slow_print("You wake up feeling much better. No harm done.")
        pause()
        explore(has_bag=True)


def explore(has_bag=True):
    header()
    slow_print("\nYou get up and wander deeper into the forest.")
    slow_print("Soon you reach a fork in the path.")

    choice = get_choice("Which way do you go?", {
        "1": "Left, toward a flickering light",
        "2": "Right, toward the sound of running water",
        "3": "Climb a tall tree to look around",
    })

    if choice == "1":
        flickering_light(has_bag)
    elif choice == "2":
        river(has_bag)
    else:
        climb_tree(has_bag)


def flickering_light(has_bag):
    slow_print("\nYou approach the light and find a small campfire, still warm.")
    slow_print("Beside it lies an old rusty key and a torn map.")

    choice = get_choice("What do you take?", {
        "1": "The rusty key",
        "2": "The torn map",
        "3": "Leave both and back away slowly",
    })

    if choice == "1":
        slow_print("\nYou pocket the key. It hums faintly, as if alive.")
        cave(has_key=True, has_bag=has_bag)
    elif choice == "2":
        slow_print("\nThe map shows a path leading to a cave in the hillside.")
        cave(has_key=False, has_bag=has_bag)
    else:
        slow_print("\nSomething about the fire unsettles you. You step back into the dark.")
        lost_ending()


def river(has_bag):
    slow_print("\nYou find a shallow river glinting under the moonlight.")
    slow_print("On the far bank, you spot the silhouette of a small cabin.")

    choice = get_choice("What do you do?", {
        "1": "Wade across toward the cabin",
        "2": "Follow the river instead",
    })

    if choice == "1":
        slow_print("\nThe water is freezing but shallow. You make it across, soaked but alive.")
        cabin(has_bag)
    else:
        slow_print("\nYou follow the river for what feels like hours...")
        roll = random.random()
        if roll < 0.5:
            slow_print("...until you stumble upon a hidden path leading out of the forest!")
            game_over("You follow the path and see distant lights - a town!", win=True)
        else:
            slow_print("...but the river just loops back to where you started.")
            lost_ending()


def climb_tree(has_bag):
    slow_print("\nYou climb the tallest tree you can find.")
    slow_print("From up high, you can see a cabin to the west and a cave to the north.")

    choice = get_choice("Where do you head?", {
        "1": "The cabin",
        "2": "The cave",
    })

    if choice == "1":
        cabin(has_bag)
    else:
        cave(has_key=False, has_bag=has_bag)


def cave(has_key, has_bag):
    slow_print("\nYou arrive at the mouth of a dark cave. A heavy stone door blocks the way.")
    if has_key:
        slow_print("The rusty key fits perfectly into a slot in the door!")
        slow_print("The door grinds open, revealing a chest full of gold and a way out.")
        game_over("You grab the gold and escape through a tunnel into the morning light.", win=True)
    else:
        choice = get_choice("The door is locked and you have no key. What now?", {
            "1": "Try to force it open",
            "2": "Search the area for another way",
        })
        if choice == "1":
            slow_print("\nYou push with all your strength...")
            if random.random() < 0.3:
                slow_print("The door budges just enough for you to slip through!")
                game_over("Inside, you find an old exit tunnel leading out of the forest.", win=True)
            else:
                slow_print("The door doesn't move an inch. You're exhausted.")
                lost_ending()
        else:
            slow_print("\nYou search the bushes nearby and find nothing but bad news.")
            lost_ending()


def cabin(has_bag):
    slow_print("\nSmoke rises from the cabin's chimney. You knock on the door.")
    choice = get_choice("An old woman answers. What do you do?", {
        "1": "Ask her for help finding your way home",
        "2": "Ask if you can stay the night",
    })

    if choice == "1":
        if has_bag:
            slow_print("\nShe studies your bag and nods. 'I know these woods well. Follow me.'")
            game_over("She guides you safely out of the forest by dawn.", win=True)
        else:
            slow_print("\nShe frowns. 'No bag, no proof you belong out here. I can't risk it.'")
            slow_print("She shuts the door.")
            lost_ending()
    else:
        slow_print("\nShe lets you in. You fall asleep by the fire...")
        slow_print("...and never quite manage to leave. But you're safe, at least.")
        game_over("You spend your days living quietly in the cabin.", win=True)


def lost_ending():
    slow_print("\nThe forest grows darker around you. You wander in circles...")
    game_over("Eventually, your torch goes out, and the forest swallows you whole.")


if __name__ == "__main__":
    try:
        start()
    except KeyboardInterrupt:
        print("\n\nYou flee the forest entirely (goodbye).")
        sys.exit(0)