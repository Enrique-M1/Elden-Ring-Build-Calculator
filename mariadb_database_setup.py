import mariadb  # This is the database that holds all of the information regarding the Characters and Armor
from _shared.DBSettings import Settings


DBUSER = Settings.getDBUsername()
DBPASS = Settings.getDBPassword()

mariadb_con = mariadb.connect(
    user=DBUSER,
    password=DBPASS,
    host="127.0.0.1",
    port=3306,
    database="Elden-Build-Info",
)
cur = mariadb_con.cursor()


# Creating the database
def create_database(db_name: str):
    mariadb_connect = mariadb.connect(
        user=DBUSER,
        password=DBPASS,
        host="127.0.0.1",
        port=3306
    )

    cursor = mariadb_connect.cursor()
    query = f"CREATE DATABASE `{db_name}`;"
    cursor.execute(query)
    print(cursor.statement)

    cursor.close()
    mariadb_connect.close()

# Printing the table that is given as argument
def print_from_table(table_name: str):
    query: str = f'SELECT * FROM {table_name};'

    cur.execute(query)
    results = cur.fetchall()

    for result in results:
        print(result)


# The starting character data
# Creating the table
def create_characters_table():
    stmt = "CREATE TABLE Characters(Id INT NOT NULL AUTO_INCREMENT, Class VARCHAR(25) NOT NULL, Level Int NOT NULL," \
            "Vigor Int NOT NULL, Mind Int NOT NULL, Endurance Int NOT NULL , Strength Int NOT NULL," \
            "Dexterity Int NOT NULL, Intelligence Int NOT NULL, Faith Int NOT NULL, Arcane Int NOT NULL," \
            "PRIMARY KEY (Id));"

    cur.execute(stmt)
    mariadb_con.commit()


#Function to insert the data
def insert_into_characters_table(C: str, L: int,V: int, M: int, E: int, S: int, D: int, I: int, F: int, A: int):
    insert_stmt: str = f"INSERT INTO Characters(Class, Level, Vigor, Mind, Endurance, \
                          Strength, Dexterity, Intelligence, Faith, Arcane) VALUES" \
                        f"('{C}', {L}, {V}, {M}, {F}, {S}, {D}, {I}, {F}, {A});"

    cur.execute(insert_stmt)
    mariadb_con.commit()


# Inserting the data
def add_characters():
    insert_into_characters_table('Hero', 7, 14, 9, 12, 16, 9, 7, 8, 11)
    insert_into_characters_table('Bandit', 5, 10, 11, 10, 9, 13, 9, 8, 14)
    insert_into_characters_table('Astrologer', 6, 9, 15, 9, 8, 12, 16, 7, 9)
    insert_into_characters_table('Warrior', 8, 11, 12, 11, 10, 16, 10, 8, 9)
    insert_into_characters_table('Prisoner', 9, 11, 12, 11, 11, 14, 14, 6, 9)
    insert_into_characters_table('Confessor', 10, 10, 13, 10, 12, 12, 9, 14, 9)
    insert_into_characters_table('Wretch', 1, 10, 10, 10, 10, 10, 10, 10, 10)
    insert_into_characters_table('Vagabond', 9, 15, 10, 11, 14, 13, 9, 9, 7)
    insert_into_characters_table('Prophet', 7, 10, 14, 8, 11, 10, 7, 16, 10)
    insert_into_characters_table('Samurai', 9, 12, 11, 13, 12, 15, 9, 8, 8)

# The Armor data

# Helmets
# Creating the table
def create_helmet_table():
    stmt = "CREATE TABLE Helmets(Id INT NOT NULL AUTO_INCREMENT, Name VARCHAR(50) NOT NULL, Physical_Def float NOT NULL," \
            "Magic_Def float NOT NULL, Fire_Def float NOT NULL, Lightning_Def float NOT NULL, Holy_Def float NOT NULL , " \
            "PRIMARY KEY (Id));"

    cur.execute(stmt)
    mariadb_con.commit()


# Function to insert the data
def insert_into_helmet_table(N: str, Phy: float, Mag: float, Fir: float, Lig: float, Hol: float):
    insert_stmt: str = f"INSERT INTO Helmets(Name, Physical_Def, Magic_Def, \
                              Fire_Def, Lightning_Def, Holy_Def) VALUES" \
                       f"('{N}', {Phy}, {Mag}, {Fir}, {Lig}, {Hol});"

    cur.execute(insert_stmt)
    mariadb_con.commit()


