from character import Character
from spell import Fireball, IceLance, LightningBolt


def print_character(name, character):
    print(name)
    print("Класс:", character.character_class)
    print("Здоровье:", character.max_health)
    print("Урон:", character.damage)
    print("Защита:", character.defense)
    print("Мана:", character.mana)
    print()


def main():
    warrior = Character(16, 8, 14, 7, 6, 10, "warrior")
    mage = Character(7, 9, 10, 15, 18, 12, "mage")
    hunter = Character(10, 17, 11, 12, 9, 8, "hunter")

    mage.add_spell(Fireball())
    mage.add_spell(IceLance())
    mage.add_spell(LightningBolt())

    print_character("Воин", warrior)
    print_character("Маг", mage)
    print_character("Охотник", hunter)

    spell_damage = mage.cast_spell(0)
    print("Маг использует Fireball")
    print("Урон заклинания:", spell_damage)
    print("Маны осталось:", mage.mana)


if __name__ == "__main__":
    main()
