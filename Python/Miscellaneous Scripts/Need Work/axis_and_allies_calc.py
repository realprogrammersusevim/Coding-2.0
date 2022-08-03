#!python3
import random

attack_unit = {
    "infantry": int(input("Enter the number of attacking infantry: ")),
    "artillery": int(input("Enter the number of attacking artillery: ")),
    "tanks": int(input("Enter the number of attacking tanks: ")),
    "fighters": int(input("Enter the number of attacking fighters: ")),
    "bombers": int(input("Enter the number of attacking bombers: ")),
}

defend_unit = {
    "infantry": int(input("Enter the number of defending infantry: ")),
    "artillery": int(input("Enter the number of defending artillery: ")),
    "tanks": int(input("Enter the number of defending tanks: ")),
    "fighters": int(input("Enter the number of defending fighters: ")),
    "bombers": int(input("Enter the number of defending bombers: ")),
}

promoted_infantry = 0
infantry = attack_unit["infantry"]
while promoted_infantry != attack_unit["artillery"] and infantry != 0:
    promoted_infantry += 1


def roll_dice(num):
    rand = random.randint(1, 6)
    if rand <= num:
        return 1
    else:
        return 0


def compute_attack_hits():
    attack_hits = 0

    for i in range(attack_unit["infantry"]):
        attack_hits += roll_dice(1)

    for i in range(promoted_infantry):
        attack_hits += roll_dice(2)

    for i in range(attack_unit["artillery"]):
        attack_hits += roll_dice(2)

    for i in range(attack_unit["tanks"]):
        attack_hits += roll_dice(3)

    for i in range(attack_unit["fighters"]):
        attack_hits += roll_dice(3)

    for i in range(attack_unit["bombers"]):
        attack_hits += roll_dice(4)

    return attack_hits


def compute_defend_hits():
    defend_hits = 0

    for i in range(defend_unit["infantry"]):
        defend_hits += roll_dice(2)

    for i in range(defend_unit["artillery"]):
        defend_hits += roll_dice(2)

    for i in range(defend_unit["tanks"]):
        defend_hits += roll_dice(3)

    for i in range(defend_unit["fighters"]):
        defend_hits += roll_dice(4)

    for i in range(defend_unit["bombers"]):
        defend_hits += roll_dice(1)

    return round(defend_hits)


def take_losses():
    attack_hits = compute_attack_hits()
    defend_hits = compute_defend_hits()

    while attack_hits != 0:
        if attack_unit["infantry"] != 0:
            attack_unit["infantry"] -= 1
            attack_hits -= 1
        elif attack_unit["artillery"] != 0:
            attack_unit["artillery"] -= 1
            attack_hits -= 1
        elif attack_unit["tanks"] != 0:
            attack_unit["tanks"] -= 1
            attack_hits -= 1
        elif attack_unit["fighters"] != 0:
            attack_unit["fighters"] -= 1
            attack_hits -= 1
        elif attack_unit["bombers"] != 0:
            attack_unit["bombers"] -= 1
            attack_hits -= 1
        else:
            break

    while defend_hits != 0:
        if defend_unit["infantry"] != 0:
            defend_unit["infantry"] -= 1
            defend_hits -= 1
        elif defend_unit["artillery"] != 0:
            defend_unit["artillery"] -= 1
            defend_hits -= 1
        elif defend_unit["tanks"] != 0:
            defend_unit["tanks"] -= 1
            defend_hits -= 1
        elif defend_unit["fighters"] != 0:
            defend_unit["fighters"] -= 1
            defend_hits -= 1
        elif defend_unit["bombers"] != 0:
            defend_unit["bombers"] -= 1
            defend_hits -= 1
        else:
            break


def run():
    while (
        attack_unit["infantry"]
        + attack_unit["artillery"]
        + attack_unit["tanks"]
        + attack_unit["fighters"]
        + attack_unit["bombers"]
        != 0
        and defend_unit["infantry"]
        + defend_unit["artillery"]
        + defend_unit["tanks"]
        + defend_unit["fighters"]
        + defend_unit["bombers"]
        != 0
    ):
        take_losses()
        # print("\n")
        # print("Attackers hit:", compute_attack_hits())
        # print("Defenders hit:", compute_defend_hits())
        # print("\n")
        # print("Attackers remaining:")
        # print("Infantry:", attack_unit["infantry"])
        # print("Artillery:", attack_unit["artillery"])
        # print("Tanks:", attack_unit["tanks"])
        # print("Fighters:", attack_unit["fighters"])
        # print("Bombers:", attack_unit["bombers"])
        # print("\n")
        # print("Defenders remaining:")
        # print("Infantry:", defend_unit["infantry"])
        # print("Artillery:", defend_unit["artillery"])
        # print("Tanks:", defend_unit["tanks"])
        # print("Fighters:", defend_unit["fighters"])
        # print("Bombers:", defend_unit["bombers"])


attack_wins = 0
defend_wins = 0
for i in range(1000):
    run()
    if (
        attack_unit["infantry"] == 0
        and attack_unit["artillery"] == 0
        and attack_unit["tanks"] == 0
        and attack_unit["fighters"] == 0
        and attack_unit["bombers"] == 0
    ):
        defend_wins += 1
    elif (
        defend_unit["infantry"] == 0
        and defend_unit["artillery"] == 0
        and defend_unit["tanks"] == 0
        and defend_unit["fighters"] == 0
        and defend_unit["bombers"] == 0
    ):
        attack_wins += 1

    print(attack_wins, defend_wins, end="\r")

print("\n")
