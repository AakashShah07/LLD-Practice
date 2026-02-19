from abc import ABC
from enums.spot_type import SpotType
from enums.vehicle_type import VehicleType
from models.vehicle import Vehicle


SPOT_VEHICLE_MAP = {
    SpotType.BIKE: [VehicleType.BIKE],
    SpotType.COMPACT: [VehicleType.BIKE, VehicleType.CAR],
    SpotType.LARGE: [VehicleType.BIKE, VehicleType.CAR, VehicleType.TRUCK],
}


class ParkingSpot(ABC):
    def __init__(self, spot_id: int, spot_type: SpotType):
        self.spot_id = spot_id
        self.spot_type = spot_type
        self.vehicle: Vehicle | None = None

    def is_available(self) -> bool:
        return self.vehicle is None

    def can_fit(self, vehicle: Vehicle) -> bool:
        return vehicle.vehicle_type in SPOT_VEHICLE_MAP[self.spot_type]

    def park(self, vehicle: Vehicle) -> None:
        if not self.is_available():
            raise Exception(f"Spot {self.spot_id} is already occupied")
        if not self.can_fit(vehicle):
            raise Exception(f"Spot {self.spot_id} cannot fit {vehicle.vehicle_type.value}")
        self.vehicle = vehicle

    def remove_vehicle(self) -> Vehicle:
        if self.vehicle is None:
            raise Exception(f"Spot {self.spot_id} is already empty")
        vehicle = self.vehicle
        self.vehicle = None
        return vehicle

    def __str__(self):
        status = f"Occupied by {self.vehicle}" if self.vehicle else "Available"
        return f"Spot {self.spot_id} ({self.spot_type.value}) - {status}"


class CompactSpot(ParkingSpot):
    def __init__(self, spot_id: int):
        super().__init__(spot_id, SpotType.COMPACT)


class LargeSpot(ParkingSpot):
    def __init__(self, spot_id: int):
        super().__init__(spot_id, SpotType.LARGE)


class BikeSpot(ParkingSpot):
    def __init__(self, spot_id: int):
        super().__init__(spot_id, SpotType.BIKE)
