from Api.extensions import database

from Api.models.Pokemon import BasePokemon, GamePokemon, GameEntities
from Api.models.Items import PokemonBag, Garment
from Api.models.User import Game

from Api.Enums.BagSize import BagSizeEnum
from Api.Utils.utils import serialize_move_for_battle
from Api.Utils.utils import resolve_stat


# --------------------------------------------------
# BASE POKEMON
# --------------------------------------------------

def list_base_pokemon():
    result = []

    for p in BasePokemon.query.all():
        result.append({
            "id": p.id,
            "name": p.name,

            "BaseHealth": p.baseHealth,
            "Will": p.will,
            "Logic": p.logic,
            "Instinct": p.instinct,
            "Primal": p.primal,

            "PrimaryType": p.primaryType.name if p.primaryType else None,
            "SecondaryType": p.secondaryType.name if p.secondaryType else None,

            # Stats
            "Strength": p.strength,
            "StrengthPotential": p.strengthPotential,
            "Dexterity": p.dexterity,
            "DexterityPotential": p.dexterityPotential,
            "Vitality": p.vitality,
            "VitalityPotential": p.vitalityPotential,
            "Special": p.special,
            "SpecialPotential": p.specialPotential,
            "Insight": p.insight,
            "InsightPotential": p.insightPotential,

            # Skills
            "Fight": p.fight,
            "Survival": p.survival,
            "Contest": p.contest,
            "Brawl": p.brawl,
            "Channel": p.channel,
            "Clash": p.clash,
            "Evasion": p.evasion,
            "Alert": p.alert,
            "Athletic": p.athletic,
            "NatureStat": p.natureStat,
            "Stealth": p.stealth,
            "Allure": p.allure,
            "Etiquette": p.etiquette,
            "Intimidate": p.intimidate,
            "Perform": p.perform,

            "LearnableMoves": [
                serialize_move_for_battle(lm.move)
                for lm in p.learnable_moves
            ]
        })

    return result


def create_base_pokemon(raw):
    strength = resolve_stat(raw.get("Strength"), raw.get("StrengthPotential"))
    dexterity = resolve_stat(raw.get("Dexterity"), raw.get("DexterityPotential"))
    vitality = resolve_stat(raw.get("Vitality"), raw.get("VitalityPotential"))
    insight = resolve_stat(raw.get("Insight"), raw.get("InsightPotential"))
    special = resolve_stat(raw.get("Special"), raw.get("SpecialPotential"))

    base = BasePokemon(
        name=raw.get("Name"),
        evolution=raw.get("Evolution"),
        preEvolution=raw.get("PreEvolution"),
        baseHealth=raw.get("BaseHealth"),
        primaryType=raw.get("PrimaryType"),
        secondaryType=raw.get("SecondaryType"),

        strength=strength,
        strengthPotential=raw.get("StrengthPotential"),
        dexterity=dexterity,
        dexterityPotential=raw.get("DexterityPotential"),
        vitality=vitality,
        vitalityPotential=raw.get("VitalityPotential"),
        special=special,
        specialPotential=raw.get("SpecialPotential"),
        insight=insight,
        insightPotential=raw.get("InsightPotential"),

        fight=raw.get("Fight"),
        survival=raw.get("Survival"),
        contest=raw.get("Contest"),
        brawl=raw.get("Brawl"),
        channel=raw.get("Channel"),
        clash=raw.get("Clash"),
        evasion=raw.get("Evasion"),
        alert=raw.get("Alert"),
        athletic=raw.get("Atheletic"),
        natureStat=raw.get("NatureStat"),
        stealth=raw.get("Stealth"),
        allure=raw.get("Allure"),
        etiquette=raw.get("Etiquette"),
        intimidate=raw.get("Intimidate"),
        perform=raw.get("Perform"),
    )

    database.session.add(base)
    database.session.commit()
    return base


# --------------------------------------------------
# GAME POKEMON
# --------------------------------------------------

