#!python3
import random
import yaml

attack_unit = {}
defend_unit = {}
promoted_infantry = 0


def get_units():
    global attack_unit, defend_unit, promoted_infantry

    with open("aaa_units.yaml", "r") as f:
        units = yaml.full_load(f)

    attack_unit = units["attack_unit"]
    defend_unit = units["defend_unit"]
    promoted_infantry = 0
    infantry = attack_unit["infantry"]
    while promoted_infantry < attack_unit["artillery"] and infantry > 0:
        promoted_infantry += 1




def roll_dice(num):
    rand = random.randint(1, 6)
    if rand <= num:
        return 1
    else:
        return 0


attack_wins = 0
defend_wins = 0
for i in range(1000):
    get_units()
    while (
        attack_unit["infantry"]
        + promoted_infantry
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

        while attack_hits != 0:
            if attack_unit["infantry"] != 0:
                attack_unit["infantry"] -= 1
                attack_hits -= 1
            elif promoted_infantry != 0:
                promoted_infantry -= 1
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
    if (
        attack_unit["infantry"] == 0
        and promoted_infantry == 0
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

print(f"""
        Attacker winrate: {attack_wins/10}%
        Defender winrate: {defend_wins/10}%
        """)