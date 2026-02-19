from models.parking_floor import ParkingFloor
from models.vehicle import Vehicle
from models.ticket import Ticket
from models.payment import Payment
from strategy.parking_strategy import ParkingStrategy


class ParkingLot:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, name: str, strategy: ParkingStrategy):
        if hasattr(self, "_initialized"):
            return
        self._initialized = True
        self.name = name
        self.floors: list[ParkingFloor] = []
        self.tickets: dict[int, Ticket] = {}
        self.strategy = strategy
        self._ticket_counter = 0

    def add_floor(self, floor: ParkingFloor) -> None:
        self.floors.append(floor)

    def park_vehicle(self, vehicle: Vehicle) -> Ticket:
        result = self.strategy.find_spot(self.floors, vehicle)
        if result is None:
            raise Exception(f"No available spot for {vehicle}")

        spot, floor_id = result
        spot.park(vehicle)

        self._ticket_counter += 1
        ticket = Ticket(self._ticket_counter, vehicle, spot, floor_id)
        self.tickets[ticket.ticket_id] = ticket
        return ticket

    def unpark_vehicle(self, ticket_id: int) -> float:
        if ticket_id not in self.tickets:
            raise Exception(f"Ticket #{ticket_id} not found")

        ticket = self.tickets[ticket_id]
        payment = Payment(ticket)
        amount = payment.process_payment()
        ticket.spot.remove_vehicle()
        del self.tickets[ticket_id]
        return amount

    def display_status(self):
        print(f"\n=== {self.name} ===")
        for floor in self.floors:
            print(f"\n{floor}")
            for spot in floor.spots:
                print(f"  {spot}")
        print(f"\nActive tickets: {len(self.tickets)}")
