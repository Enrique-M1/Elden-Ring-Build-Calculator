from pydantic import BaseModel


class FullBuild(BaseModel):
    S_Class: str
    Level: int
    Vigor: int
    Mind: int
    Endurance: int
    Strength: int
    Dexterity: int
    Intelligence: int
    Faith: int
    Arcane: int
    Remaining: int
    Helmet: str
    Chestpiece: str
    Gauntlet: str
    Legs: str
