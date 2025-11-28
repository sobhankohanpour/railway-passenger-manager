# 🚆 Railway Passenger Manager

![License](https://img.shields.io/github/license/sobhankohanpour/railway-passenger-manager)
![Last Commit](https://img.shields.io/github/last-commit/sobhankohanpour/railway-passenger-manager)
![Issues](https://img.shields.io/github/issues/sobhankohanpour/railway-passenger-manager)
![Pull Requests](https://img.shields.io/github/issues-pr/sobhankohanpour/railway-passenger-manager)

![Repo Size](https://img.shields.io/github/repo-size/sobhankohanpour/railway-passenger-manager)
![Code Size](https://img.shields.io/github/languages/code-size/sobhankohanpour/railway-passenger-manager)
![Contributors](https://img.shields.io/github/contributors/sobhankohanpour/railway-passenger-manager)
![Forks](https://img.shields.io/github/forks/sobhankohanpour/railway-passenger-manager)
![GitHub Stars](https://img.shields.io/github/stars/sobhankohanpour/railway-passenger-manager)

A Python-based simulation system for creating and managing train trips, passengers, and cargo capacity.
This project demonstrates clean OOP design using **Train**, **TrainTrip**, and **Passenger** classes with proper validation on origin/destination cities, passenger assignment rules, and remaining cargo calculations.

---

### 📌 Repository Features

| Feature                      | Description                                 |
| ---------------------------- | ------------------------------------------- |
| 🔹 Train availability check  | Ensures train is not already on a trip      |
| 🔹 City validation system    | Only registered cities are accepted         |
| 🔹 Passenger weight handling | Prevents overload based on train capacity   |
| 🔹 OOP-driven structure      | Clean, extensible, class-based architecture |
| 🔹 Callable trip instance    | Returns remaining cargo capacity instantly  |

---

### 📌 Repository Structure

The project is organized with a `src` directory containing the main module `railway.py`, which implements the core classes—`Train`, `TrainTrip`, and `Passenger`. The `README.md` sits at the root, providing documentation, usage examples, and guidance for working with the module.

```text
railway-passenger-manager/
│── src/
│   └── railway.py         # Core classes: Train, TrainTrip, Passenger
└── README.md              # Project documentation and usage examples
```

---

### 🧠 Object Model

#### **Train**

Stores train status, last station visited, maximum cargo weight, and trip availability.

#### **TrainTrip**

Validates origin city, destination, train availability, handles passengers, and returns remaining cargo capacity.

#### **Passenger**

Each passenger has a cargo load and can join or leave a trip if weight conditions allow.

---

### 🏗 Class Diagram (Conceptual)

```
TrainTrip ──> Train
│
└── passengers[] ──> Passenger
```

---

### 📍 Supported Cities

The system supports **30 major railway-compatible cities**, including:
`Tehran, Isfahan, Mashhad, Shiraz, Yazd, Rasht, Tabriz, Sanandaj, and 22 more cities defined in the code.`

---

### ⚙ How to Use

```bash
git clone https://github.com/sobhankohanpour/railway-passenger-manager.git
cd railway-passenger-manager
python src/railway.py
```

> Python 3.10+ recommended.

---

### 🔥 Usage Example

Below is a minimal example demonstrating how to create a train trip, add passengers, check remaining cargo capacity, and manage passengers:

```python
from src.railway import Train, TrainTrip, Passenger

# 1) Create a train
train = Train(
    last_station="Sanandaj",
    max_cargo_weight=34286,
    on_trip=False
)

# 2) Initialize a trip (origin must match train.last_station)
trip = TrainTrip(
    origin_city="Sanandaj",
    destination_city="Rasht",
    train=train
)

# 3) Create passengers
p1 = Passenger("Ali Saeedi", 616)
p2 = Passenger("Abolfazl Zandi", 349)

# 4) Check remaining cargo capacity
print(trip())  # ➜ 34286

# 5) Add passengers to trip
p1.join_trip(trip)
p2.join_trip(trip)

# 6) Remaining cargo after boarding
print(trip())  # ➜ 34286 - (616 + 349) = 33321

# 7) Remove a passenger if needed
p2.leave_trip(trip)

print(trip())  # ➜ 34286 - 616 = 33670
```

---

### 🧪 Future Improvements

* Expand dataset of cities + station connectivity graph
* Add ticketing & pricing system
* Implement admin dashboard (CLI or Web UI)
* Optional logging, persistence, or database integration
* API version using FastAPI or Django REST

---

### 📜 License

MIT License — Feel free to use and extend this project.
