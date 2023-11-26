from pokemons import Charmander, Squirtle
from pokemon_arena import PokemonArena
from constants import MAIN_SEPARATOR

if __name__ == "__main__":
    # ======================
    # CRÉATION DES POKÉMONS
    # ======================

    # TODO: Créer une instance de Charmander et une instance de Squirtle.
    charmander = Charmander()
    squirtle = Squirtle()

    # ============================
    # LES PREMIÈRES IMPRESSIONS...
    # ============================

    # TODO: Afficher la description des deux pokémons en utilisant leur représentation textuelle.
    print(charmander)
    print(squirtle)
    # TODO: Afficher le cri de signature des deux pokémons.
    print(charmander.get_signature_sound())
    print(squirtle.get_signature_sound())
    # ================
    # ROUND 1: COMBAT!
    # ================
    print(MAIN_SEPARATOR)

    # TODO: Utiliser la méthode statique de PokemonArena pour faire combattre les deux pokémons (PokemonArena.fight(...)).
    PokemonArena.fight(charmander, squirtle)
    # ================================
    # LE PASSAGE CHEZ L'INFIRMIÈRE JOY
    # ================================
    print(MAIN_SEPARATOR)

    # TODO: Soigner les deux pokémons en utilisant leur méthode de soin.
    charmander.heal()
    squirtle.heal()
    # ============================
    # LA MÉTAMORPHOSE DES POKÉMONS
    # ============================
    print(MAIN_SEPARATOR)

    # TODO: Faire évoluer Charmander en Charmeleon et Squirtle en Wartortle.
    charmander.evolve()
    squirtle.evolve()
    # TODO: Afficher la description de Charmeleon et Wartortle.
    print(charmander)
    print(squirtle)
    # ===============
    # LE COMBAT FINAL
    # ===============
    print(MAIN_SEPARATOR)

    # TODO: Utiliser de nouveau PokemonArena pour faire combattre les deux pokémons.
    PokemonArena.fight(charmander, squirtle)
