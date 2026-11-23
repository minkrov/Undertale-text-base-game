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


def show_stats(player):
    print("\n--- STATS ---")
    print(f"Name:  {player['name']}")
    print(f"HP:    {player['hp']}/{player['max_hp']}")
    print(f"ATK:   {player['atk']}")
    print(f"Gold:  {player['gold']}G")
    if len(player["items"]) == 0:
        print("Items: (empty)")
    else:
        print("Items: " + ", ".join(player["items"]))
    print("-------------")


def use_item(player):
    if len(player["items"]) == 0:
        print("* You don't have any items!")
        return False

    print("\nChoose an item (or 0 to go back):")
    for i in range(len(player["items"])):
        print(f"[{i + 1}] {player['items'][i]}")

    pick = input("> ").strip()
    if not pick.isdigit():
        return False

    idx = int(pick) - 1
    if idx < 0 or idx >= len(player["items"]):
        return False

    item = player["items"].pop(idx)
    if item == "Bandage":
        heal = 10
    elif item == "Monster Candy":
        heal = 10
        print("* You ate the Monster Candy. Very un-licorice-like.")
    elif item == "Spider Donut":
        heal = 12
        print("* You ate the Spider Donut. Don't worry, Spider didn't mind.")
    elif item == "Butterscotch Pie":
        heal = 99
        print("* You ate the Butterscotch-Cinnamon Pie.")
    else:
        heal = 8

    player["hp"] += heal
    print(f"* Recovered {heal} HP! (HP: {player['hp']}/{player['max_hp']})")
    return True


def battle(player, enemy_name, enemy_hp, enemy_atk):
    print("\n========================================")
    print(f"* {enemy_name} blocks the way!")
    print("========================================")

    can_spare = False
    max_enemy_hp = enemy_hp

    while enemy_hp > 0 and player["hp"] > 0:
        spare_tag = " (Yellow - Can Spare!)" if can_spare else ""
        print(f"\n{player['name']} HP: {player['hp']}/{player['max_hp']}   |   {enemy_name} HP: {enemy_hp}/{max_enemy_hp}{spare_tag}")
        print("[1] FIGHT   [2] ACT   [3] ITEM   [4] MERCY")
        choice = input("> ").strip()

        turn_used = True

        if choice == "1":
            dmg = player["atk"] + random.randint(2, 6)
            enemy_hp -= dmg
            if enemy_name == "Napstablook":
                print(f"* You swing for {dmg} damage... it passes right through him.")
                print('NAPSTABLOOK: "oh... sorry... i\'ll lower my hp anyway just to be polite..."')
            else:
                print(f"* You strike {enemy_name} for {dmg} damage!")

            if enemy_hp <= 0:
                if enemy_name == "Napstablook":
                    print('NAPSTABLOOK: "umm... you know you cant actually kill a ghost, right? awkward..."')
                    print("* Napstablook awkwardly fades away. You gained 0 EXP.")
                else:
                    gold_drop = random.randint(5, 10)
                    player["gold"] += gold_drop
                    player["kills"] += 1
                    player["atk"] += 2
                    print(f"\n* YOU WON! {enemy_name} turned to dust.")
                    print(f"* You got {gold_drop}G and your ATK went up!")
                return "won"

        elif choice == "2":
            if enemy_name == "Froggit":
                print("\n[1] Check   [2] Compliment   [3] Threaten")
                act = input("ACT > ").strip()
                if act == "1":
                    print("* FROGGIT - ATK 4 DEF 2. Life is difficult for this enemy.")
                elif act == "2":
                    print("* Froggit didn't understand what you said, but was flattered anyway.")
                    can_spare = True
                elif act == "3":
                    print("* Froggit didn't understand what you said, but was scared anyway.")
                    can_spare = True
                else:
                    turn_used = False
            elif enemy_name == "Napstablook":
                print("\n[1] Check   [2] Cheer")
                act = input("ACT > ").strip()
                if act == "1":
                    print("* NAPSTABLOOK - ATK 5 DEF 4. This monster doesn't seem to have a sense of humor.")
                elif act == "2":
                    print("* You give Napstablook a patient smile.")
                    print('NAPSTABLOOK: "heh... let me show you something..."')
                    print('* Napstablook makes a little top hat out of tears. "i call it dapper blook..."')
                    can_spare = True
                else:
                    turn_used = False

        elif choice == "3":
            turn_used = use_item(player)

        elif choice == "4":
            print("\n[1] Spare   [2] Flee")
            m = input("MERCY > ").strip()
            if m == "1":
                if can_spare:
                    gold_drop = random.randint(2, 5)
                    player["gold"] += gold_drop
                    player["spared"] += 1
                    print(f"\n* You spared {enemy_name}! You got {gold_drop}G.")
                    return "spared"
                else:
                    print(f"* {enemy_name} doesn't want to stop fighting yet.")
            elif m == "2":
                if random.randint(1, 2) == 1:
                    print("* I'm outta here! You escaped.")
                    return "fled"
                else:
                    print("* Couldn't get away!")
            else:
                turn_used = False
        else:
            print("* Pick 1, 2, 3, or 4.")
            turn_used = False

        if not turn_used:
            continue

        # enemy turn
        time.sleep(0.4)
        if random.randint(1, 5) == 1:
            print(f"* {enemy_name} attacked, but you dodged out of the way!")
        else:
            hit = random.randint(2, enemy_atk)
            player["hp"] -= hit
            print(f"* {enemy_name} hits you for {hit} damage!")

    if player["hp"] <= 0:
        print("\n* Your SOUL shatters in half...")
        print(f'VOICE: "{player["name"]}! Stay determined!"')
        print("========== GAME OVER ==========")
        return "dead"


