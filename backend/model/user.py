from dataclasses import dataclass
@dataclass
class User:
    data: dict
    def to_dict(self):
        return dict(self.data)
