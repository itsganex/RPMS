from dataclasses import dataclass
@dataclass
class Offer:
    data: dict
    def to_dict(self):
        return dict(self.data)
