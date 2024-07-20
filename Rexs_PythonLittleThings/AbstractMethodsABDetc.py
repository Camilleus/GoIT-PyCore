# abstrakcyjne klasy bazowe
import random
from time import time, sleep
import requests
import decimal
from abc import ABC, abstractmethod


class MyAbstractClass(ABC):
    @abstractmethod
    def foo(self):
        raise NotImplementedError()

    @abstractmethod
    def bar(self):
        raise NotImplementedError()

    def hehe(self):
        print("hehe")


class MySubclass(MyAbstractClass):
    def foo(self):
        print("ohyda...")

    def bar(self):
        print("piwko ;)")


my_object = MySubclass()
# my_object.foo()
# my_object.bar()
# my_object.hehe()


class User:
    pass


class AbstractUserRepository(ABC):
    @abstractmethod
    def get_all_users(self) -> list[User]:
        raise NotImplementedError

    @abstractmethod
    def get_a_user(self, user_id) -> User:
        raise NotImplementedError


class PSQLUserRepository(AbstractUserRepository):
    def get_all_users(self) -> list[User]:
        return [User(), User()]

    def get_a_user(self, user_id) -> User:
        return User()


class MongoUserRepository(AbstractUserRepository):
    def get_all_users(self) -> list[User]:
        return [User(), User()]

    def get_a_user(self, user_id) -> User:
        return User()


# fabryka abstrakcyjna


class PdfMonthReport:
    pass


class PdfQuarterReport:
    pass


class PdfYearReport:
    pass


class HtmlMonthReport:
    pass


class HtmlQuarterReport:
    pass


class HtmlYearReport:
    pass


class CsvMonthReport:
    pass


class CsvQuarterReport:
    pass


class CsvYearReport:
    pass


class AbstractReport(ABC):

    @abstractmethod
    def create_month_report(self):
        pass

    @abstractmethod
    def create_quarter_report(self):
        pass

    @abstractmethod
    def create_year_report(self):
        pass


class PdfReport(AbstractReport):
    def create_month_report(self):
        return PdfMonthReport()

    def create_quarter_report(self):
        return PdfQuarterReport()

    def create_year_report(self):
        return PdfYearReport()


class HtmlReport(AbstractReport):

    def create_month_report(self):
        return HtmlMonthReport()

    def create_quarter_report(self):
        return HtmlQuarterReport()

    def create_year_report(self):
        return HtmlYearReport()


class CsvReport(AbstractReport):

    def create_month_report(self):
        return CsvMonthReport()

    def create_quarter_report(self):
        return CsvQuarterReport()

    def create_year_report(self):
        return CsvYearReport()


def create_important_report(report_factory: AbstractReport):
    important_report = report_factory.create_quarter_report()
    important_report.process()
    print(f"STWORZYŁAM {type(important_report)} RAPORT!!!")


# create_important_report(HtmlReport())
# create_important_report(PdfReport())
# create_important_report(CsvReport())

# metoda wytwórcza


class SendingMessages(ABC):
    @abstractmethod
    def sending(self) -> str:
        pass


class Creator(ABC):
    @abstractmethod
    def create(self) -> SendingMessages:
        pass

    def send_messages(self) -> str:
        product = self.create()
        result = product.sending()
        return result


class SendingSMSMessages(SendingMessages):
    def sending(self) -> str:
        return "SMS mailing has been completed"


class CreatorSMS(Creator):
    def create(self) -> SendingMessages:
        return SendingSMSMessages()


class SendingPushMessages(SendingMessages):
    def sending(self) -> str:
        return "Push mailing has been completed"


class CreatorPush(Creator):
    def create(self) -> SendingMessages:
        return SendingPushMessages()


def client_code(creator: Creator) -> None:
    print("We know nothing about the creator code that works")
    result = creator.send_messages()
    print(f"Result: {result}")

# print("The application performs SMS mailing.")
# client_code(CreatorSMS())
# client_code(CreatorPush())


class TreatmentPlan(ABC):
    @abstractmethod
    def do_treatment(self):
        pass


class MedicialCreator(ABC):
    @abstractmethod
    def create(self) -> TreatmentPlan:
        pass

    def order_treatment(self):
        product = self.create()
        product.do_treatment()


class SurgeryPlan(TreatmentPlan):
    def do_treatment(self):
        print("WYKONUJĘ OPERACJĘ")


class SurgeryCreator(MedicialCreator):
    def create(self):
        return SurgeryPlan()


class MedicinePlan(TreatmentPlan):
    def do_treatment(self):
        print("Podaję leki")


class MedicineCreator(MedicialCreator):
    def create(self):
        return MedicinePlan()


def execute_treatment(creator: MedicialCreator):
    creator.order_treatment()

# execute_treatment(MedicineCreator())
# execute_treatment(SurgeryCreator())

# singleton


class Singleton:
    """Classic singleton"""

    __instance = None

    # def __init__(self):
    #     self.number = random.randint(1, 10)

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(Singleton)
            cls.__instance.number = random.randint(1, 10)
        return cls.__instance


