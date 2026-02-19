from datetime import datetime
from models.vehicle import Vehicle
from models.parking_spot import ParkingSpot
from enums.ticket_status import TicketStatus


class Ticket:
    def __init__(self, ticket_id: int, vehicle: Vehicle, spot: ParkingSpot, floor_id: int):
        self.ticket_id = ticket_id
        self.vehicle = vehicle
        self.spot = spot
        self.floor_id = floor_id
        self.entry_time = datetime.now()
        self.exit_time: datetime | None = None
        self.status = TicketStatus.ACTIVE

    def close(self):
        self.exit_time = datetime.now()
        self.status = TicketStatus.PAID

    def get_duration_hours(self) -> float:
        end = self.exit_time or datetime.now()
        return (end - self.entry_time).total_seconds() / 3600

    def __str__(self):
        return (
            f"Ticket #{self.ticket_id} | {self.vehicle} | "
            f"Floor {self.floor_id}, Spot {self.spot.spot_id} | "
            f"Status: {self.status.value}"
        )
