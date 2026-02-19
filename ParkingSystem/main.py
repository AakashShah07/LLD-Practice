from parking_lot import ParkingLot
from models.vehicle import Car, Bike, Truck
from models.parking_spot import CompactSpot, LargeSpot, BikeSpot
from models.parking_floor import ParkingFloor
from strategy.parking_strategy import NearestFirstStrategy


def main():
    # Setup parking lot
    strategy = NearestFirstStrategy()
    lot = ParkingLot("Downtown Parking", strategy)

    # Add floors with spots
    floor0 = ParkingFloor(0)
    floor0.add_spot(CompactSpot(1))
    floor0.add_spot(CompactSpot(2))
    floor0.add_spot(LargeSpot(3))
    floor0.add_spot(BikeSpot(4))
    lot.add_floor(floor0)

    # Park vehicles
    car = Car("KA-01-1234")
    ticket = lot.park_vehicle(car)
    print(f"Parked car, ticket #{ticket.ticket_id}")

    bike = Bike("KA-02-5678")
    ticket2 = lot.park_vehicle(bike)
    print(f"Parked bike, ticket #{ticket2.ticket_id}")

    # Unpark
    amount = lot.unpark_vehicle(ticket.ticket_id)
    print(f"Payment: Rs {amount}")


if __name__ == "__main__":
    main()
