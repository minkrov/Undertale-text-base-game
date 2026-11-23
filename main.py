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

    # make sure hp doesnt go over max
    player["hp"] += heal
    if player["hp"] > player["max_hp"]:
        player["hp"] = player["max_hp"]
        print(f"* Your HP was maxed out! (HP: {player['hp']}/{player['max_hp']})")
    else:
        print(f"* Recovered {heal} HP! (HP: {player['hp']}/{player['max_hp']})")
    return True


def battle(player, enemy_name, enemy_hp, enemy_atk):
    print("\n========================================")
    print(f"* {enemy_name} blocks the way!")
    print("========================================")

    can_spare = False
    spare_turns = 0
    max_enemy_hp = enemy_hp

    while enemy_hp > 0 and player["hp"] > 0:
        spare_tag = " (Yellow - Can Spare!)" if can_spare else ""
        print(f"\n{player['name']} HP: {player['hp']}/{player['max_hp']}   |   {enemy_name} HP: {enemy_hp}/{max_enemy_hp}{spare_tag}")
        print("[1] FIGHT   [2] ACT   [3] ITEM   [4] MERCY")
        choice = input("> ").strip().lower()

        turn_used = True

        if choice == "1" or choice == "fight":
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
                elif enemy_name == "Toriel":
                    player["kills"] += 1
                    player["atk"] += 3
                    print('\nTORIEL: "Y... you really hate me that much?"')
                    time.sleep(0.8)
                    print('TORIEL: "Now I see who I was protecting by keeping you here. Not you... them!"')
                    print('TORIEL: "Be good, won\'t you? My child..."')
                    print("* Toriel turned to dust.")
                else:
                    gold_drop = random.randint(5, 10)
                    player["gold"] += gold_drop
                    player["kills"] += 1
                    player["atk"] += 2
                    print(f"\n* YOU WON! {enemy_name} turned to dust.")
                    print(f"* You got {gold_drop}G and your ATK went up!")
                return "won"

        elif choice == "2" or choice == "act":
            if enemy_name == "Froggit":
                print("\n[1] Check   [2] Compliment   [3] Threaten")
                act = input("ACT > ").strip().lower()
                if act == "1" or act == "check":
                    print("* FROGGIT - ATK 4 DEF 2. Life is difficult for this enemy.")
                elif act == "2" or act == "compliment":
                    print("* Froggit didn't understand what you said, but was flattered anyway.")
                    can_spare = True
                elif act == "3" or act == "threaten":
                    print("* Froggit didn't understand what you said, but was scared anyway.")
                    can_spare = True
                else:
                    turn_used = False
            elif enemy_name == "Napstablook":
                print("\n[1] Check   [2] Cheer")
                act = input("ACT > ").strip().lower()
                if act == "1" or act == "check":
                    print("* NAPSTABLOOK - ATK 5 DEF 4. This monster doesn't seem to have a sense of humor.")
                elif act == "2" or act == "cheer":
                    print("* You give Napstablook a patient smile.")
                    print('NAPSTABLOOK: "heh... let me show you something..."')
                    print('* Napstablook makes a little top hat out of tears. "i call it dapper blook..."')
                    can_spare = True
                else:
                    turn_used = False
            elif enemy_name == "Toriel":
                print("\n[1] Check   [2] Talk")
                act = input("ACT > ").strip().lower()
                if act == "1" or act == "check":
                    print("* TORIEL - ATK 6 DEF 1. Knows best for you.")
                elif act == "2" or act == "talk":
                    print("* You tried to think of something to say, but couldn't.")
                    print("* (Hint: Maybe just keep choosing MERCY -> Spare to show you won't fight.)")
                else:
                    turn_used = False

        elif choice == "3" or choice == "item":
            turn_used = use_item(player)

        elif choice == "4" or choice == "mercy":
            print("\n[1] Spare   [2] Flee")
            m = input("MERCY > ").strip().lower()
            if m == "1" or m == "spare":
                if enemy_name == "Toriel":
                    spare_turns += 1
                    if spare_turns == 1:
                        print('TORIEL: "....."')
                    elif spare_turns == 2:
                        print('TORIEL: "..... ....."')
                    elif spare_turns == 3:
                        print('TORIEL: "What are you doing? Attack or run away!"')
                    else:
                        print('\nTORIEL: "...Pathetic, is it not? I cannot save even a single child."')
                        time.sleep(0.8)
                        print('TORIEL: "No, I understand. You would just be unhappy trapped down here."')
                        print('TORIEL: "If you truly wish to leave the RUINS... I will not stop you."')
                        print("* Toriel gives you a warm hug and steps aside.")
                        player["spared"] += 1
                        return "spared"
                elif can_spare:
                    gold_drop = random.randint(2, 5)
                    player["gold"] += gold_drop
                    player["spared"] += 1
                    print(f"\n* You spared {enemy_name}! You got {gold_drop}G.")
                    return "spared"
                else:
                    print(f"* {enemy_name} doesn't want to stop fighting yet.")
            elif m == "2" or m == "flee":
                if enemy_name == "Toriel":
                    print("* You can't run away! She's standing right in front of the exit.")
                    turn_used = False
                elif random.randint(1, 2) == 1:
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
        # toriel misses on purpose if your hp gets super low
        if enemy_name == "Toriel" and player["hp"] <= 4:
            print("* Toriel's fireballs deliberately veer away from you at the last second!")
        elif random.randint(1, 5) == 1:
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
    if battle(player, "Froggit", 28, 4) == "dead":
        return

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