# Inserting the data
def add_helmets():
    insert_into_helmet_table('Alberichs Pointed Hat', 1.8, 4.6, 4.2, 4.4, 4.6)
    insert_into_helmet_table('Albinauric Mask', 4.0, 2.5, 3.1, 2.1, 2.5)
    insert_into_helmet_table('All Knowing Helm', 4.6, 4.4, 3.4, 3.6, 3.1)
    insert_into_helmet_table('Aristocrat Hat', 3.1, 3.8, 4.0, 3.8, 3.1)
    insert_into_helmet_table('Azurs Glintstone Crown', 2.8, 5.8, 4.6, 4.7, 5.0)
    insert_into_helmet_table('Banished Knight Helm', 6.8, 4.8, 4.8, 4.6, 4.7)
    insert_into_helmet_table('Beast Champion Helm', 6.3, 4.6, 4.9, 4.6, 4.8)
    insert_into_helmet_table('Black Knife Hood', 3.8, 2.8, 3.1, 2.1, 3.8)
    insert_into_helmet_table('Black Wolf Mask', 5.2, 4.0, 4.5, 3.6, 4.2)
    insert_into_helmet_table('Blackflame Monk Hood', 4.4, 2.8, 4.4, 2.1, 2.8)
    insert_into_helmet_table('Blackguards Iron Mask', 5.8, 4.2, 4.4, 4.0, 4.5)
    insert_into_helmet_table('Bloodhound Knight Helm', 4.4, 3.4, 3.6, 2.5, 3.6)
    insert_into_helmet_table('Blue Silver Mail Hood', 4.2, 3.6, 3.4, 2.5, 2.5)
    insert_into_helmet_table('Braves Leather Helm', 4.2, 2.8, 3.4, 2.3, 2.8)
    insert_into_helmet_table('Briar Helm', 4.6, 3.8, 4.4, 3.1, 3.8)
    insert_into_helmet_table('Bull Goat Helm', 7.5, 4.7, 4.8, 5.3, 4.6)
    insert_into_helmet_table('Carian Knight Helm', 4.2, 4.4, 4.2, 3.4, 4.2)
    insert_into_helmet_table('Chain Coif', 4.2, 2.5, 3.8, 2.1, 2.8)
    insert_into_helmet_table('Cleanrot Helm', 5.2, 4.5, 4.6, 4.0, 4.8)
    insert_into_helmet_table('Crucible Axe Helm', 6.3, 4.6, 4.6, 4.0, 4.8)
    insert_into_helmet_table('Crucible Tree Helm', 6.5, 4.6, 4.2, 4.0, 5.2)
    insert_into_helmet_table('Cuckoo Knight Helm', 4.8, 4.4, 4.2, 3.1, 3.6)
    insert_into_helmet_table('Dialloss Mask', 4.8, 3.6, 3.6, 2.5, 3.4)
    insert_into_helmet_table('Duelist Helm', 5.8, 4.0, 4.5, 3.6, 4.2)
    insert_into_helmet_table('Eccentrics Hood', 4.4, 3.4, 3.6, 2.3, 3.1)
    insert_into_helmet_table('Elden Lord Crown', 3.8, 2.5, 3.6, 2.1, 2.3)
    insert_into_helmet_table('Envoy Crown', 2.8, 5.3, 4.7, 4.9, 5.5)
    insert_into_helmet_table('Exile Hood', 4.4, 2.8, 3.8, 2.3, 3.4)
    insert_into_helmet_table('Fire Monk Hood', 4.6, 3.1, 4.5, 2.5, 2.5)
    insert_into_helmet_table('Fire Prelate Helm', 7.0, 4.8, 7.2, 4.6, 4.7)
    insert_into_helmet_table('Gelmir Knight Helm', 4.8, 3.8, 4.4, 3.6, 3.8)
    insert_into_helmet_table('Godrick Knight Helm', 4.8, 3.8, 4.2, 3.4, 3.8)
    insert_into_helmet_table('Greathelm', 5.5, 4.2, 4.6, 3.8, 4.2)
    insert_into_helmet_table('Greathood', 3.8, 5.5, 5.0, 5.5, 6.2)
    insert_into_helmet_table('Guardian Mask', 3.8, 4.2, 4.0, 4.2, 4.2)
    insert_into_helmet_table('Haligtree Knight Helm', 4.8, 3.6, 4.0, 3.4, 4.0)
    insert_into_helmet_table('Hierodas Glintstone Crown', 2.3, 4.9, 4.7, 4.6, 4.9)
    insert_into_helmet_table('Hoslows Helm', 5.2, 4.0, 4.4, 3.8, 3.8)
    insert_into_helmet_table('Ijis Mirrorhelm', 3.8, 6.2, 4.6, 4.8, 5.8)
    insert_into_helmet_table('Imp Head (Any)', 5.8, 5.0, 5.8, 4.8, 5.0)
    insert_into_helmet_table('Iron Helmet', 4.4, 2.5, 3.1, 2.3, 3.1)
    insert_into_helmet_table('Iron Kasa', 3.6, 4.0, 4.2, 4.4, 4.0)
    insert_into_helmet_table('Jar', 6.8, 4.7, 4.9, 4.6, 4.7)
    insert_into_helmet_table('Karolos Glintstone Crown', 4.4, 4.4, 4.5, 3.4, 3.8)
    insert_into_helmet_table('Knight Helm', 4.4, 3.8, 3.8, 3.4, 3.1)
    insert_into_helmet_table('Land of Reeds Helm', 3.1, 3.6, 4.0, 4.2, 3.8)
    insert_into_helmet_table('Lazuli Glintstone Crown', 4.4, 4.4, 4.5, 3.4, 3.8)
    insert_into_helmet_table('Leyndell Knight Helm', 4.8, 3.6, 4.0, 3.6, 3.8)
    insert_into_helmet_table('Leyndell Soldier Helm', 4.4, 2.8, 3.4, 2.8, 3.1)
    insert_into_helmet_table('Lionels Helm', 6.3, 4.8, 5.3, 4.6, 4.8)
    insert_into_helmet_table('Lusals Glintstone Crown', 3.1, 5.5, 4.6, 4.8, 4.9)
    insert_into_helmet_table('Malenias Winged Helm', 4.4, 2.8, 3.4, 2.3, 3.8)
    insert_into_helmet_table('Malformed Dragon Helm', 6.1, 4.6, 4.6, 4.9, 4.6)
    insert_into_helmet_table('Malikeths Helm', 4.8, 3.8, 4.0, 3.4, 4.6)
    insert_into_helmet_table('Marionette Soldier Birdhelm', 4.4, 3.1, 3.1, 2.3, 3.1)
    insert_into_helmet_table('Marionette Soldier Helm', 4.4, 3.1, 3.1, 2.3, 3.1)
    insert_into_helmet_table('Mask of Confidence', 2.3, 5.3, 4.8, 4.7, 4.7)
    insert_into_helmet_table('Mushroom Crown', 5.8, 4.8, 3.1, 4.6, 4.8)
    insert_into_helmet_table('Navy Hood', 1.4, 4.6, 4.7, 4.4, 4.5)
    insert_into_helmet_table('Night Maiden Town Crown', 2.5, 4.2, 3.8, 4.0, 4.2)
    insert_into_helmet_table('Nights Cavalry Helm', 5.0, 3.8, 4.5, 3.8, 4.5)
    insert_into_helmet_table('Nomadic Merchants Chapeau', 2.8, 3.4, 3.4, 3.4, 3.1)
    insert_into_helmet_table('Nox Swordstress Crown', 2.8, 4.4, 3.6, 4.2, 3.8)
    insert_into_helmet_table('Octopus Head', 3.4, 4.0, 3.6, 4.0, 3.8)
    insert_into_helmet_table('Okina Mask', 3.4, 3.8, 3.8, 4.2, 3.6)
    insert_into_helmet_table('Olivinus Glintstone Crown', 4.4, 4.4, 4.5, 3.6, 3.8)
    insert_into_helmet_table('Omen Helm', 6.7, 4.6, 5.2, 5.3, 4.9)
    insert_into_helmet_table('Omensmirk Mask', 3.1, 3.1, 3.4, 4.0, 3.6)
    insert_into_helmet_table('Page Hood', 1.8, 4.4, 4.2, 4.5, 4.5)
    insert_into_helmet_table('Perfumer Hood', 1.4, 4.6, 4.2, 4.4, 4.6)
    insert_into_helmet_table('Preceptors Big Hat', 2.5, 5.5, 4.9, 4.8, 4.8)
    insert_into_helmet_table('Prisoner Iron Mask', 6.8, 4.6, 4.9, 4.5, 4.8)
    insert_into_helmet_table('Prophet Blindfold', 7.0, 4.6, 4.7, 5.2, 4.5)
    insert_into_helmet_table('Queens Crescent Crown', 2.1, 4.9, 4.5, 4.6, 4.7)
    insert_into_helmet_table('Radahn Soldier Helm', 4.6, 3.1, 3.8, 2.5, 3.1)
    insert_into_helmet_table('Radahns Redmane Helm', 6.8, 4.8, 5.0, 4.5, 4.8)
    insert_into_helmet_table('Radiant Gold', 2.3, 4.6, 4.5, 4.6, 4.8)
    insert_into_helmet_table('Ragged Hat', 3.1, 3.6, 3.8, 3.8, 3.4)
    insert_into_helmet_table('Raging Wolf Helm', 4.7, 3.5, 3.9, 2.4, 3.3)
    insert_into_helmet_table('Raya Lucarian Helm', 4.4, 3.4, 3.6, 2.3, 2.8)
    insert_into_helmet_table('Redmane Knight Helm', 5.0, 3.8, 4.4, 3.4, 3.8)
    insert_into_helmet_table('Rotten Duelist Helm', 5.5, 4.5, 4.6, 4.4, 4.5)
    insert_into_helmet_table('Royal Knight Helm', 5.8, 5.0, 4.7, 4.4, 4.6)
    insert_into_helmet_table('Rulers Mask', 1.8, 4.6, 4.4, 4.6, 4.7)
    insert_into_helmet_table('Sacred Crown Helm', 3.4, 3.6, 3.8, 4.2, 4.0)
    insert_into_helmet_table('Sage Hood', 2.3, 4.8, 4.5, 4.6, 4.8)
    insert_into_helmet_table('Sanguine Noble Hood', 1.4, 4.6, 3.8, 4.5, 4.6)
    insert_into_helmet_table('Scaled Helm', 5.8, 4.8, 5.0, 4.6, 4.8)
    insert_into_helmet_table('Silver Tear Mask', 4.2, 5.5, 5.2, 5.0, 5.3)
    insert_into_helmet_table('Snow Witch Hat', 1.8, 4.6, 4.6, 4.6, 4.6)
    insert_into_helmet_table('Spellblades Pointed Hat', 1.3, 4.5, 3.9, 4.1, 4.5)
    insert_into_helmet_table('Traveling Maiden Hood', 1.4, 4.6, 4.5, 4.6, 4.6)
    insert_into_helmet_table('Tree Sentinel Helm', 6.8, 4.6, 6.2, 4.5, 5.0)
    insert_into_helmet_table('Twinned Helm', 4.8, 4.0, 4.0, 3.1, 3.6)
    insert_into_helmet_table('Twinsage Glintstone Crown', 4.4, 4.4, 4.5, 3.4, 3.8)
    insert_into_helmet_table('Vagabond Knight Helm', 4.6, 3.1, 3.6, 2.8, 2.8)
    insert_into_helmet_table('Veterans Helm', 6.8, 4.8, 5.0, 4.6, 4.7)
    insert_into_helmet_table('Vulgar Militia Helm', 3.4, 3.8, 3.8, 4.0, 3.8)
    insert_into_helmet_table('Witchs Glintstone Crown', 4.4, 4.4, 4.5, 3.4, 3.8)
    insert_into_helmet_table('Zamor Mask', 4.2, 3.1, 3.1, 2.1, 2.8)


