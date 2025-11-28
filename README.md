# 🚆 Railway Passenger Manager

A Python-based simulation system for creating and managing train trips, passengers, and cargo capacity.  
This project demonstrates clean OOP design using **Train**, **TrainTrip**, and **Passenger** classes with proper validation on origin/destination cities, passenger assignment rules, and remaining cargo calculations.


### 📌 Repository Features

| Feature | Description |
|--------|-------------|
| 🔹 Train availability check | Ensures train is not already on a trip |
| 🔹 City validation system | Only registered cities are accepted |
| 🔹 Passenger weight handling | Prevents overload based on train capacity |
| 🔹 OOP-driven structure | Clean, extensible, class-based architecture |
| 🔹 Callable trip instance | Returns remaining cargo capacity instantly |

### 🧠 Object Model

#### **Train**
Stores train status, last station visited, maximum cargo weight and trip availability.

#### **TrainTrip**
Validates origin city, destination, train availability, handles passengers, and returns remaining capacity.

#### **Passenger**
Each passenger owns a cargo load and can join or leave a trip if weight condition allows.


### 🏗 Class Diagram (Conceptual)

```

TrainTrip ──> Train
│
└── passengers[] ──> Passenger

````


### 📍 Supported Cities

The system includes **30 major railway-compatible cities** such as:  
`Tehran, Isfahan, Mashhad, Shiraz, Yazd, Rasht, Tabriz, Sanandaj ...`


### ⚙ How to Use

```bash
git clone https://github.com/sobhankohanpour/railway-passenger-manager.git
cd railway-passenger-manager
python railway.py
````

> Python 3.13+ recommended.


### 🔥 Usage Example

```python

```


### 🧪 Future Improvements

* Expand dataset of cities + station connectivity graph
* Add ticketing & pricing system
* Implement admin dashboard (CLI or Web UI)
* Optional logging, persistence or database integration
* API version using FastAPI or Django REST


### 📜 License

MIT License — Feel free to use and extend this project.
