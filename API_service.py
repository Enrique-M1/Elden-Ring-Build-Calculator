import mariadb  # the database
import asyncio

from _shared.DBSettings import Settings
from hypercorn.config import Config
from hypercorn.asyncio import serve
from fastapi import FastAPI
from starlette.responses import RedirectResponse

from mariadb_database_setup import DBUSER
from models.stats import Stats
from models.armor import Armor
from models.character import Character
from models.fullbuild import FullBuild

# https://fastapi.tiangolo.com/
app = FastAPI(title="Elden Ring API")  # The server name

# Database Variables
DB_USER = Settings.getDBUsername()
DB_PASS = Settings.getDBPassword()


# This is the default setup for servers. If port 3306 is already full, there may be a password or a different
# username you need to substitute this for.
mariadb_con = mariadb.connect(
    user=DB_USER,
    password=DB_PASS,
    host="127.0.0.1",
    port=3306,
    database="Elden-Build-Info",
)
cur = mariadb_con.cursor()


@app.get('/', include_in_schema=False)
def get_default_page():
    return RedirectResponse(url='/docs')


# Armor
def get_armor_from_db(stats: Stats):
    helmet = get_helmet_from_db(stats)
    chestpiece = get_chest_from_db(stats)
    gauntlet = get_gauntlet_from_db(stats)
    leg = get_leg_from_db(stats)
    armor = Armor(helmet=helmet, chestpiece=chestpiece, gauntlet=gauntlet, legs=leg)

    return armor


# Helmet
def get_helmet_from_db(stats: Stats):
    query: str = ''
    match stats.build_type:
        case 'strength':
            query = get_strength_helm_query()
        case 'magic':
            query = get_magic_helm_query()
        case 'incantation':
            query = get_incantation_helm_query()
        case 'dexterity':
            query = get_dexterity_helm_query()
        case 'arcane':
            query = get_arcane_helm_query()

    cur.execute(query)
    helmets = cur.fetchall()
    helmet_name: str = ''
    max_total: float = 0.0

    for helmet in helmets:
        if float(helmet[1]) > max_total:
            helmet_name = helmet[0]
            max_total = helmet[1]

    return helmet_name

# Getting the helmet for strength table
def get_strength_helm_query():
    query: str = """
        SELECT `Name`, ROUND((Physical_Def + Magic_Def + Fire_Def + Lightning_Def + Holy_Def), 2) AS Total
        FROM helmets;
    """

    return query


# Getting the magic helmet table
def get_magic_helm_query():
    query: str = """
        SELECT `Name`, ROUND(Magic_Def, 2) AS Total
        FROM helmets;
    """

    return query


# Getting the incantation helmet from the table
def get_incantation_helm_query():
    query: str = """
            SELECT `Name`, ROUND(Holy_Def, 2) AS Total
            FROM helmets;
        """

    return query


# Getting the dexterity helmet from the table
def get_dexterity_helm_query():
    query: str = """
                SELECT `Name`, ROUND(Physical_Def + Fire_Def + Lightning_Def, 2) AS Total
                FROM helmets;
            """

    return query


# Getting the arcane helmet from the table
def get_arcane_helm_query():
    query: str = """
                SELECT `Name`, ROUND(Lightning_Def + Holy_Def, 2) AS Total
                FROM helmets;
                """

    return query


# Chestpiece
def get_chest_from_db(stats: Stats):
    query: str = ''
    match stats.build_type:
        case 'strength':
            query = get_strength_chest_query()
        case 'magic':
            query = get_magic_chest_query()
        case 'incantation':
            query = get_incantation_chest_query()
        case 'dexterity':
            query = get_dexterity_chest_query()
        case 'arcane':
            query = get_arcane_chest_query()

    cur.execute(query)
    chestpieces = cur.fetchall()
    chestpiece_name: str = ''
    max_total: float = 0.0

    for chest in chestpieces:
        if float(chest[1]) > max_total:
            chestpiece_name = chest[0]
            max_total = chest[1]

    return chestpiece_name