# Chest Pieces
# Creating the table for the chestpieces
def create_chest_armor_table():
    stmt = "CREATE TABLE ChestPieces(Id INT NOT NULL AUTO_INCREMENT, Name VARCHAR(50) NOT NULL, Physical_Def float NOT NULL," \
           "Magic_Def float NOT NULL, Fire_Def float NOT NULL, Lightning_Def float NOT NULL, Holy_Def float NOT NULL , " \
           "PRIMARY KEY (Id));"

    cur.execute(stmt)
    mariadb_con.commit()


# Function to insert the data into the table
def insert_into_chest_armor_table(N: str, Phy: float, Mag: float, Fir: float, Lig: float, Hol: float):
    insert_stmt: str = f"INSERT INTO ChestPieces(Name, Physical_Def, Magic_Def, \
                              Fire_Def, Lightning_Def, Holy_Def) VALUES" \
                       f"('{N}', {Phy}, {Mag}, {Fir}, {Lig}, {Hol});"

    cur.execute(insert_stmt)
    mariadb_con.commit()


# Function that calls the previous function to insert everything easily
def add_chest_pieces():
    insert_into_chest_armor_table('All Knowing Armor', 12.9, 12.4, 9.5, 10.2, 8.8)
    insert_into_chest_armor_table('Albeerichs Robe', 5.3, 12.8, 11.9, 12.4, 12.8)
    insert_into_chest_armor_table('Astrologer Robe', 6.7, 13.5, 13.0, 13.3, 13.0)
    insert_into_chest_armor_table('Azurs Glintstone Robe', 7.1, 15.4, 12.8, 13.0, 13.8)
    insert_into_chest_armor_table('Banished Knight Armor', 18.7, 13.5, 13.5, 13.0, 13.3)
    insert_into_chest_armor_table('Beast Champion Armor', 17.5, 13.0, 13.8, 12.8, 13.5)
    insert_into_chest_armor_table('Bull Goat Armor', 20.4, 13.3, 13.5, 14.9, 12.8)
    insert_into_chest_armor_table('Cleanrot Armor', 14.6, 12.6, 12.8, 11.4, 13.5)
    insert_into_chest_armor_table('Crucible Tree Armor', 17.7, 13.0, 11.9, 11.4, 14.5)
    insert_into_chest_armor_table('Eccentrics Armor', 12.9, 10.9, 10.9, 7.1, 9.5, )
    insert_into_chest_armor_table('Elden Lord Armor', 11.9, 8.8, 11.4, 7.1, 8.0)
    insert_into_chest_armor_table('Fias Robe', 5.3, 12.6, 12.4, 12.6, 13.0)
    insert_into_chest_armor_table('Fell Omen Cloak', 6.1, 13.0, 12.4, 12.6, 12.8)
    insert_into_chest_armor_table('Hoslows Armor', 14.0, 10.9, 11.9, 10.2, 10.2)
    insert_into_chest_armor_table('Juvenile Scholar Robe', 5.3, 12.8, 11.9, 12.4, 12.6)
    insert_into_chest_armor_table('Lionels Armor', 17.5, 13.5, 14.9, 13.0, 13.5)
    insert_into_chest_armor_table('Lord of Bloods Robe', 9.3, 10.0, 12.2, 12.2, 13.3)
    insert_into_chest_armor_table('Malformed Dragon Armor', 16.8, 13.0, 13.0, 13.8, 13.0)
    insert_into_chest_armor_table('Malikeths Armor', 13.5, 10.9, 11.4, 9.5, 12.8)
    insert_into_chest_armor_table('Preceptors Long Gown', 6.1, 14.5, 13.3, 12.8, 12.8)
    insert_into_chest_armor_table('Queens Robe', 6.1, 13.8, 12.6, 12.8, 13.3)
    insert_into_chest_armor_table('Radahns Lion Armor', 18.7, 13.5, 14.1, 12.6, 13.5)
    insert_into_chest_armor_table('Raging Wolf Armor', 13.2, 9.9, 11.1, 6.8, 9.2)
    insert_into_chest_armor_table('Sanguine Noble Robe', 6.1, 13.3, 11.9, 13.0, 13.5)
    insert_into_chest_armor_table('Snow Witch Robe', 5.7, 13.4, 13.4, 13.2, 13.4)
    insert_into_chest_armor_table('Twinned Armor', 14.6, 12.4, 12.4, 10.2, 11.4)
    insert_into_chest_armor_table('Veterans Armor', 18.7, 13.5, 14.1, 12.8, 13.3)
    insert_into_chest_armor_table('White Reed Armor', 9.5, 10.9, 10.9, 11.9, 10.2)
    insert_into_chest_armor_table('Blaidds Armor', 14.6, 11.4, 12.6, 10.2, 11.9)
    insert_into_chest_armor_table('Fingerprint Armor', 13.5, 9.5, 12.6, 6.7, 9.5)
    insert_into_chest_armor_table('Fire Prelate Armor', 19.2, 13.5, 19.8, 13.0, 13.3)
    insert_into_chest_armor_table('Lusats Robe', 8, 15.4, 12.8, 13.3, 13.5)
    insert_into_chest_armor_table('Omen Armor', 18.3, 13.0, 14.5, 14.9, 13.8)
    insert_into_chest_armor_table('Royal Knight Armor', 16.0, 14.1, 13.3, 12.4, 13.0)
    insert_into_chest_armor_table('Tree Sentinel Armor', 18.7, 13.0, 17.1, 12.6, 14.1)
    insert_into_chest_armor_table('Aristocrat Coat', 8.8, 10.9, 11.4, 10.9, 8.8)
    insert_into_chest_armor_table('Bandit Garb', 8.0, 10.2, 10.2, 10.9, 9.5)
    insert_into_chest_armor_table('Black Knife Armor', 11.4, 8.8, 9.5, 6.7, 11.4)
    insert_into_chest_armor_table('Blackflame Monk Armor', 13.5, 10.2, 13.0, 8.0, 10.2)
    insert_into_chest_armor_table('Bloodhound Knight Armor', 12.4, 9.5, 10.2, 7.1, 10.3)
    insert_into_chest_armor_table('Blue Cloth Vest', 9.5, 10.2, 10.9, 11.9, 9.5)
    insert_into_chest_armor_table('Blue Silver Mail Armor', 12.4, 10.9, 10.2, 8.0, 8.0)
    insert_into_chest_armor_table('Briar Armor', 12.9, 10.9, 12.4, 8.8, 10.9)
    insert_into_chest_armor_table('Carian Knight Armor', 11.8, 12.3, 11.8, 9.4, 11.8)
    insert_into_chest_armor_table('Crucible Axe Armor', 17.5, 13.0, 12.8, 11.4, 13.5)
    insert_into_chest_armor_table('Deathbed Dress', 0.6, 11.9, 11.4, 11.9, 12.4)
    insert_into_chest_armor_table('Depraved Perfumer Robe', 6.0, 13.2, 12.7, 12.5, 12.7)
    insert_into_chest_armor_table('Errant Sorcerer Robe', 4.2, 13.0, 12.6, 12.4, 13.0)
    insert_into_chest_armor_table('Fire Monk Armor', 14.0, 10.9, 13.3, 9.5, 9.5)
    insert_into_chest_armor_table('Haligtree Crest Surcoat', 10.6, 12.9, 9.5, 10.2, 8.0)
    insert_into_chest_armor_table('Knight Armor', 12.4, 10.9, 10.9, 9.5, 8.8)
    insert_into_chest_armor_table('Kaiden Armor', 11.9, 8.0, 8.8, 7.1, 8.0)
    insert_into_chest_armor_table('Land of Reeds Armor', 8.8, 10.2, 11.4, 11.9, 10.9)
    insert_into_chest_armor_table('Marais Robe', 5.3, 12.6, 12.4, 12.4, 12.6)
    insert_into_chest_armor_table('Millicents Robe', 4.2, 12.6, 11.9, 12.4, 12.6)
    insert_into_chest_armor_table('Mushroom Body', 6.1, 13.3, 5.3, 12.8, 13.0)
    insert_into_chest_armor_table('Prophet Robe', 6.7, 13.5, 12.6, 13.0, 13.0)
    insert_into_chest_armor_table('Scale Armor', 11.9, 7.1, 10.9, 6.7, 8.0)
    insert_into_chest_armor_table('Scaled Armor', 16.0, 13.5, 14.1, 13.0, 13.5)
    insert_into_chest_armor_table('Vagabond Knight Armor', 13.5, 10.2, 10.9, 8.8, 8.8)
    insert_into_chest_armor_table('Upper Class Robe', 4.2, 12.8, 11.9, 12.6, 13.0)
    insert_into_chest_armor_table('Blue Festive Garb', 4.2, 12.6, 11.4, 12.6, 13.8)
    insert_into_chest_armor_table('Braves Battlewear', 5.3, 12.8, 12.4, 12.6, 12.8)
    insert_into_chest_armor_table('Consorts Robe', 5.3, 13.0, 12.4, 12.4, 12.8)
    insert_into_chest_armor_table('Corhyns Robe', 6.1, 13.3, 12.8, 12.8, 13.5)
    insert_into_chest_armor_table('Drake Knight Armor', 11.4, 10.2, 11.4, 8.8, 10.2)
    insert_into_chest_armor_table('Festive Garb', 4.2, 12.6, 11.9, 12.4, 13.0)
    insert_into_chest_armor_table('Godskin Noble Robe', 6.1, 13.0, 12.4, 12.6, 14.1)
    insert_into_chest_armor_table('Goldmasks Rages', 4.2, 11.9, 11.4, 11.9, 12.8)
    insert_into_chest_armor_table('Gravekeeper Cloak', 7.1, 8.0, 9.5, 10.2, 8.8)
    insert_into_chest_armor_table('Guardian Garb', 9.5, 10.9, 10.2, 10.9, 10.9)
    insert_into_chest_armor_table('Haligtree Knight Armor', 13.5, 10.2, 11.4, 9.5, 11.4)
    insert_into_chest_armor_table('High Page Clothes', 5.5, 13.5, 12.8, 13.0, 13.2)
    insert_into_chest_armor_table('Lazuli Robe', 6.1, 13.8, 11.9, 12.4, 12.8)
    insert_into_chest_armor_table('Malenias Armor', 10.9, 6.1, 7.1, 4.2, 7.1)
    insert_into_chest_armor_table('Night Maiden Armor', 8.0, 12.4, 11.4, 11.9, 12.4)
    insert_into_chest_armor_table('Nights Cavalry Armor', 14.0, 10.9, 12.6, 10.9, 12.6)
    insert_into_chest_armor_table('Raptors Black Feathers', 8.0, 10.2, 10.2, 10.9, 9.5)
    insert_into_chest_armor_table('Ronins Armor', 10.5, 11.9, 12.4, 13.4, 11.9)


