import random


def gen_player_achievements() -> set[str]:
    achievements = {'First Blood', 'Sharpshooter', 'Survivor', 'Explorer',
                    'Master Collector', 'Speed Runner', 'Puzzle Master',
                    'Team Player', 'Stealth Expert', 'Boss Slayer',
                    'World Savior', 'Legendary Hero', 'Ultimate Champion',
                    'Secret Finder', 'Completionist'}
    temp = []
    total_achievements = random.randint(5, 10)
    for i in range(total_achievements):
        selected_achievement = random.choice(tuple(achievements))
        temp.append(selected_achievement)
    player_achievements = set(temp)
    return player_achievements


def main() -> None:
    print("=== Achievement Tracker System ===")
    alice = gen_player_achievements()
    bob = gen_player_achievements()
    Charlie = gen_player_achievements()
    Dylan = gen_player_achievements()
    print(f'Player Alice: {alice}')
    print(f'Player Bob: {bob}')
    print(f'Player Charlie: {Charlie}')
    print(f'Player Dylan: {Dylan}')
    all_achievements = set.union(alice, bob, Charlie, Dylan)
    print(f'All distinct achievements: {all_achievements}\n')
    Common_achievements = set.intersection(alice, bob, Charlie, Dylan)
    print(f'Common achievements: {Common_achievements}\n')
    print(f'Only Alice has: {set.difference(alice, bob, Charlie, Dylan)}')
    print(f'Only Bob has: {set.difference(bob, alice, Charlie, Dylan)}')
    print(f'Only Charlie has: {set.difference(Charlie, alice, bob, Dylan)}')
    print(f'Only Dylan has: {set.difference(Dylan, alice, bob, Charlie)}\n')
    print(f'Alice is missing: {set.difference(all_achievements, alice)}')
    print(f'Bob is missing: {set.difference(all_achievements, bob)}')
    print(f'Charlie is missing: {set.difference(all_achievements, Charlie)}')
    print(f'Dylan is missing: {set.difference(all_achievements, Dylan)}')


if __name__ == "__main__":
    main()
