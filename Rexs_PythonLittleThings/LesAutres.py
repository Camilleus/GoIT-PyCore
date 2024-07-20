"""
lOGICAL VARIABLES



is_active = input("Is the user active? ")
is_admin = input("Is the user administrator? ")
is_permission = input("Does the user have access? ")

access = False
is_admin = False
is_active = False
is_permission = False

if access is 1:
    is_permission = True
else:
    is_permission = False

if is_admin is True:
    is_permission = True
    is_active = True
else:
    is_admin = False

if access is True and is_active is True:
    is_permission = True
    is_active = True
else:
    is_permission = False
    is_active = False

if is_permission is True:
    acces = True
else:
    acces = False





#SQUARE EQUATION


import math

a = int(input("Enter coefficient a: "))
b = int(input("Enter coefficient b: "))
c = int(input("Enter coefficient c: "))

D = b ** 2 - 4 * a * c

if D > 0:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
elif D == 0:
    x1 = (-b + math.sqrt(D)) / (2 * a)
else:
    D < 0





#GREATEST COMMON DIVISOR



first = int(input("Enter the first integer: "))
second = int(input("Enter the second integer: "))

gcd = int( first if first < second else second)
smaller = int( first if first < second else second)
bigger = int( first if first > second else second)

while bigger % gcd != 0 :
    gcd -= 1
    print(gcd)
    if bigger % int(gcd) == 0:
        if smaller % int(gcd) != 0:
            gcd -= 1
            print(gcd)
        else:
            print(gcd)





#CAESAR'S CODE



message = input("Enter a message: ")
offset = int(input("Enter the offset: "))
encoded_message = ""
for ch in message:
    letter = ""
    if not ch.isalpha():
        encoded_message += ch
        continue
    if 65 <= ord(ch) <= 90:
        letter = "A"
    else:
        letter = "a"
    pos = ord(ch) - ord(letter)
    pos = (pos + offset) % 26
    new_char = chr(pos + ord(letter))
    encoded_message += new_char     

#Factorial / Silnia


def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

factorial(5)# 120


#Sum of Consecutive Numbers 
import time
end = int(input("Hello! What's the number you want to see a consecutive number of? type it here: "))
start = int(input("Do you have a specific number to start with?(default is 0): "))
sum = 0

for x in range(start,end):
 x+=1
 sum+=x

print("This is your number's consecutive number: ")
print(sum)
time.sleep(3)
print("Thank you kindly for using my code :D")


articles_dict = [
    {
        "title": "Endless ocean waters.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Oceans of other planets are full of silver",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "An ocean that cannot be crossed.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "The ocean that you love.",
        "author": "Golden Gun",
        "year": 2021,
    },
]

def find_articles(key, letter_case=False):
    founded_articles = []
    for article in articles_dict:
        title = article['title']
        author = article['author']
        year = article['year']

        if not letter_case:
            key = key.lower()
            title_lower = title.lower()
            author_lower = author.lower()
        else:
            title_lower = title
            author_lower = author

        if key in title_lower or key in author_lower:
            founded_articles.append({
                'author': author,
                'title': title,
                'year': year
            })

    if not founded_articles:
        print("Not found")

    return founded_articles



import re


def find_word(text, word):
    search_result = re.search(rf'\b{re.escape(word)}\b', text, re.IGNORECASE)

    if search_result:
        result_dict = {
            'result': True,
            'first_index': search_result.start(),
            'last_index': search_result.end() - 1,
            'search_string': search_result.group(),
            'string': text
        }
    else:
        result_dict = {
            'result': False,
            'first_index': None,
            'last_index': None,
            'search_string': word,
            'string': text
        }

    return result_dict



import re


def replace_spam_words(text, spam_words):
    for word in spam_words:
        word_pattern = re.compile(rf'\b{re.escape(word)}\b', re.IGNORECASE)
        text = word_pattern.sub('*' * len(word), text)
    return text




import re

def find_all_emails(text):
    all_emails = re.compile(r"[a-zA-Z][a-zA-Z0-9_.]+@[a-z]+\.[a-z]{2,}")
    result = all_emails.findall(text)
    return result




import re


def find_all_phones(text):
    result = re.findall(r"\+380\([0-9]{2}\)[0-9]{3}\-[0-9]{1}\-[0-9]{3}|\+380\([0-9]{2}\)[0-9]{3}\-[0-9]{2}\-[0-9]{2}", text)
    return result



text = "Irma +380(67)777-7-771 second +380(67)777-77-77 aloha a@test.com abc111@test.com.net +380(67)111-777-777+380(67)777-77-787"
phones = find_all_phones(text)
print(phones)





import re


def find_all_links(text):
    result = []
    pattern = r'https?://(?:[a-zA-Z0-9_-]+\.)*[a-zA-Z0-9_-]+(?<!\.)\.[a-zA-Z]{2,}'
    iterator = re.finditer(pattern, text)
    for match in iterator:
        result.append(match.group())
    return result




def write_employees_to_file(employee_list, path):
    with open(path, "w") as file:
        for department in employee_list:
            for employee in department:
                file.write(employee + "\n")
    file.close()


employee_list = [['Robert Stivenson,28',
                  'Alex Denver,30'], ['Drake Mikelsson,19']]
write_employees_to_file(employee_list, "employee_data.txt")




def add_employee_to_file(record, path):
    file = open(path, 'a')  # Otwieranie pliku w trybie dodawania (append)
    file.write(record + '\n')  # Dodawanie nowego pracownika i nowej linii
    file.close()

# Przykład użycia:
add_employee_to_file("Drake Mikelsson,19", "employee_data.txt")




def get_cats_info(path):
    cats_info = []

    with open(path, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            cat_info = {
                "id": parts[0],
                "name": parts[1],
                "age": parts[2]
            }
            cats_info.append(cat_info)

    return cats_info

# Przykład użycia:
path = "cats_data.txt"
cats_data = get_cats_info(path)
print(cats_data)





def get_recipe(path, search_id):
    with open(path, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            if parts[0] == search_id:
                recipe = {
                    "id": parts[0],
                    "name": parts[1],
                    "ingredients": parts[2:]
                }
                return recipe
    
    return None

# Przykład użycia:
path = "recipes.txt"
search_id = "60b90c3b13067a15887e1ae4"
recipe = get_recipe(path, search_id)
if recipe:
    print(recipe)
else:
    print("Przepis o podanym ID nie został znaleziony.")






def sanitize_file(source, output):
    with open(source, 'r') as source_file:
        content = source_file.read()
        sanitized_content = ''.join([char for char in content if not char.isdigit()])
    
    with open(output, 'w') as output_file:
        output_file.write(sanitized_content)

# Przykład użycia:
source_file_path = "source.txt"
output_file_path = "output.txt"
sanitize_file(source_file_path, output_file_path)
print("Plik został oczyszczony i zapisany do", output_file_path)





def save_applicant_data(source, output):
    with open(output, 'w') as output_file:
        for applicant in source:
            name = applicant["name"]
            specialty = applicant["specialty"]
            math_score = applicant["math"]
            lang_score = applicant["lang"]
            eng_score = applicant["eng"]
            output_line = f"{name},{specialty},{math_score},{lang_score},{eng_score}\n"
            output_file.write(output_line)

# Przykład użycia:
applicant_data = [
    {
        "name": "Kovalchuk Oleksiy",
        "specialty": 301,
        "math": 175,
        "lang": 180,
        "eng": 155,
    },
    {
        "name": "Ivanchuk Boryslav",
        "specialty": 101,
        "math": 135,
        "lang": 150,
        "eng": 165,
    },
    {
        "name": "Karpenko Dmitro",
        "specialty": 201,
        "math": 155,
        "lang": 175,
        "eng": 185,
    },
]
output_file_path = "output.txt"
save_applicant_data(applicant_data, output_file_path)
print("Dane kandydatów zostały zapisane do pliku", output_file_path)





def is_equal_string(utf8_string, utf16_string):
    decoded_utf8 = utf8_string.encode('utf-8').decode('utf-8')
    decoded_utf16 = utf16_string.encode('utf-16').decode('utf-16')
    
    return decoded_utf8 == decoded_utf16

# Przykład użycia:
utf8_string = "Hello, world!"
utf16_string = "Hello, world!".encode('utf-16').decode('utf-16')
result = is_equal_string(utf8_string, utf16_string)
print(result)  # Oczekiwane wyjście: True





def is_equal_string(utf8_string, utf16_string):
    utf8_normalized = utf8_string.decode('utf-8').casefold().encode('utf-8')
    utf16_normalized = utf16_string.decode('utf-16').casefold().encode('utf-8')
    return utf8_normalized == utf16_normalized





def save_credentials_users(path, users_info):
    with open(path, 'wb') as file:
        for username, password in users_info.items():
            user_data = f"{username}:{password}\n"
            file.write(user_data.encode())

# Przykład użycia:
users_info = {'andry': 'uyro18890D', 'steve': 'oppjM13LL9e'}
save_credentials_users('users.txt', users_info)





def get_credentials_users(path):
    credentials = []
    with open(path, 'rb') as file:
        lines = file.readlines()
        for line in lines:
            credentials.append(line.decode().strip())
    return credentials

# Przykład użycia:
credentials = get_credentials_users('users.txt')
print(credentials)





import base64

def encode_data_to_base64(data):
    encoded_data = []
    for item in data:
        username, password = item.split(':')
        encoded_item = base64.b64encode(f'{username}:{password}'.encode()).decode()
        encoded_data.append(encoded_item)
    return encoded_data

# Przykład użycia:
credentials = ['andry:uyro18890D', 'steve:oppjM13LL9e']
encoded_credentials = encode_data_to_base64(credentials)
print(encoded_credentials)





import shutil



def create_backup(path, file_name, employee_residence):
    file_path = f"{path}/{file_name}"
    
    with open(file_path, 'wb') as file:
        for employee, residence in employee_residence.items():
            line = f"{employee} {residence}\n"
            file.write(line.encode())
    
    backup_folder = f"{path}/backup_folder"
    shutil.make_archive('backup_folder', 'zip', path)

    return f"{backup_folder}.zip"

# Przykład użycia:
employee_residence = {'Michael': 'Canada', 'John': 'USA', 'Liza': 'Australia'}
backup_path = "/path/to/backup"
backup_file = "employee_residence.txt"
backup_archive = create_backup(backup_path, backup_file, employee_residence)
print("Backup archive:", backup_archive)





import shutil

def unpack(archive_path, path_to_unpack):
    shutil.unpack_archive(archive_path, path_to_unpack)

# Przykład użycia:
archive_path = "/path/to/backup/backup_folder.zip"
path_to_unpack = "/path/to/extracted_data"
unpack(archive_path, path_to_unpack)
print("Archive unpacked successfully.")





from setuptools import setup


def do_setup(args_dict):
    setup(**args_dict)






from setuptools import setup


def do_setup(args_dict, requires, entry_points):
    setup(name=args_dict['name'],
          version=args_dict['version'],
          description=args_dict['description'],
          url=args_dict['url'],
          author=args_dict['author'],
          author_email=args_dict['author_email'],
          license=args_dict['license'],
          packages=args_dict['packages'],
          install_requires=requires,
          entry_points={'console_scripts': ['helloworld = useful.some_code:hello_world']}
          )






def is_integer(s):
    s = s.strip()
    if len(s) == 0:
        return False
    if s[0] in ['+', '-']:
        s = s[1:]
    if s.isdigit():
        return True
    else:
        return False






import re


def capital_text(text):
    text = text.capitalize()
    text = re.sub(r'([.!?]\s*)([a-z])',lambda m: m.group(1) + m.group(2).upper(), text)

    return text





def solve_riddle(riddle, word_length, start_letter, reverse=False):
    if reverse:
        riddle = riddle[::-1]
    
    for i in range(len(riddle) - word_length + 1):
        if riddle[i] == start_letter:
            candidate = riddle[i:i+word_length]
            if candidate.isalpha() and candidate.islower():
                return candidate
    
    return ""





def data_preparation(data):
    result = []

    for sublist in data:
        if len(sublist) > 2:
            sublist.remove(min(sublist))
            sublist.remove(max(sublist))
            result.extend(sublist)
        else:
            sublist.extend(sublist)

    result.sort(reverse=True)
    return result






def token_parser(s):    
    import re
    tokens = re.findall(r'(\d+|[+\-*/()])', s)
    return tokens






def all_sub_lists(lst):
    n = len(lst)
    sublists = [[]]

    for i in range(n):
        for j in range(i + 1, n + 1):
            sublist = lst[i:j]
            sublists.append(sublist)
    
    return sorted(sublists, key=len)





def make_request(keys, values):
    if len(keys) != len(values):
        return {}
    request_dict = {}
    request_dict = {keys[i]: values[i] for i in range(len(keys))}

    return request_dict





def sequence_buttons(string):
    char_buttons = {
        '.': '1', ',': '11', '?': '111','!': '1111',':': '1111',
        'A': '2', 'B': '22', 'C': '222',
        'D': '3', 'E': '33', 'F': '333',
        'G': '4', 'H': '44', 'I': '444',
        'J': '5', 'K': '55', 'L': '555',
        'M': '6', 'N': '66', 'O': '666',
        'P': '7', 'Q': '77', 'R': '777', 'S': '7777',
        'T': '8', 'U': '88', 'V': '888',
        'W': '9', 'X': '99', 'Y': '999', 'Z': '9999',
        ' ': '0'
    }
    
    string = string.upper()
    flush = []
    
    for char in string:
        if char in char_buttons:
            flush.append(char_buttons[char])
    
    return ''.join(flush) 





def file_operations(path, additional_info, start_pos, count_chars):
    with open(path, 'a') as file:
        file.write(additional_info)
    with open(path, 'r') as file:
        file.seek(start_pos)  
        read_data = file.read(count_chars) 
        
    return read_data





import re


def get_employees_by_profession (path, profession): 
    with open(path, 'r') as file:
        verses = file.readlines()
        matchings = []
        for verse in verses:
            if verse.find(profession) > 0:
                vers = verse.replace(profession, "") 
                matchings.append(re.sub (r'\s+', '', vers))
        return ' '.join(matchings)
        






def flatten(data):
    if not data: 
        return []
    first = data[0]
    rest = data[1:]
    if isinstance(first, list):  
        return flatten(first) + flatten(rest)
    else:  
        return [first] + flatten(rest)






def decode(data):    
    if len(data)==2:
        return [data[0]]*data[1]
    elif len(data)<2:
        return data
    return decode(data[:2])+decode(data[2:])






def encode(data):  
    if not data:
        return []
    first = data[0]
    rest = data[1:]
    char_counter = []
    count = 1
        
    while rest and rest[0] == first:
        count += 1
        rest = rest[1:]

    if count > 1:
        return [first, count] + encode(rest)
    else:
        return [first, 1] + encode(rest)






from datetime import datetime


def get_str_date(date):

    date_to_go = datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%fZ')
    date_to_display = date_to_go.strftime('%A %d %B %Y')
    
    return date_to_display






from datetime import date


def get_days_in_month(month, year):
    if month < 1:
        raise ValueError("Numer miesiąca musi być w zakresie od 1 do 12.")
    if month > 12:
        raise ValueError("Numer miesiąca musi być w zakresie od 1 do 12.")
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return 29
        else:
            return 28







from datetime import datetime


def get_days_from_today(date):
    now = datetime.now().date()
    parts = date.split('-')
    the_date = datetime(int(parts[0]), int(parts[1]), int(parts[2])).date()
    return (now - the_date).days






from random import randrange


def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or quantity <= min or quantity >= max:
        return []
    numbers_ticket = set()
    numbers = 0
    while len(numbers_ticket) < quantity:
        random_num = randrange(min, max + 1)
        numbers_ticket.add(random_num)
    sorted_numbers_on_ticket = sorted(numbers_ticket)
    return sorted_numbers_on_ticket






import random


def get_random_winners(quantity, participants):
    participant_keys = list(participants.keys())
    if quantity > len(participant_keys):
        return []
    random.shuffle(participant_keys)
    random_winners = random.sample(participant_keys, quantity)
        
    return random_winners






from decimal import Decimal, getcontext


def decimal_average(number_list, signs_count):
    getcontext().prec = signs_count 
    decimal_numbers = [Decimal(str(num)) for num in number_list]
    lol = sum(decimal_numbers)
    counter = Decimal(len(decimal_numbers))
    average = lol / counter
    return average





DEFAULT_DISCOUNT = 0.05


def get_discount_price_customer(price, customer):
    if "discount" in customer:
        discount = customer["discount"]
    else:
        discount = DEFAULT_DISCOUNT

    discounted_price = price * (1 - discount)
    return discounted_price
    
    
    
def discount_price(discount):
    def calculate_discounted_price(price):
        return price * (1 - discount)

    return calculate_discounted_price
    
    
    
    
def format_phone_number(func):
    def wrapper(phone):
        if len(phone) <= 12:
            phone = "+38" + phone
        
        return func(phone)
    
    return wrapper
    
@format_phone_number
def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
            .removeprefix("+")
            .replace("(", "")
            .replace(")", "")
            .replace("-", "")
            .replace(" ", "")
    )
    if new_phone.startswith("38"):
        new_phone = "+" +  new_phone
    elif new_phone.startswith("+38"):
        pass
    else:
        new_phone = "+38" +  new_phone
    return new_phone
    
    
    
    
import re

def generator_numbers(string=""):
    pattern = r"-?\d+"

    matches = re.findall(pattern, string)

    for match in matches:
        yield int(match)

def sum_profit(string):
    total_profit = 0

    for number in generator_numbers(string):
        total_profit += number
    
    return total_profit
    
    
    
    
def get_emails(list_contacts):
    email_list = list(map(lambda contact: contact["email"], list_contacts))
    return email_list
    
    
    
    
    
def positive_values(list_payment):
    positive_payments = list(filter(lambda x: x > 0, list_payment))
    return positive_payments
    
    
    
    
def get_favorites(contacts):
    favorite_contacts = list(filter(lambda contact: contact["favorite"], contacts))
    return favorite_contacts
    
    
    
    
    
from functools import reduce


def sum_numbers(numbers):
    total_sum = reduce(lambda x, y: x + y, numbers)
    return total_sum



from functools import reduce


def amount_payment(payment):
    total_payment = reduce(lambda x, y: x + y if y > 0 else x, payment, 0)
    return total_payment


from collections import UserList


class AmountPaymentList(UserList):

    def amount_payment(self):
        return sum(filter(lambda x: x > 0, self.data))


################################
class Animal:
    color = "white"

    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight

    def change_color(self, new_color):
        Animal.color = new_color


class Owner:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def info(self):
        return {
            "name": self.name,
            "age": self.age,
            "address": self.address
        }


class Cat(Animal):

    def say(self):
        return "Meow"


class Dog(Animal):
    def __init__(self, nickname, weight, breed, owner):
        self.breed = breed
        self.owner = owner
        super().__init__(nickname, weight)

    def say(self):
        return "Woof"

    def who_is_owner(self):
        return self.owner.info()


class CatDog(Cat, Dog):
    def say(self):
        return "Meow"

    def info(self):
        return f"{self.nickname}-{self.weight}"


class DogCat(Dog, Cat):
    def say(self):
        return "Woof"

    def info(self):
        return f"{self.nickname}-{self.weight}"


dog = Dog("Barbos", 23, "labrador")
cat = Cat("Simon", 10)
first_animal = Animal("Alex", 10)
second_animal = Animal("Svenya", 10)
first_animal.change_color("red")

###############################

from collections import UserString
from collections import UserDict


class LookUpKeyDict(UserDict):
    def lookup_key(data, value):
        keys = []
        for key in data:
            if data[key] == value:
                keys.append(key)
        return keys


class NumberString(UserString):
    def number_count(self):
        count = 0
        for char in self.data:
            if char.isdigit():
                count += 1
        return count


class IDException(Exception):
    pass


def add_id(id_list, employee_id):
    if employee_id.startswith("01"):
        id_list.append(employee_id)
        return id_list
    else:
        raise IDException

######################################

class Contacts:
    current_id = 1

    def __init__(self):
        self.contacts = []

    def list_contacts(self):
        return self.contacts

    def add_contacts(self, name, phone, email, favorite):
        self.contacts.append(
            {
                "id": Contacts.current_id,
                "name": name,
                "phone": phone,
                "email": email,
                "favorite": favorite,
            }
        )
        Contacts.current_id += 1

    def get_contact_by_id(self, id):
        result = list(
            filter(lambda contact: contact.get("id") == id, self.contacts))
        return result[0] if len(result) > 0 else None

    def remove_contacts(self, id):
        for contact in self.contacts:
            if contact["id"] == id:
                self.contacts.remove(contact)
            else:
                pass
"""