# Gauntlets
# Creating the Table
def create_gauntlets_table():
    stmt = "CREATE TABLE Gauntlets(Id INT NOT NULL AUTO_INCREMENT, Name VARCHAR(50) NOT NULL, Physical_Def float NOT NULL," \
           "Magic_Def float NOT NULL, Fire_Def float NOT NULL, Lightning_Def float NOT NULL, Holy_Def float NOT NULL , " \
           "PRIMARY KEY (Id));"

    cur.execute(stmt)
    mariadb_con.commit()


# Function to insert the data
def insert_into_gauntlets_table(N: str, Phy: float, Mag: float, Fir: float, Lig: float, Hol: float):
    insert_stmt: str = f"INSERT INTO Gauntlets(Name, Physical_Def, Magic_Def, \
                                  Fire_Def, Lightning_Def, Holy_Def) VALUES" \
                       f"('{N}', {Phy}, {Mag}, {Fir}, {Lig}, {Hol});"

    cur.execute(insert_stmt)
    mariadb_con.commit()

# Inserting the data
def add_gauntlets():
    insert_into_gauntlets_table('Alberichs Bracers', 1.3, 3.2, 2.9, 3.1, 3.2)
    insert_into_gauntlets_table('All Knowing Gauntlets', 3.2, 3.1, 2.3, 2.5, 2.1)
    insert_into_gauntlets_table('Astrologer Gloves', 1.3, 3.2, 3.1, 3.2, 3.1)
    insert_into_gauntlets_table('Azurs Manchettes', 1.0, 3.4, 2.8, 2.9, 3.2)
    insert_into_gauntlets_table('Bandit Manchettes', 1.5, 1.9, 1.9, 2.1, 1.7)
    insert_into_gauntlets_table('Banished Knight Gauntlets', 4.7, 3.3, 3.3, 3.2, 3.3)
    insert_into_gauntlets_table('Battlemage Manchettes', 1.0, 3.2, 2.8, 2.9, 3.1)
    insert_into_gauntlets_table('Beast Champion Gauntlets', 4.4, 3.2, 3.4, 3.2, 3.3)
    insert_into_gauntlets_table('Black Knife Gauntlets', 2.8, 2.1, 2.3, 1.6, 2.8)
    insert_into_gauntlets_table('Blackflame Monk Gauntlets', 3.3, 2.5, 3.2, 1.9, 2.5)
    insert_into_gauntlets_table('Blaidds Gauntlets', 3.6, 2.8, 3.2, 2.7, 2.9)
    insert_into_gauntlets_table('Bloodhound Knight Gauntlets', 3.1, 2.3, 2.5, 1.7, 2.5)
    insert_into_gauntlets_table('Bloodsoaked Manchettes', 1.3, 3.1, 3.1, 3.1, 3.1)
    insert_into_gauntlets_table('Blue Silver Bracelets', 2.3, 1.9, 1.6, 1.0, 1.0)
    insert_into_gauntlets_table('Braves Bracer', 0.6, 3.1, 2.8, 2.9, 3.1)
    insert_into_gauntlets_table('Briar Gauntlets', 3.2, 2.7, 3.1, 2.1, 2.7)
    insert_into_gauntlets_table('Bull Goat Gauntlets', 5.2, 3.3, 3.3, 3.7, 3.2)
    insert_into_gauntlets_table('Carian Knight Gauntlets', 2.9, 3.1, 2.9, 2.3, 2.9)
    insert_into_gauntlets_table('Champion Bracers', 1.6, 1.9, 2.3, 2.5, 2.3)
    insert_into_gauntlets_table('Cleanrot Gauntlets', 3.6, 3.1, 3.2, 2.8, 3.3)
    insert_into_gauntlets_table('Confessor Gloves', 2.1, 2.8, 2.8, 3.1, 2.5)
    insert_into_gauntlets_table('Crucible Gauntlets', 4.4, 3.2, 3.2, 2.8, 3.3)
    insert_into_gauntlets_table('Cuckoo Knight Gauntlets', 3.3, 3.1, 2.9, 2.1, 2.5)
    insert_into_gauntlets_table('Depraved Perfumer Gloves', 1.5, 3.2, 3.1, 3.1, 3.1)
    insert_into_gauntlets_table('Drake Knight Gauntlets', 2.8, 2.5, 2.8, 2.1, 2.5)
    insert_into_gauntlets_table('Eccentrics Manchettes', 2.9, 2.1, 2.3, 1.5, 1.9)
    insert_into_gauntlets_table('Elden Lord Bracers', 2.9, 2.1, 2.8, 1.7, 1.9)
    insert_into_gauntlets_table('Errant Sorcerer Manchettes', 0.6, 3.2, 3.1, 2.9, 3.2)
    insert_into_gauntlets_table('Exile Gauntlets', 2.9, 1.7, 2.5, 1.5, 2.1)
    insert_into_gauntlets_table('Fingerprint Gauntlets', 3.3, 2.3, 3.1, 1.6, 2.3)
    insert_into_gauntlets_table('Fire Monk Gauntlets', 3.5, 2.7, 3.3, 2.3, 2.3)
    insert_into_gauntlets_table('Fire Prelate Gauntlets', 4.9, 3.3, 5.0, 3.2, 3.3)
    insert_into_gauntlets_table('Foot Soldier Gauntlets', 2.1, 2.5, 2.7, 2.8, 2.5)
    insert_into_gauntlets_table('Gauntlets', 2.9, 1.7, 2.7, 1.5, 1.9)
    insert_into_gauntlets_table('Gelmir Knight Gauntlets', 3.3, 2.7, 3.1, 2.5, 2.7)
    insert_into_gauntlets_table('Godrick Knight Gauntlets', 3.3, 2.7, 2.9, 2.3, 2.7)
    insert_into_gauntlets_table('Godskin Apostole Bracelets', 1.7, 3.2, 3.1, 3.2, 3.6)
    insert_into_gauntlets_table('Godskin Noble Bracelets', 1.3, 3.2, 2.9, 3.1, 3.4)
    insert_into_gauntlets_table('Gold Bracelets', 1.0, 2.9, 2.8, 2.9, 3.2)
    insert_into_gauntlets_table('Golden Prosthetic', 1.5, 3.2, 3.1, 3.2, 3.2)
    insert_into_gauntlets_table('Guardian Bracers', 2.7, 2.9, 2.8, 2.9, 2.9)
    insert_into_gauntlets_table('Haligtree Gauntlets', 3.2, 2.3, 2.5, 1.9, 2.5)
    insert_into_gauntlets_table('Haligtree Knight Gauntlets', 3.3, 2.5, 2.8, 2.3, 2.8)
    insert_into_gauntlets_table('Highwayman Gauntlets', 1.9, 2.7, 2.7, 2.8, 2.5)
    insert_into_gauntlets_table('Hoslows Gauntlets', 3.5, 2.7, 2.9, 2.5, 2.5)
    insert_into_gauntlets_table('Iron Gauntlets', 2.8, 2.1, 2.3, 1.5, 1.9)
    insert_into_gauntlets_table('Kaiden Gauntlets', 2.9, 1.9, 2.1, 1.7, 1.9)
    insert_into_gauntlets_table('Knight Gauntlets', 3.1, 2.7, 2.7, 2.3, 2.1)
    insert_into_gauntlets_table('Land of Reeds Gauntlets', 2.1, 2.5, 2.8, 2.9, 2.7)
    insert_into_gauntlets_table('Leather Gloves', 1.9, 2.3, 2.3, 2.5, 2.5)
    insert_into_gauntlets_table('Leyndell Knight Gauntlets', 3.3, 2.5, 2.8, 2.5, 2.7)
    insert_into_gauntlets_table('Lionels Gauntlets', 4.4, 3.3, 3.7, 3.2, 3.3)
    insert_into_gauntlets_table('Lusats Manchettes', 1.3, 3.4, 2.8, 3.1, 3.1)
    insert_into_gauntlets_table('Malenias Gauntlets', 3.1, 1.9, 2.3, 1.6, 2.7)
    insert_into_gauntlets_table('Malformed Dragon Gauntlets', 4.2, 3.2, 3.2, 3.4, 3.2)
    insert_into_gauntlets_table('Malikeths Gauntlets', 3.3, 2.7, 2.8, 2.3, 3.2)
    insert_into_gauntlets_table('Mausoleum Gauntlents', 3.2, 2.5, 2.5, 2.1, 2.5)
    insert_into_gauntlets_table('Mausoleum Knight Gauntlets', 3.3, 2.7, 2.8, 2.5, 2.8)
    insert_into_gauntlets_table('Millicents Gloves', 1.0, 3.1, 2.9, 3.1, 3.1)
    insert_into_gauntlets_table('Mushroom Arms', 1.5, 3.3, 1.3, 3.2, 3.2)
    insert_into_gauntlets_table('Nights Cavalry Gauntlets', 3.5, 2.7, 3.1, 2.7, 3.1)
    insert_into_gauntlets_table('Nobles Gloves', 1.5, 3.3, 3.3, 3.2, 3.3)
    insert_into_gauntlets_table('Nox Bracelets', 2.1, 2.9, 2.8, 2.8, 2.3)
    insert_into_gauntlets_table('Omen Gauntlets', 4.6, 3.2, 3.6, 3.7, 3.4)
    insert_into_gauntlets_table('Omenkiller Long Gauntlets', 2.1, 2.1, 2.3, 2.8, 2.5)
    insert_into_gauntlets_table('Perfumer Gloves', 1.0, 3.2, 2.9, 3.1, 3.2)
    insert_into_gauntlets_table('Preceptors Gloves', 1.5, 3.6, 3.3, 3.2, 3.2)
    insert_into_gauntlets_table('Queens Bracelets', 1.5, 3.4, 3.1, 3.2, 3.3)
    insert_into_gauntlets_table('Radahns Soldier Gauntlets', 3.3 ,2.5, 2.8, 1.9, 2.3)
    insert_into_gauntlets_table('Ragged Gloves', 2.3, 2.7, 2.8, 2.9, 2.7)
    insert_into_gauntlets_table('Raging Wolf Gauntlets', 3.2, 2.4, 2.7, 1.6, 2.2)
    insert_into_gauntlets_table('Raya Lucarian Gauntlets', 3.2, 2.7, 2.7, 1.7, 2.1)
    insert_into_gauntlets_table('Redmane Knight Gauntlets', 3.5, 2.7, 3.1, 2.3, 2.7)
    insert_into_gauntlets_table('Ronins Gauntlets', 2.7, 2.9, 3.1, 3.2, 2.9)
    insert_into_gauntlets_table('Royal Knight Gauntlets', 4.0, 3.5, 3.3, 3.1, 3.2)
    insert_into_gauntlets_table('Royal Remains Gauntlets', 2.9, 2.3, 2.5, 1.9, 2.1)
    insert_into_gauntlets_table('Scaled Gauntlets', 4.0, 3.3, 3.5, 3.2, 3.3)
    insert_into_gauntlets_table('Sorcerer Manchettes', 1.0, 3.2, 3.1, 2.9, 3.1)
    insert_into_gauntlets_table('Spellblades Gloves', 0.9, 3.1, 2.7, 2.8, 3.1)
    insert_into_gauntlets_table('Travelers Gloves', 1.3, 3.2, 3.2, 3.1, 3.2)
    insert_into_gauntlets_table('Travelers Manchettes', 1.6, 3.3, 3.2, 3.2, 3.1)
    insert_into_gauntlets_table('Traveling Maiden Gloves', 1.3, 3.3, 3.2, 3.2, 3.3)
    insert_into_gauntlets_table('Tree Sentinel Gauntlets', 4.7, 3.2, 4.3, 3.1, 3.5)
    insert_into_gauntlets_table('Twinned Gauntlets', 3.3, 2.8, 2.8, 2.1, 2.5)
    insert_into_gauntlets_table('Vagabond Knight Gauntlets', 3.3, 2.5, 2.7, 2.1, 2.1)
    insert_into_gauntlets_table('Veterans Gauntlets', 4.7, 3.3, 3.5, 3.2, 3.3)
    insert_into_gauntlets_table('Vulgar Militia Gauntlets', 1.7, 2.1, 2.1, 2.3, 2.1)
    insert_into_gauntlets_table('War Surgeon Gloves', 1.6, 2.2, 2.4, 2.6, 2.4)
    insert_into_gauntlets_table('Warrior Gauntlets', 2.3, 2.5, 2.7, 2.9, 2.3)
    insert_into_gauntlets_table('White Reed Gauntlets', 2.3, 2.7, 2.7, 2.9, 2.5)
    insert_into_gauntlets_table('Zamor Bracelets', 2.8, 1.9, 1.9, 1.3, 1.7)


