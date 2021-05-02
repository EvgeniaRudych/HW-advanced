# 1. Create a class hierarchy of animals with at least 5 animals that have additional methods each,
# create an instance for each of the animal and call the unique method for it.
# Determine if each of the animal is an instance of the Animals class.
from abc import abstractmethod, ABC


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    """
    Parent class, should have eat, sleep
    """

    def eat(self):
        print(f"A(n) {self.__class__.__name__} called {self.name} is eating.")

    def sleep(self):
        print(f"A(n) {self.__class__.__name__}  called {self.name} is sleeping zzz....")


class Dog(Animal):
    def __init__(self, breed, name, age):
        super().__init__(name, age)
        self.breed = breed

    def breed_name(self):
        print(f" I am {self.breed} dog called {self.name}.")


class Goat(Animal):
    def milking(self):
        print(f"{self.name} the goat is being milked!")


class Horse(Animal):
    def __init__(self, colour, characteristics, name, age):
        super().__init__(name, age)
        self.colour = colour
        self.characteristics = characteristics

    def about_horse(self):
        print(f"I am a {self.characteristics} called {self.name}. My colour is {self.colour} and I am {self.age} y. o.")


class Shark(Animal):
    def swimming(self):
        print(f" {self.name} the shark is swimming")

    def hunting(self):
        print(f"{self.name} the shark is looking for its dinner")


class Lizard(Animal):
    def crawling(self):
        print(f"{self.name} the lizard is crawling carefully")


dog = Dog('Dachshund', 'Patrick', 2)
goat = Goat('Zelda', 4)
horse = Horse('black', 'pony', 'Ronda', 7)
shark = Shark('Joe', 5)
lizard = Lizard('Mario', 1)

dog.breed_name()
dog.eat()
goat.milking()
goat.sleep()
horse.about_horse()
shark.hunting()
shark.swimming()
lizard.crawling()

for item in (dog, goat, horse, shark, lizard):
    print(isinstance(item, Animal))


# 1.a. Create a new class Human and use multiple inheritance to create Centaur class,
#  create an instance of Centaur class and call the common method of these classes and unique.

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introducing(self):
        print(f" I am {self.name}. I am {self.age} y. o.")


class Centaur(Human, Animal):

    def running(self):
        print(f"{self.name} is running with other centaurs.")


centaur = Centaur('Charon', 50)

centaur.eat()
centaur.introducing()
centaur.running()


# 2. Create two classes: Person, Cell Phone, one for composition, another one for aggregation.

class Person:
    def __init__(self):
        arm1 = Arm("Beckoning")
        arm2 = Arm("Pointing")


class Arm:
    def __init__(self, gesture):
        self.gesture = gesture


person1 = Person()


class CellPhone:
    def __init__(self, screen):
        self.screen = screen


class Screen:
    def __init__(self):
        pass


screen = Screen
cell_phone = CellPhone(Screen)

3.
"""
Create regular class taking 8 params on init - name, last_name, phone_number, address, email, birthday, age, sex
Override a printable string representation of Profile class and return: list of the params mentioned above
"""


class Profile:
    def __init__(self, name, last_name, phone_number, address, email, birthday, age, sex):
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age
        self.sex = sex
        self.parameters = [name, last_name, phone_number, address, email,
                           birthday, age, sex]

    def __str__(self):
        return str(self.parameters)


my_profile = Profile('Evgenia', 'Rudych', '0508751444', 'Sobornosti avenue', 'yevheniia.rudych.ukma.edu.ua', '28.04.02',
                     '19', 'female')
print(my_profile)


# 4.* Create an interface for the Laptop with the next methods: Screen, Keyboard, Touchpad, WebCam, Ports, Dynamics
# and create an HPLaptop class by using your interface.

class Laptop(ABC):

    @abstractmethod
    def screen(self):
        raise NotImplementedError

    @abstractmethod
    def keyboard(self):
        raise NotImplementedError

    @abstractmethod
    def touchpad(self):
        raise NotImplementedError

    @abstractmethod
    def webcam(self):
        raise NotImplementedError

    @abstractmethod
    def ports(self):
        raise NotImplementedError

    @abstractmethod
    def dynamics(self):
        raise NotImplementedError


class HPLaptop(Laptop):
    def __init__(self, laptop_screen, laptop_keyboard, laptop_touchpad, laptop_webcam, laptop_ports, laptop_dynamics):
        self.laptop_screen = laptop_screen
        self.laptop_keyboard = laptop_keyboard
        self.laptop_touchpad = laptop_touchpad
        self.laptop_webcam = laptop_webcam
        self.laptop_ports = laptop_ports
        self.laptop_dynamics = laptop_dynamics

    def screen(self):
        print(f" The laptop's screen is {self.laptop_screen}")

    def keyboard(self):
        print(f"Laptop's keyboard is {self.laptop_keyboard}")

    def touchpad(self):
        print(f"Laptop's touchpad is {self.laptop_touchpad}")

    def webcam(self):
        print(f"Laptop's webcam is {self.laptop_webcam}")

    def ports(self):
        print(f"Laptop's ports are {self.laptop_ports}")

    def dynamics(self):
        print(f"Laptop's dynamics are {self.laptop_dynamics}")

hplaptop15s = HPLaptop('IPS', 'without backlight', 'buttonless', '5 MP', 'USB 3.1', 'Genius SP-Q160')

hplaptop15s.screen()
hplaptop15s.keyboard()
hplaptop15s.touchpad()
hplaptop15s.webcam()
hplaptop15s.ports()
hplaptop15s.dynamics()