# Getting the strength chestpiece from the table
def get_strength_chest_query():
    query: str = """
            SELECT `Name` , ROUND((Physical_Def + Magic_Def + Fire_Def + Lightning_Def + Holy_Def), 2) AS Total
            FROM `chestpieces`;
        """

    return query


# Getting the magic chestpiece from the table
def get_magic_chest_query():
    query: str = """
        SELECT `Name` , ROUND(Magic_Def, 2) AS Total
            FROM `chestpieces`;
    """

    return query


# Getting the incantation chestpiece from the table
def get_incantation_chest_query():
    query: str = """
            SELECT `Name` , ROUND(Holy_Def, 2) AS Total
            FROM `chestpieces`;
        """

    return query


# Getting the dexterity chestpiece from the table
def get_dexterity_chest_query():
    query: str = """
                SELECT `Name` , ROUND(Physical_Def + Fire_Def + Lightning_Def, 2) AS Total
                FROM `chestpieces`;
            """

    return query


# Getting the arcane chestpiece from the table
def get_arcane_chest_query():
    query: str = """
                SELECT `Name` , ROUND(Lightning_Def + Holy_Def, 2) AS Total
                FROM `chestpieces`;
                """

    return query


# Gauntlets
def get_gauntlet_from_db(stats: Stats):
    query: str = ''
    match stats.build_type:
        case 'strength':
            query = get_strength_gauntlet_query()
        case 'magic':
            query = get_magic_gauntlet_query()
        case 'incantation':
            query = get_incantation_gauntlet_query()
        case 'dexterity':
            query = get_dexterity_gauntlet_query()
        case 'arcane':
            query = get_arcane_gauntlet_query()

    cur.execute(query)
    gauntlets = cur.fetchall()
    gauntlet_name: str = ''
    max_total: float = 0.0

    for gauntlet in gauntlets:
        if float(gauntlet[1]) > max_total:
            gauntlet_name = gauntlet[0]
            max_total = gauntlet[1]

    return gauntlet_name


# Getting the strength gauntlet from the table
def get_strength_gauntlet_query():
    query: str = """
                SELECT `Name` , ROUND((Physical_Def + Magic_Def + Fire_Def + Lightning_Def + Holy_Def), 2) AS Total
                FROM `gauntlets`;
            """

    return query


# Getting the magic gauntlet from the table
def get_magic_gauntlet_query():
    query: str = """
                    SELECT `Name` , ROUND(Magic_Def, 2) AS Total
                    FROM `gauntlets`;
                """

    return query


# Getting the incantation gauntlet from the table
def get_incantation_gauntlet_query():
    query: str = """
            SELECT `Name` , ROUND(Holy_Def, 2) AS Total
                FROM `gauntlets`;
        """

    return query


# Getting the dexterity gauntlet from the table
def get_dexterity_gauntlet_query():
    query: str = """
                SELECT `Name` , ROUND(Physical_Def + Fire_Def + Lightning_Def, 2) AS Total
                    FROM `gauntlets`;
            """

    return query


# Getting the arcane gauntlet from the table
def get_arcane_gauntlet_query():
    query: str = """
                    SELECT `Name` , ROUND(Lightning_Def + Holy_Def, 2) AS Total
                        FROM `gauntlets`;
                """

    return query


# Leg Armor
def get_leg_from_db(stats: Stats):
    query: str = ''
    match stats.build_type:
        case 'strength':
            query = get_strength_leg_query()
        case 'magic':
            query = get_magic_leg_query()
        case 'incantation':
            query = get_incantation_leg_query()
        case 'dexterity':
            query = get_dexterity_leg_query()
        case 'arcane':
            query = get_arcane_leg_query()

    cur.execute(query)
    legs = cur.fetchall()
    leg_name: str = ''
    max_total: float = 0.0

    for leg in legs:
        if float(leg[1]) > max_total:
            leg_name = leg[0]
            max_total = leg[1]

    return leg_name