# Leg Armor
# Creating the table
def create_legs_table():
    stmt = "CREATE TABLE Legs(Id INT NOT NULL AUTO_INCREMENT, Name VARCHAR(50) NOT NULL, Physical_Def float NOT NULL," \
           "Magic_Def float NOT NULL, Fire_Def float NOT NULL, Lightning_Def float NOT NULL, Holy_Def float NOT NULL , " \
           "PRIMARY KEY (Id));"

    cur.execute(stmt)
    mariadb_con.commit()


# Function to insert the data
def insert_into_legs_table(N: str, Phy: float, Mag: float, Fir: float, Lig: float, Hol: float):
    insert_stmt: str = f"INSERT INTO Legs(Name, Physical_Def, Magic_Def, \
                                      Fire_Def, Lightning_Def, Holy_Def) VALUES" \
                       f"('{N}', {Phy}, {Mag}, {Fir}, {Lig}, {Hol});"

    cur.execute(insert_stmt)
    mariadb_con.commit()


# Inserting the data
def add_legs():
    insert_into_legs_table('All Knowing Greaves', 7.4, 7.1, 5.4, 5.8, 5.0)
    insert_into_legs_table('Alberichs Trousers', 3.0, 7.3, 6.8, 7.2, 7.3)
    insert_into_legs_table('Astrologer Trousers', 3.8, 7.7, 7.4, 7.6, 7.4)
    insert_into_legs_table('Bandit Boots', 4.0, 5.4, 5.4, 5.8, 5.0)
    insert_into_legs_table('Banished Knight Greaves', 10.8, 7.7, 7.7, 7.4, 7.6)
    insert_into_legs_table('Beast Champion Greaves', 10.1, 7.4, 7.9, 7.3, 7.7)
    insert_into_legs_table('Black Knife Greaves', 6.5, 5.0, 5.4, 3.8, 6.5)
    insert_into_legs_table('Blackflame Monk Greaves', 7.7, 5.8, 7.4, 4.5, 5.8)
    insert_into_legs_table('Bloodhound Knight Greaves', 7.1, 5.4, 5.8, 4.0, 5.8)
    insert_into_legs_table('Briar Greaves', 7.4, 6.2, 7.1, 5.0, 6.2)
    insert_into_legs_table('Bull Goat Greaves', 11.9, 7.6, 7.7, 8.5, 7.3)
    insert_into_legs_table('Champion Gaiters', 3.8, 4.5, 5.4, 5.8, 5.4)
    insert_into_legs_table('Carian Knight Greaves', 6.8, 7.1, 6.8, 5.4, 6.8)
    insert_into_legs_table('Chain Leggings', 6.8, 4.0, 6.2, 3.4, 4.5)
    insert_into_legs_table('Cleanrot Greaves', 8.4, 7.2, 7.3, 6.5, 7.7)
    insert_into_legs_table('Cloth Trousers', 3.0, 7.3, 7.1, 6.8, 7.1)
    insert_into_legs_table('Commoners Shoes', 1.5, 7.1, 6.5, 6.8, 7.1)
    insert_into_legs_table('Confessor Boots', 4.5, 6.2, 6.2, 6.8, 5.4)
    insert_into_legs_table('Consorts Trousers', 3.0, 7.4, 7.1, 7.1, 7.3)
    insert_into_legs_table('Crucible Greaves', 10.1, 7.4, 7.3, 6.5, 7.7)
    insert_into_legs_table('Eccentrics Breeches', 6.5, 4.5, 5.0, 3.0, 4.0)
    insert_into_legs_table('Elden Lord Greaves', 6.5, 4.5, 6.2, 3.8, 4.0)
    insert_into_legs_table('Errant Sorcerer Boots', 3.0, 7.6, 7.3, 7.2, 7.6)
    insert_into_legs_table('Exile Greaves', 7.4, 4.5, 6.2, 3.8, 5.4)
    insert_into_legs_table('Finger Maiden Shoes', 3.0, 7.6, 7.2, 7.3, 7.6)
    insert_into_legs_table('Fire Monk Greaves', 8.0, 6.2, 7.6, 5.4, 5.4)
    insert_into_legs_table('Foot Soldier Greaves', 5.4, 6.2, 6.5, 6.8, 6.2)
    insert_into_legs_table('Fur Leggings', 3.4, 3.8, 4.0, 5.0, 4.0)
    insert_into_legs_table('Gelmir Knight Greaves', 7.7, 6.2, 7.1, 5.8, 6.2)
    insert_into_legs_table('Godrick Knight Greaves', 7.7, 6.2, 6.8, 5.4, 6.2)
    insert_into_legs_table('Godskin Apostle Trousers', 3.4, 7.2, 6.8, 7.1, 7.9)
    insert_into_legs_table('Guardian Greaves', 6.2, 6.8, 6.5, 6.8, 6.8)
    insert_into_legs_table('Haligtree Greaves', 7.4, 5.4, 5.8, 4.5, 5.8)
    insert_into_legs_table('Haslows Greaves', 8.0, 6.2, 6.8, 5.8, 5.8)
    insert_into_legs_table('Kaiden Trousers', 6.5, 4.0, 4.5, 3.8, 4.0)
    insert_into_legs_table('Knight Greaves', 7.1, 6.2, 6.2, 5.4, 5.0)
    insert_into_legs_table('Land of Reeds Greaves', 5.0, 5.8, 6.5, 6.8, 6.2)
    insert_into_legs_table('Leather Trousers', 6.5, 5.0, 5.4, 3.4, 4.5)
    insert_into_legs_table('Lionels Greaves', 10.1, 7.7, 8.5, 7.4, 7.7)
    insert_into_legs_table('Malformed Dragon Greaves', 9.6, 7.4, 7.4, 7.9, 7.4)
    insert_into_legs_table('Malikeths Greaves', 7.7, 6.2, 6.5, 5.4, 7.3)
    insert_into_legs_table('Millicents Boots', 2.3, 7.2, 6.8, 7.1, 7.2)
    insert_into_legs_table('Mushroom Legs', 3.4, 7.6, 3.0, 7.3, 7.4)
    insert_into_legs_table('Nobles Trousers', 3.4, 7.6, 7.7, 7.4, 7.6)
    insert_into_legs_table('Omenkiller Boots', 5.0, 5.0, 5.4, 6.5, 5.8)
    insert_into_legs_table('Queens Leggings', 2.3, 7.6, 6.8, 7.1, 7.3)
    insert_into_legs_table('Page Trousers', 3.4, 7.2, 7.1, 7.3, 7.3)
    insert_into_legs_table('Preceptors Trousers', 3.4, 8.3, 7.6, 7.6, 7.3)
    insert_into_legs_table('Prisoner Trousers', 2.3, 6.8, 6.5, 6.5, 7.2)
    insert_into_legs_table('Prophet Trousers', 3.0, 7.6, 7.3, 7.2, 7.6)
    insert_into_legs_table('Radahns Greaves', 10.8, 7.7, 8.1, 7.2, 7.7)
    insert_into_legs_table('Radahn Soldier Greaves', 7.7, 5.8, 6.5, 4.5, 5.4)
    insert_into_legs_table('Raging Wolf Greaves', 7.5, 5.6, 6.3, 3.8, 5.2)
    insert_into_legs_table('Raya Lucarian Greaves', 7.4, 6.2, 6.2, 4.0, 5.0)
    insert_into_legs_table('Rotten Duelist Greaves', 7.4, 6.2, 6.6, 5.8, 6.2)
    insert_into_legs_table('Sage Trousers', 3.4, 7.6, 7.1, 7.3, 7.6)
    insert_into_legs_table('Sanguine Noble Waistcloth', 3.0, 7.4, 6.5, 7.3, 7.6)
    insert_into_legs_table('Scaled Greaves', 9.2, 7.7, 8.1, 7.4, 7.7)
    insert_into_legs_table('Snow Witch Skirt', 3.0, 7.4, 7.4, 7.3, 7.4)
    insert_into_legs_table('Sorcerer Leggings', 2.3, 7.3, 7.3, 7.1, 7.3)
    insert_into_legs_table('Travelers Slops', 3.0, 7.3, 7.3, 7.1, 7.3)
    insert_into_legs_table('Traveling Maiden Boots', 3.1, 7.7, 7.4, 7.5, 7.7)
    insert_into_legs_table('Twinned Greaves', 7.7, 6.5, 6.5, 5.0, 5.8)
    insert_into_legs_table('Warrior Greaves', 5.4, 5.8, 6.2, 6.8, 5.4)
    insert_into_legs_table('Veterans Greaves', 10.8, 7.7, 8.1, 7.3, 7.6)
    insert_into_legs_table('White Reed Greaves', 5.4, 6.2, 6.2, 6.8, 5.8)
    insert_into_legs_table('Zamor Legwraps', 6.5, 4.5, 4.5, 3.0, 4.0)
    insert_into_legs_table('Drake Knight Greaves', 6.5, 5.8, 6.5, 5.0, 5.8)
    insert_into_legs_table('Perfumer Searong', 2.3, 7.3, 6.8, 7.1, 7.3)
    insert_into_legs_table('Spellblades Trousers', 2.9, 7.3, 6.7, 7.0, 7.3)
    insert_into_legs_table('Ronins Greaves', 6.2, 6.8, 7.1, 7.3, 6.8)
    insert_into_legs_table('Blaidds Greaves', 8.4, 6.5, 7.3, 6.2, 6.8)
    insert_into_legs_table('Nights Cavalry Greaves', 8.0, 6.2, 7.2, 6.2, 7.2)
    insert_into_legs_table('Blue Silver Mail Skirt', 6.8, 5.8, 5.4, 4.0, 4.0)
    insert_into_legs_table('Nomadic Merchants Trousers', 4.5, 5.4, 5.4, 5.4, 5.0)
    insert_into_legs_table('Tree Sentinel Greaves', 10.8, 7.4, 9.9, 7.2, 8.1)
    insert_into_legs_table('Royal Knight Greaves', 9.2, 8.1, 7.6, 7.1, 7.4)
    insert_into_legs_table('Nox Greaves', 5.4, 7.1, 6.8, 6.8, 5.8)
    insert_into_legs_table('Shaman Leggings', 3.0, 4.5, 4.0, 4.5, 3.8)
    insert_into_legs_table('Omen Greaves', 10.6, 7.4, 8.3, 8.5, 7.9)
    insert_into_legs_table('Battlemage Legwraps', 3.0, 7.4, 6.8, 7.1, 7.2)