# singleton = Singleton()
# print(id(singleton))
# print(singleton.number)
# singleton = Singleton()
# print(id(singleton))
# print(singleton.number)
# singleton = Singleton()
# print(id(singleton))
# print(singleton.number)

# fasada


class CurrencyProvider:
    def _get_json_from_url(self):
        return requests.get('https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=11').json()

    def get_EUR_buy_value_in_hryvnias(self, quantity):
        return decimal.Decimal(self._get_json_from_url()[0]["buy"]) * quantity


currency_provider = CurrencyProvider()
# eur_buy_value = currency_provider.get_EUR_buy_value_in_hryvnias(10)
# print(eur_buy_value)

# adapter


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age
        }


class Owner:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.animals = []

    def adopt_animal(self, animal_info):
        self.animals.append(
            f"{animal_info['animal_name']}, {animal_info['age_in_months']}")


def adapt_dog_for_owner(dog: Dog) -> dict:
    return {"animal_name": dog.to_dict()["name"], "age_in_months": dog.to_dict()["age"] * 12}


tali = Dog(name="Tali", age=13)
krzysiek = Owner(name="Krzysiek", age="tajemnica")
krzysiek.adopt_animal(adapt_dog_for_owner(tali))
# print(krzysiek.animals)

# pełnomocnik


class Request(ABC):
    @abstractmethod
    def request(self) -> None:
        pass


class RealRequest(Request):
    def request(self) -> None:
        print("RealRequest: Handling request.")
        requests.get(
            'https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=11')


class Proxy(Request):
    def __init__(self, real_request) -> None:
        self._real_request = real_request
        self.start = None

    def request(self) -> None:
        self.start = time()
        self._real_request.request()
        self.log_access()

    def log_access(self) -> None:
        print(f"Proxy: Logging the time of request. {time() - self.start}")


def client_code(subject: Request) -> None:
    subject.request()


# client_code(Proxy(real_request=RealRequest()))


# polecenie

class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass


class Receiver:
    def createXMLOrder(self, text: str) -> None:
        print(f"Create XML order: {text} ")

    def send_email(self, text: str) -> None:
        print(f"Send email: {text} ")


class TestReceiver:
    def createXMLOrder(self, text: str) -> None:
        print("JESTEM TESTEM")

    def send_email(self, text: str) -> None:
        print("JESTEM TESTEM")


class CommandCreateXMLOrder(Command):
    def __init__(self, receiver: Receiver, text: str) -> None:
        self._receiver = receiver
        self._text = text

    def execute(self) -> None:
        self._receiver.createXMLOrder(self._text)


class CommandSendEmail(Command):
    def __init__(self, receiver: Receiver, html: str) -> None:
        self._receiver = receiver
        self._html = html

    def execute(self) -> None:
        self._receiver.send_email(self._html)


class Invoker:
    def __init__(self) -> None:
        self._commands = []

    def add_command(self, command: Command):
        self._commands.append(command)

    def send_and_create(self) -> None:
        for command in self._commands:
            command.execute()


def client():
    invoker = Invoker()
    invoker.add_command(CommandSendEmail(Receiver(), "Send email"))
    invoker.add_command(CommandSendEmail(Receiver(), "Send my email"))
    invoker.add_command(CommandSendEmail(TestReceiver(), "Send spam"))
    invoker.add_command(CommandSendEmail(TestReceiver(), "Send spam"))
    invoker.add_command(CommandCreateXMLOrder(Receiver(), "Save report"))
    invoker.send_and_create()

# client()

# obserwator


class Publisher(ABC):
    @abstractmethod
    def attach(self, observer):
        pass

    @abstractmethod
    def detach(self, observer):
        pass

    @abstractmethod
    def notify(self):
        pass


class Observer(ABC):
    @abstractmethod
    def update(self, publisher):
        pass


class PublisherMessages(Publisher):
    _observers = []
    latest_message = ""
    # _indicator = 0

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)

    def business_logic_execution(self, message):
        print(f"Application logic is being executed.")
        # self._indicator += 1
        self.latest_message = message
        self.notify()


class ConcreteObserver(Observer):
    def update(self, publisher):
        print("ZOSTAŁEM POWIADOMIONY O:", publisher.latest_message)


class PessimistObserver(Observer):
    def update(self, publisher):
        if publisher.latest_message == "SYTUACJA NA RYNKU ŚWIŃ TRAGICZNA":
            print("ZOSTAŁEM POWIADOMIONY O:", publisher.latest_message)
            print("OLABOGA!")


observer_1 = ConcreteObserver()
observer_2 = PessimistObserver()
observer_3 = ConcreteObserver()
publisher = PublisherMessages()
for observer in [observer_1, observer_2, observer_3]:
    publisher.attach(observer)
publisher.business_logic_execution("SYTUACJA NA RYNKU ŚWIŃ BEZ ZMIAN")
publisher.business_logic_execution("SYTUACJA NA RYNKU ŚWIŃ TRAGICZNA")
publisher.business_logic_execution("SYTUACJA NA RYNKU ŚWIŃ NORMUJE SIĘ")
