from abc import ABC, abstractmethod
from models.parking_spot import ParkingSpot
from models.parking_floor import ParkingFloor
from models.vehicle import Vehicle


class ParkingStrategy(ABC):
    @abstractmethod
    def find_spot(self, floors: list[ParkingFloor], vehicle: Vehicle) -> tuple[ParkingSpot, int] | None:
        """Returns (spot, floor_id) or None if no spot available."""
        pass


class NearestFirstStrategy(ParkingStrategy):
    """Assigns the first available spot starting from floor 0, spot 0."""

    def find_spot(self, floors: list[ParkingFloor], vehicle: Vehicle) -> tuple[ParkingSpot, int] | None:
        for floor in floors:
            available = floor.get_available_spots(vehicle)
            if available:
                return available[0], floor.floor_id
        return None