def toriel_house(player):
    print("\n----------------------------------------")
    print("* At the end of the Ruins, you reach a cozy little house.")
    print("* Inside, the air smells warmly of butterscotch and cinnamon.")
    print('\nTORIEL: "Surprise! Welcome to your new home, my child."')
    print('TORIEL: "I even have your own room ready down the hall. Make yourself comfortable!"')

    got_pie = False
    while True:
        print("\nWhere do you look?")
        print("[1] Rest in the bedroom")
        print("[2] Read the book on the table")
        print("[3] Check stats")
        print("[4] Go downstairs into the basement")
        c = input("> ").strip()

        if c == "1":
            player["hp"] = player["max_hp"]
            print("* You take a nice nap under the warm covers. (HP fully restored!)")
            if not got_pie:
                player["items"].append("Butterscotch Pie")
                got_pie = True
                print("* When you wake up, there's a slice of Butterscotch Pie on a plate by the door!")
                print("* (Added Butterscotch Pie to items)")
        elif c == "2":
            print('* "Fact #14: Snails actually make terrible shoelaces."')
        elif c == "3":
            show_stats(player)
        elif c == "4":
            break
        else:
            print("* Invalid choice.")

    print("\n----------------------------------------")
    print("* You walk down the long purple basement corridor.")
    print("* At the very end, Toriel stands silently in front of a huge stone door.")
    time.sleep(0.8)
    print('\nTORIEL: "You wish to know how to return \'home\', do you not?"')
    print('TORIEL: "Ahead of us lies the end of the RUINS. A one-way exit to the rest of the underground."')
    print('TORIEL: "I am going to destroy it. Every human that leaves here meets the same fate... ASGORE."')
    print('TORIEL: "If you truly wish to leave... prove to me you are strong enough to survive!"')

    return battle(player, "Toriel", 55, 6)


def ending(player):
    print("\n----------------------------------------")
    print("* Before you step through the heavy doors, Flowey pops up from a patch of dirt.")
    time.sleep(0.8)

    if player["kills"] == 0:
        print('\nFLOWEY: "Clever. Verrrry clever."')
        print('FLOWEY: "You really didn\'t kill a single monster in there, huh?"')
        print('FLOWEY: "Well, good luck keeping that up out there... hehehe..."')
        print("* Flowey sinks into the ground.")
        time.sleep(1.0)
        print("\n* You push open the heavy Ruins doors and step out into a snowy forest.")
        print("* Heavy footsteps crunch in the snow right behind you.")
        time.sleep(0.9)
        print('\n???: "H u m a n ."')
        print('???: "Don\'t you know how to greet a new pal? Turn around and shake my hand."')
        input("\n[Press Enter to turn around and shake his hand] ")
        print("\n* pfffffffffft...")
        time.sleep(0.7)
        print('SANS: "heheh... the old whoopee cushion in the hand trick. it\'s ALWAYS funny."')
        print('SANS: "anyways, you\'re a human, right? i\'m sans. sans the skeleton."')
        print("\n========================================")
        print("   ENDING: PACIFIST (Ruins Cleared!)    ")
        print("========================================")

    elif player["kills"] >= 2:
        print('\nFLOWEY: "Heh... you really turned them all to dust without blinking."')
        print('FLOWEY: "Maybe you and I aren\'t so different after all..."')
        print("* Flowey nervously ducks back into the dirt.")
        time.sleep(0.9)
        print("\n* You step out into the freezing snowy woods. Everything ahead is dead quiet.")
        print("* Even the cameras hidden in the bushes seem afraid to move.")
        print("\n========================================")
        print("         ENDING: NO MERCY               ")
        print("========================================")

    else:
        print('\nFLOWEY: "See? When things got tough, you still swung back."')
        print('FLOWEY: "Just wait until you meet everyone else out there. Hehehe..."')
        print("* Flowey disappears.")
        time.sleep(0.9)
        print("\n* You step through the big stone doors into a cold, snowy forest.")
        print("* Your journey through the Underground has only just begun.")
        print("\n========================================")
        print("          ENDING: NEUTRAL               ")
        print("========================================")

    print(f"Final Stats -> Monsters Spared: {player['spared']} | Monsters Killed: {player['kills']} | Gold: {player['gold']}G")


def play_once():
    print("\n==============================")
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
    if player["hp"] > 0:
        res = toriel_house(player)
        if res != "dead":
            ending(player)


def main():
    while True:
        play_once()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y" and again != "yes":
            print("* See ya, partner.")
            break


if __name__ == "__main__":
    main()
