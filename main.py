class Plane:
    def __init__(self, name):
        self.__name = name
        self.__flights = []

    @property
    def name(self):
        return self.__name

    @property
    def flights(self):
        return self.__flights

    def __str__(self):
        return f"Самолет авиакомпании: {self.name}"

    def add_flight(self, flight):
        self.__flights.append(flight)


class Flight:
    def __init__(self, origin, destination, plane):
        self.__origin = origin
        self.__destination = destination
        self.__plane = plane
        self.__tickets = []

    @property
    def origin(self):
        return self.__origin

    @property
    def destination(self):
        return self.__destination

    @property
    def plane(self):
        return self.__plane

    @property
    def tickets(self):
        return self.__tickets

    def __str__(self):
        return f"Рейс из {self.origin} в {self.destination} на самолете авиакомпании {self.plane.name}"

    def add_ticket(self, ticket):
        self.__tickets.append(ticket)


class Ticket:
    def __init__(self):
        return

    def __str__(self):
        return


def create_plane():
    return


def create_flight():
    return


def create_ticket():
    return


def menu():
    plane = None
    flight = None
    ticket = None

    while True:
        print("\nМеню:")
        print("1. Создать самолет")
        print("2. Создать рейс")
        print("3. Создать билет")
        print("4. Вывести информацию о самолете")
        print("5. Вывести информацию о рейсе")
        print("6. Вывести информацию о билете")
        print("7. Выход из программы")

        point = input("Выберите пункт меню: ")

        if point == "1":
            pass
        elif point == "2":
            pass
        elif point == "3":
            pass
        elif point == "4":
            pass
        elif point == "5":
            pass
        elif point == "6":
            pass
        elif point == "7":
            pass
        else:
            pass


if __name__ == "main":
    menu()