def ruins(player):
    print("\n----------------------------------------")
    print("* Toriel leads you through a couple simple switch puzzles, then runs ahead")
    print("* to prepare a surprise for you at her house, asking you to walk carefully.")
    print("\n* You enter a quiet purple stone room. A glittering star floats nearby.")
    print("* Touching it fills you with determination.")
    print("* In the corner sits a pedestal with a bowl labeled: 'Take one.'")

    candy_taken = 0
    while True:
        print("\nWhat do you do?")
        print("[1] Take a piece of candy")
        print("[2] Check stats")
        print("[3] Keep walking down the corridor")
        c = input("> ").strip()

        if c == "1":
            if candy_taken == 0:
                player["items"].append("Monster Candy")
                candy_taken += 1
                print("* You took a piece of Monster Candy.")
            elif candy_taken == 1:
                player["items"].append("Monster Candy")
                candy_taken += 1
                print("* You took another piece. You feel like the scum of the earth.")
            elif candy_taken == 2:
                candy_taken += 1
                print("* You grabbed too fast and spilled the whole bowl onto the floor. Nice job.")
            else:
                print("* The bowl is empty. Look at what you've done.")
        elif c == "2":
            show_stats(player)
        elif c == "3":
            break
        else:
            print("* Invalid choice.")

    print("\n* As you walk through a pile of crunching red leaves, something hops out!")
    battle(player, "Froggit", 28, 4)

    print("\n----------------------------------------")
    print("* Further down the hall, you spot 10G hidden under some leaves! (+10G)")
    player["gold"] += 10
    print("* Nearby, a small spider web has a sign: 'Spider Bake Sale - Donuts 7G'.")
    print("* Blocking the exit doorway ahead, a ghost is lying flat on the ground")
    print("* saying 'zzzzzzzz' out loud repeatedly.")

    bought_donut = False
    while True:
        print("\nWhat do you do?")
        print("[1] Move the ghost with force")
        print("[2] Lie down next to him")
        print("[3] Buy a Spider Donut (7G)")
        print("[4] Check stats")
        c = input("> ").strip()

        if c == "1":
            battle(player, "Napstablook", 35, 5)
            break
        elif c == "2":
            print("\n* You lie flat on the cold stone floor next to the ghost.")
            time.sleep(0.7)
            print('NAPSTABLOOK: "oh... hey... are you feeling like garbage too?"')
            print("* For a moment, it feels like the room melts into outer space. Pretty chill.")
            print('NAPSTABLOOK: "well... i\'ll get out of your hair now. bye..."')
            player["spared"] += 1
            break
        elif c == "3":
            if bought_donut:
                print("* The spiders wave politely. One donut per customer!")
            elif player["gold"] >= 7:
                player["gold"] -= 7
                player["items"].append("Spider Donut")
                bought_donut = True
                print("* Four spiders crawl down and hand you a Spider Donut! (-7G)")
            else:
                print(f"* Not enough gold! You only have {player['gold']}G.")
        elif c == "4":
            show_stats(player)
        else:
            print("* Invalid choice.")


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
    ruins(player)
    print("\n[Next up: Toriel's house...]")


if __name__ == "__main__":
    main()
