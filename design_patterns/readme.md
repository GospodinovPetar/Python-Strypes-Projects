# Design Patterns Cheatsheet

## 1. Builder
- **Purpose**: Separates the construction of a complex object from its representation.
- **When to use**: When constructing a complex object, especially when the object has many parameters.
- **Key Concept**: A builder class with methods to set parts of the object step-by-step.

### Example:
```python
class Car:
    def __init__(self, wheels, color, engine):
        self.wheels = wheels
        self.color = color
        self.engine = engine

class CarBuilder:
    def __init__(self):
        self.car = Car(4, "Red", "V8")
    
    def build_wheels(self, wheels):
        self.car.wheels = wheels
        return self
    
    def build_color(self, color):
        self.car.color = color
        return self
    
    def build_engine(self, engine):
        self.car.engine = engine
        return self
    
    def get_result(self):
        return self.car

builder = CarBuilder()
car = builder.build_color("Blue").build_engine("V6").get_result()
print(vars(car))  # {'wheels': 4, 'color': 'Blue', 'engine': 'V6'}
```
## 2. Factories
- **Purpose**: Provides an interface for creating objects in a super class but allows subclasses to alter the type of created objects.
- **When to use**: When the creation process is complex and depends on different factors.
- **Key Concept**: The use of factory methods or abstract factories.
```python
class Car:
    def drive(self):
        print("Driving a car")

class Truck:
    def drive(self):
        print("Driving a truck")

class VehicleFactory:
    @staticmethod
    def create_vehicle(vehicle_type):
        if vehicle_type == "Car":
            return Car()
        elif vehicle_type == "Truck":
            return Truck()

vehicle = VehicleFactory.create_vehicle("Car")
vehicle.drive()  # Output: Driving a car
```
## 3. Prototype
- **Purpose**: Creates new objects by copying an existing object, known as the prototype.
- **When to use**: When creating a new object is costly or complex.
- **Key Concept**: Cloning an existing instance instead of creating a new one.
```python
import copy
class Car:
    def __init__(self, model, engine):
        self.model = model
        self.engine = engine

    def clone(self):
        return copy.deepcopy(self)

original_car = Car("Tesla", "Electric")
cloned_car = original_car.clone()
print(cloned_car.model)  # Output: Tesla
```
## 4. Singleton
- **Purpose**: Ensures a class has only one instance and provides a global point of access to it.
- **When to use**: When you need to control access to shared resources (e.g., database connections).
- **Key Concept**: A private constructor and a static method to return the instance.
```python
class Singleton:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

singleton1 = Singleton()
singleton2 = Singleton()
print(singleton1 is singleton2)  # Output: True
```
## 5. Adapter
- **Purpose**: Allows incompatible interfaces to work together.
- **When to use**: When you need to integrate two incompatible interfaces.
- **Key Concept**: An adapter class that wraps the existing interface to make it compatible with the desired interface.
```python
class EuropeanSocket:
    def plug_in(self):
        print("Plugged into European socket.")

class AmericanSocket:
    def plug_in(self):
        print("Plugged into American socket.")

class Adapter:
    def __init__(self, socket):
        self.socket = socket

    def plug_in(self):
        self.socket.plug_in()

european_socket = EuropeanSocket()
adapter = Adapter(european_socket)
adapter.plug_in()  # Output: Plugged into European socket.
```
## 6. Bridge
- **Purpose**: Separates an abstraction from its implementation so that both can be modified independently.
- **When to use**: When you need to decouple an abstraction from its implementation to allow both to evolve separately.
- **Key Concept**: An abstraction class that delegates its work to an implementation class.
```python
class Engine:
    def start(self):
        raise NotImplementedError

class PetrolEngine(Engine):
    def start(self):
        print("Starting petrol engine")

class DieselEngine(Engine):
    def start(self):
        print("Starting diesel engine")

class Car:
    def __init__(self, engine: Engine):
        self.engine = engine

    def drive(self):
        self.engine.start()

car = Car(PetrolEngine())
car.drive()  # Output: Starting petrol engine
```
## 7. Composite
- **Purpose**: Composes objects into tree-like structures to represent part-whole hierarchies.
- **When to use**: When you want to treat individual objects and compositions of objects uniformly.
- **Key Concept**: A common interface for both single objects and compositions.
```python
class Component:
    def operation(self):
        pass

class Leaf(Component):
    def operation(self):
        print("Leaf operation")

class Composite(Component):
    def __init__(self):
        self.children = []

    def add(self, component):
        self.children.append(component)

    def operation(self):
        for child in self.children:
            child.operation()

leaf = Leaf()
composite = Composite()
composite.add(leaf)
composite.operation()  # Output: Leaf operation
```
## 8. Decorator
- **Purpose**: Allows you to add behavior to an object dynamically.
- **When to use**: When you want to extend the functionality of objects in a flexible and reusable way.
- **Key Concept**: A decorator class that wraps the original object and adds new functionality.
```python
class Car:
    def drive(self):
        print("Driving a car")

class CarDecorator:
    def __init__(self, car: Car):
        self.car = car

    def drive(self):
        self.car.drive()
        print("Adding a turbo boost!")

car = Car()
decorated_car = CarDecorator(car)
decorated_car.drive()  # Output: Driving a car
```
## 9. Façade
- **Purpose**: Provides a simplified interface to a complex subsystem.
- **When to use**: When you want to provide a simple interface to a complex system.
- **Key Concept**: A facade class that delegates client requests to the appropriate subsystem components.
```python
class Engine:
    def start(self):
        print("Engine started")

class Lights:
    def turn_on(self):
        print("Lights turned on")

class CarFacade:
    def __init__(self):
        self.engine = Engine()
        self.lights = Lights()

    def start_car(self):
        self.engine.start()
        self.lights.turn_on()

car = CarFacade()
car.start_car()  # Output: Engine started
```