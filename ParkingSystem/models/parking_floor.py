from models.parking_spot import ParkingSpot
from models.vehicle import Vehicle


class ParkingFloor:
    def __init__(self, floor_id: int):
        self.floor_id = floor_id
        self.spots: list[ParkingSpot] = []

    def add_spot(self, spot: ParkingSpot) -> None:
        self.spots.append(spot)

    def get_available_spots(self, vehicle: Vehicle) -> list[ParkingSpot]:
        return [spot for spot in self.spots if spot.is_available() and spot.can_fit(vehicle)]

    def __str__(self):
        available = sum(1 for s in self.spots if s.is_available())
        return f"Floor {self.floor_id}: {available}/{len(self.spots)} spots available"
