from dataclasses import dataclass


@dataclass
class Config:
    fullname: str

    def __post_init__(self):
        self.validateFullName()

    def validateFullName(self):
        name = self.fullname
        if name==None or name.strip()=="":
            raise ValueError(f"Invalid fullname: '{name}'")