from enums.vehicle_type import VehicleType
from models.ticket import Ticket

RATE_PER_HOUR = {
    VehicleType.BIKE: 10,
    VehicleType.CAR: 20,
    VehicleType.TRUCK: 40,
}


class Payment:
    def __init__(self, ticket: Ticket):
        self.ticket = ticket
        self.amount: float = 0.0

    def calculate_amount(self) -> float:
        hours = self.ticket.get_duration_hours()
        rate = RATE_PER_HOUR[self.ticket.vehicle.vehicle_type]
        self.amount = max(rate, round(hours * rate, 2))
        return self.amount

    def process_payment(self) -> float:
        self.calculate_amount()
        self.ticket.close()
        return self.amount
