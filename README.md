# Low-Level Design (LLD) Practice

A collection of Low-Level Design problems implemented from scratch in **Python**, focusing on clean architecture, SOLID principles, and common design patterns.

## Why LLD?

Low-Level Design is about translating high-level requirements into well-structured, maintainable, and extensible code. It tests your ability to:

- Break down a system into classes and their relationships
- Apply OOP concepts — Abstraction, Encapsulation, Inheritance, Polymorphism
- Use the right design patterns at the right place
- Write code that is easy to extend without modification (Open/Closed Principle)

## Problems

| # | Problem | Design Patterns | Status |
|---|---------|----------------|--------|
| 1 | [Parking Lot System](ParkingSystem/) | Singleton, Strategy, Inheritance | Completed |

## Design Patterns Covered

| Pattern | Type | Used In |
|---------|------|---------|
| Singleton | Creational | Parking Lot |
| Strategy | Behavioral | Parking Spot Assignment |
| Factory | Creational | — |
| Observer | Behavioral | — |
| State | Behavioral | — |
| Chain of Responsibility | Behavioral | — |

## Project Structure

Each problem follows a consistent modular layout:

```
ProblemName/
├── main.py                  # Entry point & demo
├── <core_class>.py          # Central orchestrator (e.g., ParkingLot)
├── enums/                   # Enums and constants
├── models/                  # Core entities and data classes
└── strategy/                # Strategy/behavioral patterns
```

## Key Concepts Practiced

- **SOLID Principles** — Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion
- **OOP** — Abstract classes, polymorphism, composition over inheritance
- **Design Patterns** — Creational, Structural, and Behavioral
- **Clean Code** — Readable, modular, and self-documenting

## How to Run

```bash
cd ProblemName/
python main.py
```

## Roadmap

- [x] Parking Lot System
- [ ] Elevator System
- [ ] Tic Tac Toe
- [ ] Snake and Ladder
- [ ] Vending Machine
- [ ] Library Management System
- [ ] BookMyShow (Movie Ticket Booking)
- [ ] ATM System
- [ ] Chess

## Tech

- **Language:** Python 3.10+
- **No external dependencies** — pure OOP, no frameworks