def create_game_pokemon(raw):
    game = Game.query.filter_by(id=raw.get("gameId")).first()
    if not game:
        return None, "Game not found"

    base = BasePokemon.query.get(raw.get("basePokemonId"))
    if not base:
        return None, "BasePokemon not found"

    pokemon = GamePokemon(
        basePokemonId=base.id,
        name=raw.get("name"),
        level=raw.get("level"),
        gender=raw.get("gender"),
        age=raw.get("age"),
        natureId=raw.get("natureId"),
        abilityId=raw.get("abilityId"),
        status=raw.get("status"),
        itemId=raw.get("itemId"),
        isNpc=raw.get("isNpc", False),
        experiencePoints=raw.get("experiencePoints", 0),
        playerColor=raw.get("playerColor"),
        Guid=raw.get("Guid"),

        baseHealth=base.baseHealth,
        health=base.baseHealth + base.vitality,
        lethalHealth=0,

        will=raw.get("will"),
        logic=raw.get("logic"),
        instinct=raw.get("instinct"),
        primal=raw.get("primal"),

        primaryType=base.primaryType,
        secondaryType=base.secondaryType,

        strength=base.strength,
        strengthPotential=base.strengthPotential,
        dexterity=base.dexterity,
        dexterityPotential=base.dexterityPotential,
        vitality=base.vitality,
        vitalityPotential=base.vitalityPotential,
        special=base.special,
        specialPotential=base.specialPotential,
        insight=base.insight,
        insightPotential=base.insightPotential,

        fight=base.fight,
        survival=base.survival,
        contest=base.contest,
        brawl=base.brawl,
        channel=base.channel,
        clash=base.clash,
        evasion=base.evasion,
        alert=base.alert,
        athletic=base.athletic,
        natureStat=base.natureStat,
        stealth=base.stealth,
        allure=base.allure,
        etiquette=base.etiquette,
        intimidate=base.intimidate,
        perform=base.perform,
    )

    database.session.add(pokemon)
    database.session.commit()

    # Garments
    for gid in raw.get("garments", []):
        garment = Garment.query.get(gid)
        if garment:
            pokemon.garments.append(garment)

    # Bag
    database.session.add(PokemonBag(
        pokemonId=pokemon.id,
        bagSize=BagSizeEnum.size5
    ))

    # Game entity link
    entity = GameEntities(gameId=game.id, pokemonId=pokemon.id)
    database.session.add(entity)

    database.session.commit()

    return pokemon, entity


# --------------------------------------------------
# CHARACTER DATA
# --------------------------------------------------

def pull_character_data(gameId, guid):
    pokemon = (
        database.session.query(GamePokemon)
        .join(GameEntities)
        .join(Game)
        .filter(Game.gameId == gameId)
        .filter(GamePokemon.Guid == guid)
        .first()
    )

    if not pokemon:
        return None

    base = pokemon.basePokemon

    def pick(a, b):
        return a if a is not None else b

    return {
        "GameId": gameId,
        "Guid": pokemon.Guid,
        "Name": pokemon.name,
        "Level": pokemon.level,
        "Gender": pokemon.gender,
        "Age": pokemon.age,
        "Nature": pokemon.nature,
        "Ability": pokemon.ability,

        "BaseHealth": pick(pokemon.baseHealth, base.baseHealth),
        "Will": pick(pokemon.will, base.will),
        "Logic": pick(pokemon.logic, base.logic),
        "Instinct": pick(pokemon.instinct, base.instinct),
        "Primal": pick(pokemon.primal, base.primal),

        "PrimaryType": pick(pokemon.primaryType, base.primaryType),
        "SecondaryType": pick(pokemon.secondaryType, base.secondaryType),

        "Strength": pick(pokemon.strength, base.strength),
        "StrengthPotential": pick(pokemon.strengthPotential, base.strengthPotential),
        "Dexterity": pick(pokemon.dexterity, base.dexterity),
        "DexterityPotential": pick(pokemon.dexterityPotential, base.dexterityPotential),
        "Vitality": pick(pokemon.vitality, base.vitality),
        "VitalityPotential": pick(pokemon.vitalityPotential, base.vitalityPotential),
        "Special": pick(pokemon.special, base.special),
        "SpecialPotential": pick(pokemon.specialPotential, base.specialPotential),
        "Insight": pick(pokemon.insight, base.insight),
        "InsightPotential": pick(pokemon.insightPotential, base.insightPotential),

        "ExperiencePoints": pokemon.experiencePoints,
        "IsNpc": pokemon.isNpc,
        "PlayerColor": pokemon.playerColor,
    }
