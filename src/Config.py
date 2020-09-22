from dataclasses import dataclass
import yaml

@dataclass
class Config:
    fullname: str

    def __post_init__(self):
        self._validateFullName()

    def _validateFullName(self):
        name = self.fullname
        if name==None or name.strip()=="":
            raise ValueError(f"Invalid fullname: '{name}'")
    
    @classmethod
    def parseYaml(cls, string:str):
        dictionary = yaml.safe_load(string)
        fullname = dictionary['fullname']
        return cls(fullname=fullname)