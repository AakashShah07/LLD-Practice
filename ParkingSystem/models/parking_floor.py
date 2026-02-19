from models.parking_spot import ParkingSpot
from models.vehicle import Vehicle


class ParkingFloor:
    def __init__(self, floor_id: int):
        self.floor_id = floor_id
        self.spots: list[ParkingSpot] = []

    def add_spot(self, spot: ParkingSpot) -> None:
        # TODO: implement
        pass

    def find_available_spot(self, vehicle: Vehicle) -> ParkingSpot | None:
        # TODO: implement - find a suitable available spot for the vehicle
        pass