# Save the Build Table creation and insertion
def create_saved_builds_table():
    stmt = "CREATE TABLE Saved_Builds(Id INT NOT NULL AUTO_INCREMENT, Name VARCHAR(25) NOT NULL, "\
            "Class VARCHAR(25) NOT NULL, Level Int NOT NULL, Vigor Int NOT NULL, Mind Int NOT NULL,"\
            "Endurance Int NOT NULL , Strength Int NOT NULL, Dexterity Int NOT NULL, Intelligence Int NOT NULL, "\
            "Faith Int NOT NULL, Arcane Int NOT NULL, Remaining Int NOT NULL, Helmet VARCHAR(50) NOT NULL,"\
            "Chestpiece VARCHAR(50) NOT NULL, Gauntlets VARCHAR(50) NOT NULL, Legs VARCHAR(50) NOT NULL,"\
            "PRIMARY KEY (Id));"
    cur.execute(stmt)
    mariadb_con.commit()


def save_build_to_db(N: str, C: str, L: int, V: int, M: int, E: int, S: int, D: int, I: int, F: int, A: int, R: int,
                     H: str, Chest: str, Gaunt: str, Leg: str):
    insert_stmt: str = f"INSERT INTO Saved_Builds(Name, Class, Level, Vigor, Mind, Endurance, Strength, \
                         Dexterity, Intelligence, Faith, Arcane, Remaining, Helmet, Chestpiece, Gauntlets, Legs) VALUES"\
                        f"('{N}', '{C}', {L}, {V}, {M}, {E}, {S}, {D}, {I}, {F}, {A}, {R}, \
                         '{H}', '{Chest}', '{Gaunt}', '{Leg}')"
    cur.execute(insert_stmt)
    mariadb_con.commit()


# Main
if __name__ == '__main__':
    # db = "Elden-Build-Info"  # Naming the database
    # create_database(db)  # Creating the database

    # Populating the database with the necessary tables

    # create_characters_table()
    # add_characters()
    # create_helmet_table()
    # add_helmets()
    # create_chest_armor_table()
    # add_chest_pieces()
    # create_gauntlets_table()
    # add_gauntlets()
    # create_legs_table()
    # add_legs()
    # create_saved_builds_table()

    # Printing the data to make sure it was inserted properly

    print_from_table("Characters")
    print_from_table("Helmets")
    print_from_table("ChestPieces")
    print_from_table("Gauntlets")
    print_from_table("Legs")
    print_from_table("Saved_Builds")
