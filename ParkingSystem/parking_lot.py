from models.parking_floor import ParkingFloor
from models.vehicle import Vehicle
from models.ticket import Ticket
from strategy.parking_strategy import ParkingStrategy


class ParkingLot:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, name: str, strategy: ParkingStrategy):
        if hasattr(self, '_initialized'):
            return
        self._initialized = True
        self.name = name
        self.floors: list[ParkingFloor] = []
        self.tickets: dict[int, Ticket] = {}
        self.strategy = strategy
        self._ticket_counter = 0

    def add_floor(self, floor: ParkingFloor) -> None:
        # TODO: implement
        pass

    def park_vehicle(self, vehicle: Vehicle) -> Ticket | None:
        # TODO: implement - use strategy to find spot, create ticket
        pass

    def unpark_vehicle(self, ticket_id: int) -> float:
        # TODO: implement - free spot, calculate payment, return amount
        pass
