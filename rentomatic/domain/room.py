import uuid
from dataclasses import dataclass

@dataclass
class Room:
    code : uuid.UUID
    size : int
    price : int
    longitude : float
    latitude : float
    
    @classmethod
    def from_dict(self, d):
        return self(**d)
    
    def to_dict(self):
        return  self.__dict__


# room = Room(uuid.uuid4,1,1,1,1)

# print(room.__eq__(room))

