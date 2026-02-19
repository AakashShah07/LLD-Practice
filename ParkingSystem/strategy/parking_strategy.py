from abc import ABC, abstractmethod
from models.parking_spot import ParkingSpot
from models.parking_floor import ParkingFloor
from models.vehicle import Vehicle


class ParkingStrategy(ABC):
    @abstractmethod
    def find_spot(self, floors: list[ParkingFloor], vehicle: Vehicle) -> ParkingSpot | None:
        pass


class NearestFirstStrategy(ParkingStrategy):
    def find_spot(self, floors: list[ParkingFloor], vehicle: Vehicle) -> ParkingSpot | None:
        # TODO: implement - assign nearest available spot (floor 0 first)
        pass
