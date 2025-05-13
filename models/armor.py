from pydantic import BaseModel


class Armor(BaseModel):
    helmet: str
    chestpiece: str
    gauntlet: str
    legs: str
