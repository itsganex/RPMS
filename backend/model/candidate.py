from dataclasses import dataclass
@dataclass
class Candidate:
    data: dict
    def to_dict(self):
        return dict(self.data)
