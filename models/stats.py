from pydantic import BaseModel


class Stats(BaseModel):
    build_type: str
    class_name: str
    save_build_name: str
