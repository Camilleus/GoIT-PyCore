import requests
from math import pi

# - Single responsibility — zasada jednej odpowiedzialności


class Address:
    def __init__(self, zip, city, street):
        self.zip = zip
        self.city = city
        self.street = street

    def get_display_format(self):
        return f'{self.city}, {self.zip}, {self.street}'


class Occupation:
    def __init__(self, title, salary):
        self.title = title
        self._salary = salary

    @property
    def salary(self):
        return self._salary / 1.23


class Person:
    def __init__(self, name, last_name, address, occupation):
        self.name = name
        self.last_name = last_name
        self.address = address
        self.occupation = occupation

    def get_address(self):
        return self.address.get_display_format()

    def get_salary(self):
        return self.occupation.salary


person = Person('Aleksander', 'Aleksandrowski',
                Address('36007', 'Poznan', 'European, 28'))
# print(person.get_address())

# - Open-closed — zasada otwarte/zamknięte


class Rect:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return self.radius ** 2 * pi


def total_area(shapes):
    sum = 0
    for el in shapes:
        sum += el.get_area()
    return sum


# shapes = [Rect(10, 10), Circle(5), Rect(4, 5), Rect(3, 3)]
# area = total_area(shapes)
# print(area)

# - Liskov substitution — zasada podstawienia autorstwa Barbary Liskov

class Dog:
    def __init__(self, name, age, bark_loudness):
        self.name = name
        self.age = age
        self.bark_loudness = bark_loudness

    def bark(self):
        print("Bark" + "!" * self.bark_loudness)


class Retriever(Dog):
    def __init__(self, name, age, bark_loudness):
        super().__init__(name, age, bark_loudness)

    def bark(self):
        return "Bark bark!"


dogs = [Dog("Tali", 13, 2), Retriever("Wafel", 4, 3)]
for dog in dogs:
    dog.bark()


# - Interface segregation — zasada segregacji interfejsów

class CodeProducer:
    def write_code(self):
        pass


class PizzaEater:
    def eat_pizza(self, slice_count):
        pass


class OfficeProgrammer(CodeProducer, PizzaEater):
    def __init__(self, name):
        self.name = name

    def eat_pizza(self, slice_count):
        print(f'{self.name} eat {slice_count} slice pizza!')

    def write_code(self):
        print(f'{self.name} write code!')


class OfficeTester(PizzaEater):
    ...


class RemoteProgrammer(CodeProducer):
    def __init__(self, name):
        self.name = name

    def write_code(self):
        print(f'{self.name} write code!')


tester = OfficeTester()
o_program = OfficeProgrammer("Joe")
r_program = RemoteProgrammer("Jane")


# - Dependency inversion — zasada odwrócenia zależności


class RequestConnection:
    def __init__(self, request):
        self.request = request

    def get_json_from_url(self, url):
        return self.request.get(url).json()


class LoggingRequestConnection(RequestConnection):

    def get_json_from_url(self, url):
        print("GET request to url: ", url)
        return self.request.get(url).json()


class TestRequestConnection(RequestConnection):
    def get_json_from_url(self, url):
        return [{'ccy': 'EUR', 'base_ccy': 'UAH', 'buy': '10', 'sale': '10'}, {'ccy': 'USD', 'base_ccy': 'UAH', 'buy': '10', 'sale': '10'}]


class ApiClient:
    def __init__(self, fetch: RequestConnection):
        self.fetch = fetch

    def get_data(self, url):
        response = self.fetch.get_json_from_url(url)
        return response


def data_adapter(data: dict):
    return [{f"{el.get('ccy')}": {"buy": float(el.get('buy')), "sale": float(el.get('sale'))}} for el in data]


def pretty_view(data):
    pattern = '|{:^10}|{:^10}|{:^10}|'
    print(pattern.format('currency', 'sale', 'buy'))
    for el in data:
        currency, *_ = el.keys()
        buy = el.get(currency).get('buy')
        sale = el.get(currency).get('sale')
        print(pattern.format(currency, sale, buy))


if __name__ == '__main__':
    # fetch_method = TestRequestConnection(None)
    fetch_method = LoggingRequestConnection(requests)
    api_client = ApiClient(fetch_method)

    data = api_client.get_data(
        'https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=11')
    print(data)
    # pretty_view(data_adapter(data))
