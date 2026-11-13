from dataclasses import dataclass
@dataclass
class Company:
    data: dict
    def to_dict(self):
        return dict(self.data)
