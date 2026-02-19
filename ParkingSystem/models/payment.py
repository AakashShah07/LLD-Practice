from models.ticket import Ticket


class Payment:
    def __init__(self, ticket: Ticket):
        self.ticket = ticket
        self.amount: float = 0.0

    def calculate_amount(self) -> float:
        # TODO: implement - calculate based on duration and vehicle type
        pass

    def process_payment(self) -> bool:
        # TODO: implement
        pass
