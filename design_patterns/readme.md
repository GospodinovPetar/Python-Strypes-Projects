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
## 10. Flyweight
- **Purpose**: Reduces the cost of creating and maintaining a large number of similar objects by sharing common parts.
- **When to use**: When there are a large number of fine-grained objects that share the same state.
- **Key Concept**: Shared immutable state and the use of a factory to manage shared instances.
```python
class Flyweight:
    def __init__(self, state):
        self.state = state

class FlyweightFactory:
    _flyweights = {}

    @staticmethod
    def get_flyweight(state):
        if state not in FlyweightFactory._flyweights:
            FlyweightFactory._flyweights[state] = Flyweight(state)
        return FlyweightFactory._flyweights[state]

flyweight1 = FlyweightFactory.get_flyweight("State1")
flyweight2 = FlyweightFactory.get_flyweight("State1")
print(flyweight1 is flyweight2)  # Output: True
```
## 11. Proxy
- **Purpose**: Provides a surrogate or placeholder for another object.
- **When to use**: When you need to control access to an object or add additional functionality.
- **Key Concept**: A proxy class that controls access to the real object.
```python
class RealSubject:
    def request(self):
        print("Real subject handling request")

class Proxy:
    def __init__(self, real_subject):
        self.real_subject = real_subject

    def request(self):
        print("Proxy handling request")
        self.real_subject.request()

real_subject = RealSubject()
proxy = Proxy(real_subject)
proxy.request()  # Output: Proxy handling request
                 # Real subject handling request
```
## 12. Chain of Responsobility
- **Purpose**: Allows a request to be passed along a chain of handlers, where each handler can either process the request or pass it on.
- **When to use**: When you have a chain of objects that can handle a request in a flexible way.
- **Key Concept**: A chain of handler objects, each with a reference to the next.
```python
class Handler:
    def __init__(self, successor=None):
        self.successor = successor

    def handle(self, request):
        if self.successor:
            self.successor.handle(request)

class ConcreteHandlerA(Handler):
    def handle(self, request):
        if request == "A":
            print("Handler A processed the request")
        elif self.successor:
            self.successor.handle(request)

class ConcreteHandlerB(Handler):
    def handle(self, request):
        if request == "B":
            print("Handler B processed the request")
        elif self.successor:
            self.successor.handle(request)

handler_chain = ConcreteHandlerA(ConcreteHandlerB())
handler_chain.handle("A")  # Output: Handler A processed the request
```
## 13. Command
- **Purpose**: Encapsulates a request as an object, allowing you to parameterize clients with queues, requests, and operations.
- **When to use**: When you want to decouple the sender and receiver of a request.
- **Key Concept**: Command objects that encapsulate actions.
### Example:
```python
class Command:
    def execute(self):
        pass

class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light
    
    def execute(self):
        self.light.turn_on()

class Light:
    def turn_on(self):
        print("Light is on")

class RemoteControl:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command
    
    def press_button(self):
        self.command.execute()

light = Light()
light_on = LightOnCommand(light)
remote = RemoteControl()
remote.set_command(light_on)
remote.press_button()  # Output: Light is on
```
## 14. Interpreter
- **Purpose**: Defines a grammatical representation for a language and an interpreter to interpret sentences in that language.
- **When to use**: When you have a language to interpret (e.g., expressions or command syntax).
- **Key Concept**: An abstract syntax tree (AST) and an interpreter class.
```python
class Expression:
    def interpret(self, context):
        pass

class TerminalExpression(Expression):
    def __init__(self, data):
        self.data = data

    def interpret(self, context):
        return self.data in context

class OrExpression(Expression):
    def __init__(self, expr1, expr2):
        self.expr1 = expr1
        self.expr2 = expr2

    def interpret(self, context):
        return self.expr1.interpret(context) or self.expr2.interpret(context)

# Usage
context = "Hello World"
expr1 = TerminalExpression("Hello")
expr2 = TerminalExpression("Hi")
or_expr = OrExpression(expr1, expr2)
print(or_expr.interpret(context))  # Output: True (since "Hello" is in context)
```
## 15. Iterator
- **Purpose**: Provides a way to access elements of a collection without exposing its underlying representation.
- **When to use**: When you want to provide a way to iterate over elements of a collection.
- **Key Concept**: An iterator object that keeps track of the position in the collection.
```python
class ListIterator:
    def __init__(self, collection):
        self.collection = collection
        self.index = 0

    def has_next(self):
        return self.index < len(self.collection)

    def next(self):
        item = self.collection[self.index]
        self.index += 1
        return item

class Collection:
    def __init__(self):
        self.items = []
    
    def add(self, item):
        self.items.append(item)

    def iterator(self):
        return ListIterator(self.items)

# Usage
collection = Collection()
collection.add("Item 1")
collection.add("Item 2")
iterator = collection.iterator()

while iterator.has_next():
    print(iterator.next())
# Output:
# Item 1
# Item 2
```
## 16. Mediator
- **Purpose**: Allows communication between objects without them referring to each other explicitly.
- **When to use**: When you need to reduce the dependencies between interacting objects.
- **Key Concept**: A mediator class that coordinates the interactions between objects.
```python
class Mediator:
    def send(self, message, colleague):
        pass

class ConcreteMediator(Mediator):
    def __init__(self, colleague1, colleague2):
        self.colleague1 = colleague1
        self.colleague2 = colleague2
        self.colleague1.set_mediator(self)
        self.colleague2.set_mediator(self)

    def send(self, message, colleague):
        if colleague == self.colleague1:
            self.colleague2.receive(message)
        elif colleague == self.colleague2:
            self.colleague1.receive(message)

class Colleague:
    def __init__(self, name):
        self.name = name
        self.mediator = None

    def set_mediator(self, mediator):
        self.mediator = mediator

    def send(self, message):
        print(f"{self.name} sends: {message}")
        self.mediator.send(message, self)

    def receive(self, message):
        print(f"{self.name} receives: {message}")

colleague1 = Colleague("Colleague 1")
colleague2 = Colleague("Colleague 2")
mediator = ConcreteMediator(colleague1, colleague2)

colleague1.send("Hello, Colleague 2")  
# Output: Colleague 1 sends: Hello, Colleague 2
# Colleague 2 receives: Hello, Colleague 2
```
## 17. Memento
- **Purpose**: Captures and externalizes an object's state so that it can be restored later.
- **When to use**: When you need to implement undo functionality or save the state of an object.
- **Key Concept**: A memento object that stores the state and an originator object that manages the state.
```python
class Memento:
    def __init__(self, state):
        self.state = state

class Originator:
    def __init__(self, state):
        self.state = state
    
    def save_state(self):
        return Memento(self.state)
    
    def restore_state(self, memento):
        self.state = memento.state
    
    def __str__(self):
        return f"Originator's current state: {self.state}"

# Usage
originator = Originator("State1")
print(originator)
memento = originator.save_state()
originator.state = "State2"
print(originator)
originator.restore_state(memento)
print(originator)  # Output: Originator's current state: State1
```
## 18. Observer
- **Purpose**: Allows an object to notify other objects when its state changes.
- **When to use**: When you have one-to-many dependencies between objects.
- **Key Concept**: Observers that register with a subject to receive notifications.
```python
class Observer:
    def update(self, state):
        pass

class ConcreteObserver(Observer):
    def __init__(self, name):
        self.name = name
    
    def update(self, state):
        print(f"{self.name} received update: {state}")

class Subject:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self, state):
        for observer in self._observers:
            observer.update(state)

# Usage
subject = Subject()
observer1 = ConcreteObserver("Observer 1")
observer2 = ConcreteObserver("Observer 2")
subject.add_observer(observer1)
subject.add_observer(observer2)

subject.notify_observers("New State")  
# Output:
# Observer 1 received update: New State
# Observer 2 received update: New State
```
## 19. State
- **Purpose**: Allows an object to alter its behavior when its internal state changes.
- **When to use**: When an object has different behaviors based on its internal state.
- **Key Concept**: A state object that encapsulates the state-specific behavior.
```python
class State:
    def handle(self):
        pass

class ConcreteStateA(State):
    def handle(self):
        print("State A handling the request")

class ConcreteStateB(State):
    def handle(self):
        print("State B handling the request")

class Context:
    def __init__(self):
        self.state = None

    def set_state(self, state):
        self.state = state

    def request(self):
        self.state.handle()

# Usage
context = Context()
state_a = ConcreteStateA()
state_b = ConcreteStateB()

context.set_state(state_a)
context.request()  # Output: State A handling the request

context.set_state(state_b)
context.request()  # Output: State B handling the request
```
## 20. Strategy
- **Purpose**: Defines a family of algorithms and makes them interchangeable at runtime.
- **When to use**: When you want to choose an algorithm at runtime and avoid hard-coding it.
- **Key Concept**: A strategy interface and concrete strategy classes.
```python
class Strategy:
    def execute(self, data):
        pass

class ConcreteStrategyA(Strategy):
    def execute(self, data):
        return f"Strategy A: {data}"

class ConcreteStrategyB(Strategy):
    def execute(self, data):
        return f"Strategy B: {data}"

class Context:
    def __init__(self, strategy):
        self.strategy = strategy
    
    def set_strategy(self, strategy):
        self.strategy = strategy
    
    def execute_strategy(self, data):
        return self.strategy.execute(data)

# Usage
context = Context(ConcreteStrategyA())
print(context.execute_strategy("Test"))  # Output: Strategy A: Test

context.set_strategy(ConcreteStrategyB())
print(context.execute_strategy("Test"))  # Output: Strategy B: Test
```