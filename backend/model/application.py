from dataclasses import dataclass
@dataclass
class Application:
    data: dict
    def to_dict(self):
        return dict(self.data)
