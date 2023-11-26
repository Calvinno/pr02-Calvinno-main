from pokemon_types import PokemonFireType, PokemonWaterType, PokemonGrassType


class Squirtle(PokemonWaterType):  # TODO: Héritez de la classe PokemonWaterType
    # TODO: Créer un constructeur qui ne prend aucun paramètre et qui utilise le constructeur de la classe parent
    # en spécifiant le nom à "Squirtle", l'attaque à 48 et la défense à 65.
    def __init__(self) -> None:
        super().__init__("Squirtle", 48, 65)

    # TODO: "Override" la méthode "evolve". Cette méthode ne prend aucun paramètre et ne retourne rien. Elle change
    # le nom à "Wartortle", l'attaque à 63 et la défense à 80.
    def evolve(self):
        self.name = "Wartortle"
        self.attack = 63
        self.defense = 80

    # TODO: "Override" la méthode "get_signature_sound". Cette méthode ne prend aucun paramètre et retourne la
    # chaîne "Squirtle-squirtle".
    def get_signature_sound(self) -> str:
        return "Squirtle-squirtle"

    # TODO: Retirer cette ligne lorsque vous implémentez la classe


class Charmander(PokemonFireType):  # TODO: Héritez de la classe PokemonFireType
    # TODO: Créer un constructeur qui ne prend aucun paramètre et qui utilise le constructeur de la classe parent
    # en spécifiant le nom à "Charmander", l'attaque à 52 et la défense à 43.
    def __init__(self) -> None:
        super().__init__("Charmander", 52, 43)

    # TODO: "Override" la méthode "evolve". Cette méthode ne prend aucun paramètre et ne retourne rien. Elle change
    # le nom à "Charmeleon", l'attaque à 64 et la défense à 58.
    def evolve(self):
        self.name = "Charmeleon"
        self.attack = 64
        self.defense = 58

    # TODO: "Override" la méthode "get_signature_sound". Cette méthode ne prend aucun paramètre et retourne la
    # chaîne "Char-char".
    def get_signature_sound(self) -> str:
        return "Char-char"

    # TODO: Retirer cette ligne lorsque vous implémentez la classe


class Bulbasaur(PokemonGrassType):  # TODO: Héritez de la classe PokemonGrassType
    # TODO: Créer un constructeur qui ne prend aucun paramètre et qui utilise le constructeur de la classe parent
    # en spécifiant le nom à "Bulbasaur", l'attaque à 49 et la défense à 49.
    def __init__(self) -> None:
        super().__init__("Bulbasaur", 49, 49)

    # TODO: "Override" la méthode "evolve". Cette méthode ne prend aucun paramètre et ne retourne rien. Elle change
    # le nom à "Ivysaur", l'attaque à 62 et la défense à 63.
    def evolve(self):
        self.name = "Ivysaur"
        self.attack = 62
        self.defense = 63

    # TODO: "Override" la méthode "get_signature_sound". Cette méthode ne prend aucun paramètre et retourne la
    # chaîne "Bulba-bulba".
    def get_signature_sound(self) -> str:
        return "Bulba-bulba"

    # TODO: Retirer cette ligne lorsque vous implémentez la classe
