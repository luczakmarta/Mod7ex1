#Podział na klasy
class Person:
    def __init__(self, name, surname, email,telephone):
        self.name = name
        self.surname = surname
        self.email = email
        self.telephone= telephone

    def __str__(self):
        return f'{self.name} {self.surname}  {self.email} {self.telephone} '


Person1 = Person(name="Marta", surname="Luczak,",  email="m@wp.pl,",telephone= "+48 502224543")
Person2 = Person(name="Patryk", surname="Ziezio,",  email="d@wp.pl,",telephone=1)
Person3 = Person(name="Maciej", surname="Nowak,",  email="c@wp.pl,",telephone=1)
Person4 = Person(name="Edyta", surname="Las,", email="w@wp.pl,",telephone=1)
Person5 = Person(name="Maja", surname="Lisiecka,", email="e@wp.pl,",telephone=1)

items = [Person1, Person2, Person3, Person4, Person5]

for person in items:
    print(person)
print("________")

class Business(Person):
    def __init__ (self, company,position ,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.company = company
        self.position = position

    def __str__(self):
        return f'{self.name} {self.surname}  {self.email2} {self.telephone2} {self.company} {self.position} '

business1=Business(name="Marta", surname="Luczak",  email2="m@wp.pl",telephone2=1,company="Citi",position="Analyst")
business2=Business(name="Patryk", surname="Ziezio",  email2="d@wp.pl",telephone2=1,company="HM",position="Analyst")
business3=Business(name="Maciej", surname="Nowak",  email2="c@wp.pl",telephone2=1,company="Zara",position="Analyst")
business4=Business(name="Edyta", surname="Las",  email2="w@wp.pl",telephone2=1,company="Sklep",position="Analyst")
business5=Business(name="Maja", surname="Lisiecka",  email2="e@wp.pl",telephone2=1,company="CCC",position="Analyst")

items2 = [business1,business2,business3,business4,business5]

for business in items2:
    print(business)

#metoda contact()

def contact(self)
    print(self.telephone)

#label_lenght
def label_length(self):
    return(len(self.imie + " " + self.nazwisko))

#Create Contacts

#podział na prywatne + biznesowe
def generowanie_wizytowek(rodzaj=BaseContact, ilosc=1):
    wizytowki = []
    if rodzaj == Person:
        for i in range(0, ilosc):
            kontakt  = Person(name=fake.name(), surname=fake.surname(), telephone =fake.telephone(),  email=fake.email())
            wizytowki.append(kontakt)
    if rodzaj == BusinessContact:
        for i in range(0, ilosc):
            kontakt  = Business(name=fake.name(), surname=fake.surname(), telephone=fake.telephone(),
            email2=fake.email(), position = fake.job(), company=fake.company(), telephone2=fake.phone_number())
            wizytowki.append(kontakt)
    return wizytowki

wizytowki = generowanie_wizytowek(BusinessContact, 10)
for i in wizytowki:
    print(i)