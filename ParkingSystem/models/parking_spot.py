from abc import ABC
from enums.spot_type import SpotType
from models.vehicle import Vehicle


class ParkingSpot(ABC):
    def __init__(self, spot_id: int, spot_type: SpotType):
        self.spot_id = spot_id
        self.spot_type = spot_type
        self.vehicle: Vehicle | None = None

    def is_available(self) -> bool:
        # TODO: implement
        pass

    def park(self, vehicle: Vehicle) -> None:
        # TODO: implement
        pass

    def remove_vehicle(self) -> None:
        # TODO: implement
        pass


class CompactSpot(ParkingSpot):
    def __init__(self, spot_id: int):
        super().__init__(spot_id, SpotType.COMPACT)


class LargeSpot(ParkingSpot):
    def __init__(self, spot_id: int):
        super().__init__(spot_id, SpotType.LARGE)


class BikeSpot(ParkingSpot):
    def __init__(self, spot_id: int):
        super().__init__(spot_id, SpotType.BIKE)
