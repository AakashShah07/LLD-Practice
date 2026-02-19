from parking_lot import ParkingLot
from models.vehicle import Car, Bike, Truck
from models.parking_spot import CompactSpot, LargeSpot, BikeSpot
from models.parking_floor import ParkingFloor
from strategy.parking_strategy import NearestFirstStrategy


def main():
    # Initialize parking lot with nearest-first strategy
    strategy = NearestFirstStrategy()
    lot = ParkingLot("Downtown Parking", strategy)

    # Floor 0: 2 compact, 1 large, 1 bike spot
    floor0 = ParkingFloor(0)
    floor0.add_spot(CompactSpot(1))
    floor0.add_spot(CompactSpot(2))
    floor0.add_spot(LargeSpot(3))
    floor0.add_spot(BikeSpot(4))
    lot.add_floor(floor0)

    # Floor 1: 1 compact, 2 large spots
    floor1 = ParkingFloor(1)
    floor1.add_spot(CompactSpot(5))
    floor1.add_spot(LargeSpot(6))
    floor1.add_spot(LargeSpot(7))
    lot.add_floor(floor1)

    lot.display_status()

    # Park vehicles
    print("\n--- Parking vehicles ---")
    car1 = Car("KA-01-1234")
    t1 = lot.park_vehicle(car1)
    print(f"Parked: {t1}")

    car2 = Car("KA-01-5678")
    t2 = lot.park_vehicle(car2)
    print(f"Parked: {t2}")

    bike1 = Bike("KA-02-9999")
    t3 = lot.park_vehicle(bike1)
    print(f"Parked: {t3}")

    truck1 = Truck("KA-03-4444")
    t4 = lot.park_vehicle(truck1)
    print(f"Parked: {t4}")

    lot.display_status()

    # Unpark a car
    print("\n--- Unparking car1 ---")
    amount = lot.unpark_vehicle(t1.ticket_id)
    print(f"Payment for ticket #{t1.ticket_id}: Rs {amount}")

    lot.display_status()

    # Try parking a truck when only compact/bike spots left on floor 0
    print("\n--- Parking another truck ---")
    truck2 = Truck("KA-03-7777")
    t5 = lot.park_vehicle(truck2)
    print(f"Parked: {t5}")

    lot.display_status()


if __name__ == "__main__":
    main()
