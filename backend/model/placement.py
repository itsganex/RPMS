from dataclasses import dataclass
@dataclass
class Placement:
    data: dict
    def to_dict(self):
        return dict(self.data)