# Getting the strength leg armor from the table
def get_strength_leg_query():
    query: str = """
                    SELECT `Name` , ROUND((Physical_Def + Magic_Def + Fire_Def + Lightning_Def + Holy_Def), 2) AS Total
                    FROM `legs`;
                """

    return query


# Getting the magic leg armor from the table
def get_magic_leg_query():
    query: str = """
                        SELECT `Name` , ROUND(Magic_Def, 2) AS Total
                        FROM `legs`;
                    """

    return query


# Getting the incantation leg armor from the table
def get_incantation_leg_query():
    query: str = """
            SELECT `Name` , ROUND(Holy_Def, 2) AS Total
                FROM `legs`;
        """

    return query


# Getting the dexterity leg armor from the table
def get_dexterity_leg_query():
    query: str = """
                SELECT `Name` , ROUND(Physical_Def + Fire_Def + Lightning_Def, 2) AS Total
                    FROM `legs`;
            """

    return query


# Getting the arcane leg armor from the table
def get_arcane_leg_query():
    query: str = """
                    SELECT `Name` , ROUND(Lightning_Def + Holy_Def, 2) AS Total
                        FROM `legs`;
                """

    return query


# Character Data
def get_character_stats_from_db(stats: Stats):
    query: str = ''
    match stats.build_type:
        case 'strength':
            query = get_strength_query(stats.class_name)
        case 'magic':
            query = get_magic_query(stats.class_name)
        case 'arcane':
            query = get_arcane_query(stats.class_name)
        case 'dexterity':
            query = get_dexterity_query(stats.class_name)
        case 'incantation':
            query = get_incantation_query(stats.class_name)

    cur.execute(query)
    results = cur.fetchall()
    character = ''
    for result in results:
        character = Character(S_Class=stats.class_name, Level=result[0], Vigor=result[1],
                              Mind=result[2], Endurance=result[3], Strength=result[4],
                              Dexterity=result[5], Intelligence=result[6], Faith=result[7],
                              Arcane=result[8], Remaining=result[9])

    return character


# Strength Character class
def get_strength_query(class_name: str):
    query: str = f"""
        SELECT
    150 AS MaxLevel,
    40 AS MaxVigor,
    Mind,
    40 AS MaxEndurance,
    60 AS MaxStrength,
    40 AS MaxDexterity,
    Intelligence,
    Faith,
    Arcane,
    (150 - (60 - Strength) - `Level` - (40 - Vigor) - (40 - Endurance) - (40 - Dexterity)) AS RemainingPoints
FROM characters
WHERE Class = '{class_name}';
    """

    return query


# Mage Character class
def get_magic_query(class_name: str):
    query: str = f"""
        SELECT 
    150 AS MaxLevel,
    30 AS MaxVigor,
    40 AS MaxMind,
    Endurance,
    Strength,
    30 AS MaxDexterity,
    60 AS MaxIntelligence,
    30 AS MaxFaith,
    Arcane,
    (150 - (30 - Vigor) - `Level` - (40 - Mind) - (30 - Dexterity) - (60 - Intelligence) - (30 - Faith)) AS RemainingPoints
FROM characters
WHERE Class = '{class_name}';
    """

    return query


# Blood loss Character class
def get_arcane_query(class_name: str):
    query: str = f"""
    SELECT 
    150 AS MaxLevel,
    40 AS MaxVigor,
    Mind,
    40 AS MaxEndurance,
    18 As Strength,
    30 AS MaxDexterity,
    Intelligence,
    Faith,
    60 AS MaxArcane,
    (150 - (40 - Vigor) - `Level` - (40 - Endurance) - (18 - Strength) - (30 - Dexterity) - (60 - Arcane)) AS RemainingPoints
FROM characters
WHERE Class = '{class_name}';
    """

    return query


