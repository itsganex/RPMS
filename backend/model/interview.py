from dataclasses import dataclass
@dataclass
class Interview:
    data: dict
    def to_dict(self):
        return dict(self.data)
