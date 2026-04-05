from ex0 import AquaFactory, FlameFactory
from ex0.AbstractCreature import Creature
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import NormalStrategy, AggressiveStrategy, DefensiveStrategy
from ex2.AbstractBattleStrategy import BattleStrategy


def battle(opponents: list[tuple[Creature, BattleStrategy]]) -> None:
    print("*"*3 + " Tournament " + "*"*3)
    print(f"{len(opponents)} opponents involved\n")
    if len(opponents) <= 1:
        print("Battle error, aborting tournament: at leat 2 opponents are "
              "required!")
        return
    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            print("\n* Battle *")
            print(opponents[i][0].describe())
            print(" vs.")
            print(opponents[j][0].describe())
            print(" now fight!")
            try:
                opponent_a_result = opponents[i][1].act(opponents[i][0])
                opponent_b_result = opponents[j][1].act(opponents[j][0])
                print(opponent_a_result)
                print(opponent_b_result)
            except Exception as e:
                print(f"Battle Error, aborting tournament: {e}")
                return


if __name__ == "__main__":

    aqua_fac = AquaFactory()
    flame_fac = FlameFactory()
    heal_fac = HealingCreatureFactory()
    transform_fac = TransformCreatureFactory()

    print("Tournament 0 (Basic)")
    battle([(aqua_fac.create_base(), NormalStrategy()),
            (heal_fac.create_base(), DefensiveStrategy())])

    print("\nTournament 1 (error)")
    battle([(flame_fac.create_base(), AggressiveStrategy()),
            (heal_fac.create_base(), DefensiveStrategy())])

    print("\nTournament 2 (multiple)")
    battle([(aqua_fac.create_base(), NormalStrategy()),
            (heal_fac.create_base(), DefensiveStrategy()),
            (transform_fac.create_base(), AggressiveStrategy())])