# Speed Character class
def get_dexterity_query(class_name: str):
    query = f"""
    SELECT 
    150 AS MaxLevel,
    40 AS MaxVigor,
    Mind,
    40 AS MaxEndurance,
    19 As Strength,
    60 AS MaxDexterity,
    Intelligence,
    Faith,
    30 AS MaxArcane,
    (150 - (40 - Vigor) - `Level` - (40 - Endurance) - (19 - Strength) - (60 - Dexterity) - (30 - Arcane))
    AS RemainingPoints
    FROM characters
    WHERE Class = '{class_name}';
    """

    return query


# Incantation Character class
def get_incantation_query(class_name: str):
    query: str = f"""
        SELECT 
    150 AS MaxLevel,
    40 AS MaxVigor,
    30 AS MaxMind,
    20 AS MaxEndurance,
    25 As Strength,
    Dexterity,
    Intelligence,
    60 AS MaxFaith,
    20 AS MaxArcane,
    (150 - (40 - Vigor) - `Level` - (30 - Mind) - (20 - Endurance) - (25 - Strength) - (60 - Faith) - (20 - Arcane)) 
    AS RemainingPoints
    FROM characters
    WHERE Class = '{class_name}';
    """

    return query


# Saving the build to the database
def save_build_to_db(save_build_name: str, fb: FullBuild):
    insert_stmt: str = f"INSERT INTO Saved_Builds(Name, Class, Level, Vigor, Mind, Endurance, Strength," \
                       f"Dexterity, Intelligence, Faith, Arcane, Remaining, Helmet, Chestpiece, Gauntlets, Legs) VALUES" \
        f"('{save_build_name}', '{fb.S_Class}', {fb.Level}, {fb.Vigor}, " \
         f"{fb.Mind}, {fb.Endurance}, {fb.Strength}, " \
         f"{fb.Dexterity}, {fb.Intelligence}, {fb.Faith}, {fb.Arcane}, {fb.Remaining}, " \
         f"'{fb.Helmet}', '{fb.Chestpiece}', '{fb.Gauntlet}', '{fb.Legs}')"

    cur.execute(insert_stmt)
    mariadb_con.commit()


# Getting the Full build
def get_full_build_from_db(stats: Stats):
    ch = get_character_stats_from_db(stats)
    ar = get_armor_from_db(stats)
    fb = FullBuild(S_Class=ch.S_Class, Level=ch.Level, Vigor=ch.Vigor, Mind=ch.Mind,
                   Endurance=ch.Endurance, Strength=ch.Strength, Dexterity=ch.Dexterity,
                   Intelligence=ch.Intelligence, Faith=ch.Faith, Arcane=ch.Arcane,
                   Remaining=ch.Remaining, Helmet=ar.helmet, Chestpiece=ar.chestpiece,
                   Gauntlet=ar.gauntlet, Legs=ar.legs)
    return fb


# Getting the saved builds from the database
def get_builds_from_db(table_name: str):
    query: str = f'SELECT * FROM {table_name};'

    cur.execute(query)
    results = cur.fetchall()

    return results


# API endpoint for the character
@app.post('/api/character')
def get_stats(stats: Stats):
    return get_character_stats_from_db(stats)


# API endpoint for the armor call
@app.post('/api/armor')
def get_armor(stats: Stats):
    return get_armor_from_db(stats)


# API endpoint for the full build call
@app.post('/api/full-build')
def get_full_build(stats: Stats):
    fb = get_full_build_from_db(stats)
    if stats.save_build_name != '':
        save_build_to_db(stats.save_build_name, fb)
    return fb


# API endpoint for the saved builds call
@app.get('/api/builds')
def get_saved_builds():
    return get_builds_from_db('saved_builds')


if __name__ == '__main__':
    config = Config()
    config.bind = ['localhost:40000']

    asyncio.run(serve(app, config))  # Runs server and addresses the calls as entered
