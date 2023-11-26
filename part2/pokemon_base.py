from abc import ABC, abstractmethod
from pokemon_enums import PokemonState, PokemonType
from constants import MAX_HEALTH


class Pokemon(ABC):  # TODO: Rendez la classe Pokemon abstraite
    # TODO: Sauvegarder les paramètres dans des attributs privés (préfixés par __)
    # Initialisez l'attribut __health à MAX_HEALTH, l'attribut __state à PokemonState.NORMAL et l'attribut
    # __evolved à False.
    __health = MAX_HEALTH
    __state = PokemonState.NORMAL
    __state_counter = 0
    __evolved = False

    def __init__(self, name: str, attack: int, defense: int, type: PokemonType) -> None:
        self.__name = name
        self.__attack = attack
        self.__defense = defense
        self.__type = type

    # TODO: Ajouter "getters" pour les attributs privés en utilisant les décorateurs @property
    # Voici les noms des getters à utiliser: name, attack, defense, type, health, state, state_counter et evolved
    @property
    def name(self):
        return self.__name

    @property
    def attack(self):
        return self.__attack

    @property
    def defense(self):
        return self.__defense

    @property
    def type(self):
        return self.__type

    @property
    def health(self):
        return self.__health

    @property
    def state(self):
        return self.__state

    @property
    def state_counter(self):
        return self.__state_counter

    @property
    def evolved(self):
        return self.__evolved

    # Pour les setters suivant, vous devez vous assurer d'utiliser le décorateur "@nom_de_l_attribut.setter"
    # pour chaque attribut, ainsi que de valider les valeurs reçues avant de les affecter à l'attribut privé.

    # TODO: Ajouter le "setter" name, s'assurant de mettre à jour l'attribut uniquement si le nom n'est pas vide

    @name.setter
    def name(self, name):
        if not name == "":
            self.__name = name

    # TODO: Ajouter le "setter" attack, s'assurant de mettre à jour l'attribut uniquement si la valeur est positive
    @attack.setter
    def attack(self, attack):
        if not attack < 0:
            self.__attack = attack
        else:
            self.__attack = 0

    # TODO: Ajouter le "setter" defense, s'assurant de mettre à jour l'attribut uniquement si la valeur est positive
    @defense.setter
    def defense(self, defense):
        if not defense < 0:
            self.__defense = defense
        else:
            self.__defense = 0

    # TODO: Ajouter le "setter" state, s'assurant de mettre à jour l'attribut uniquement si la valeur est un state valide
    @state.setter
    def state(self, state):
        if isinstance(state, PokemonState):
            self.__state = state

    # TODO: Ajouter le "setter" state_counter, s'assurant de mettre à jour l'attribut uniquement si la valeur est positive
    @state_counter.setter
    def state_counter(self, state_counter):
        if not state_counter < 0:
            self.__state_counter = state_counter
        else:
            self.__state_counter = 0

    # Pour les méthodes abstraites suivantes, vous devez vous assurer d'utiliser le décorateur "@abstractmethod".

    # TODO: Déclarer la signature de la méthode abstraite "get_attack_multiplier", qui prend en paramètre le type
    # du Pokémon attaqué (PokemonType) et qui retourne un nombre à virgule (float) représentant le multiplicateur
    @abstractmethod
    def get_attack_multiplier(type: PokemonType) -> float:
        pass

    # TODO: Déclarer la signature de la méthode abstraite "generate_random_induced_state", qui ne prend aucun
    # paramètre et qui retourne un tuple contenant un état (PokemonState) et un compteur d'état (int).
    @abstractmethod
    def generate_random_induced_state() -> (PokemonType, int):
        pass

    # TODO: Déclarer la signature de la méthode abstraite "get_signature_sound", qui ne prend aucun paramètre et
    # qui retourne un string représentant le son caractéristique du Pokémon.
    @abstractmethod
    def get_signature_sound() -> str:
        pass

    # TODO: Déclarer la signature de la méthode abstraite "evolve", qui ne prend aucun paramètre et qui ne retourne
    # rien.
    @abstractmethod
    def evolve():
        pass

    # TODO: Implémenter la méthode non-abstraite decrement_state_counter, qui décrémente l'attribut __state_counter de 1, à moins que
    # sa valeur soit déjà à 0.
    def decrement_state_counter(self):
        stateCounter = self.state_counter - 1
        self.state_counter = stateCounter

    # TODO: Implémenter la méthode non-abstraite "is_knocked_out", qui ne prend aucun paramètre et qui retourne un booléen indiquant si le Pokémon est
    # KO, c'est-à-dire si son attribut __health est à 0.)
    def is_knocked_out(self):
        return self.__health == 0

    # TODO: Implémenter la méthode non-abstraite "heal" qui ne prend aucun paramètre et qui ne retourne rien. Cette méthode
    # met à jour l'attribut __health à MAX_HEALTH.
    def heal(self):
        self.__health = MAX_HEALTH

    # TODO: Implémenter la méthode spéciale __str__ qui retourne une chaîne de caractères décrivant le Pokémon, par
    # exemple: "Pikachu est de type ELECTRIC. Il a 112 points d'attaque et 96 points de défense."
    def __str__(self) -> str:
        return f"{self.name} est de type {self.type}. Il a {self.attack} points d'attaque et {self.defense} points de défense."

    # TODO: Implémenter la méthode spéciale __add__ qui surcharge l'opérateur "+", qui prend en paramètre un nombre
    # entier (int) représentant les points de vie à ajouter au Pokémon et qui ne retourne rien. Cette méthode doit
    # mettre à jour l'attribut __health en ajoutant les points de vie reçus à la santé actuelle du Pokémon. Si les
    # points de vie sont négatifs, ne faites rien.
    def __add__(self, health: int) -> None:
        if not health < 0:
            updateHealth = self.health + health
            if updateHealth > MAX_HEALTH:
                updateHealth = MAX_HEALTH
            self.__health = updateHealth

    # TODO: Implémenter la méthode spéciale __sub__ qui surcharge l'opérateur "-", qui prend en paramètre un nombre
    # entier (int) représentant les dégâts subis par le Pokémon et qui ne retourne rien. Cette méthode doit mettre à
    # jour l'attribut __health en soustrayant les dégâts reçus à la santé actuelle du Pokémon. Si les dégâts sont
    # négatifs, ne faites rien.
    def __sub__(self, damage: int) -> None:
        if not damage < 0:
            updateHealth = self.health - damage
            if updateHealth < 0:
                updateHealth = 0
            self.__health = updateHealth
