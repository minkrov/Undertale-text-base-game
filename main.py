import time
import random


def get_name():
    while True:
        name = input("Name the fallen human: ").strip()
        if name == "":
            return "Frisk"

        low = name.lower()
        if low == "sans":
            print("* nope.")
        elif low == "flowey":
            print("* Hey! I already chose that name.")
        elif low == "toriel":
            print("* I think you should think of your own name, my child.")
        elif low == "chara":
            print("* The true name.")
            return name
        else:
            return name


def flowey_intro(player):
    print("\n----------------------------------------")
    print("* You wake up on a bed of golden flowers.")
    print("* Ahead of you, a small yellow flower pops out of the ground.")
    time.sleep(0.8)

    print('\nFLOWEY: "Howdy! I\'m FLOWEY. FLOWEY the FLOWER!"')
    print('FLOWEY: "Golly, you must be so confused down here in the Underground."')
    print('FLOWEY: "Someone ought to teach you how things work around here!"')
    time.sleep(0.8)

    print("\n* A small red heart (your SOUL) floats in front of your chest.")
    print('FLOWEY: "Down here, LOVE is shared through... little white friendliness pellets."')
    print('FLOWEY: "Move around! Get as many as you can!"')

    print("\n[1] Run into the pellets")
    print("[2] Dodge them")
    choice = input("> ").strip()

    if choice == "1":
        player["hp"] = 1
        print("\n* OUCH! The pellets tear right through you! (HP dropped to 1/20)")
        time.sleep(0.7)
        print('FLOWEY: "You idiot."')
        print('FLOWEY: "In this world, it\'s KILL or BE KILLED."')
    else:
        print("\n* You step out of the way. The pellets fly past.")
        time.sleep(0.6)
        print('FLOWEY: "Hey buddy, you missed them. Run. Into. The. Bullets."')
        print("* Wait... did he just say bullets?")
        print("* Suddenly a ring of pellets surrounds you and hits anyway! (HP dropped to 1/20)")
        player["hp"] = 1
        print('FLOWEY: "Hehehe... DIE."')

    time.sleep(1.0)
    print("\n* Right before the pellets close in, a bright fireball knocks Flowey away!")
    print("* A tall goat-like monster in purple robes steps forward.")
    time.sleep(0.7)
    print('\nTORIEL: "What a terrible creature, torturing such a poor, innocent youth..."')
    print('TORIEL: "Ah, do not be afraid, my child. I am TORIEL, caretaker of the RUINS."')
    player["hp"] = player["max_hp"]
    print("* Toriel healed your wounds! (HP restored to 20/20)")
    print('TORIEL: "Come! I will guide you through the catacombs."')


def main():
    print("==============================")
    print("       UNDERTALE (text)       ")
    print("==============================")
    print("Long ago, two races ruled over Earth: HUMANS and MONSTERS.")
    print("After a long war, monsters were sealed underground beneath Mt. Ebott.")
    print("Many years later... you climbed the mountain, tripped on a vine,")
    print("and fell down into the dark.\n")

    name = get_name()
    player = {
        "name": name,
        "hp": 20,
        "max_hp": 20,
        "atk": 5,
        "gold": 0,
        "items": ["Bandage"],
        "kills": 0,
        "spared": 0,
    }

    print(f"\n* Stay determined, {player['name']}!")
    time.sleep(0.6)

    flowey_intro(player)
    print("\n[To be continued in the Ruins...]")


if __name__ == "__main__":
    main()
