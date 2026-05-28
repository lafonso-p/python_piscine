def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(
        artifacts, key=lambda artifact: artifact['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda mage: mage['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: f"* {spell} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    if not mages:
        return {'max_power': 0, 'min_power': 0, 'avg_power': 0.0}

    max_mage = max(mages, key=lambda mage: mage['power'])
    min_mage = min(mages, key=lambda mage: mage['power'])

    total_power = sum(map(lambda mage: mage['power'], mages))
    avg_power = round(total_power / len(mages), 2)

    return {
        'max_power': max_mage['power'],
        'min_power': min_mage['power'],
        'avg_power': avg_power
    }


def main():
    artifacts = [
        {'name': "Gabigol's Muque", 'power': 8100, 'type': 'magical'},
        {'name': 'Danilos Header', 'power': 9600, 'type': 'finalization'},
        {'name': 'Arrascas Cake', 'power': 3000, 'type': 'healing'}
    ]

    sorted_artifacts = artifact_sorter(artifacts)
    print("\n ==== Testing sorter ====")
    for item in sorted_artifacts:
        print(f"{item['name']} ({item['power']} power)")

    print()
    print("-"*40)
    print()

    mages = [
        {'name': "Zico", 'power': 100000, 'element': "free kicks"},
        {'name': "Arrascaeta", 'power': 7500, 'element': "Cakes"},
        {'name': "Bruno Henrique", 'power': 7450, 'element': "king of derbys"},
        {'name': "Joker Gerson", 'power': 500, 'element': "treason"}
    ]

    filtered_items = power_filter(mages, 8000)
    print(" ==== all mages registered ====")
    for mage in mages:
        print(f"{mage['name']} - a.k.a (element): {mage['element']}")
    print("\n ==== testing filter (power more than 8000) ====")
    for item in filtered_items:
        print(f"{item['name']} - power: {item['power']}")

    print()
    print("-"*40)
    print()

    spells = ["Cera", "Caatimba", "provocation"]

    transformed_spells = spell_transformer(spells)
    print(" ==== Testing spell transformer: ====")
    for spell in transformed_spells:
        print(spell)

    print()
    print("-"*40)
    print()

    mages_analized = mage_stats(mages)
    print("==== Stats of mages ====")
    print(f"most powerful: {mages_analized['max_power']}\n"
          f"least powerful: {mages_analized['min_power']}\n"
          f"average power: {mages_analized['avg_power']}")


if __name__ == "__main__":
    main()
