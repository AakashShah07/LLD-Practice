from datetime import datetime
from models.vehicle import Vehicle
from models.parking_spot import ParkingSpot
from enums.ticket_status import TicketStatus


class Ticket:
    def __init__(self, ticket_id: int, vehicle: Vehicle, spot: ParkingSpot):
        self.ticket_id = ticket_id
        self.vehicle = vehicle
        self.spot = spot
        self.entry_time: datetime = datetime.now()
        self.exit_time: datetime | None = None
        self.status: TicketStatus = TicketStatus.ACTIVE
