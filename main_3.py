"""
• კლასის აღწერა: შექმენით კლასი Cat შემდეგი სამი მეთოდით: eat(), talk(), walk()
რომლებიც ბეჭდავს შესაბამის ტექსტს ეკრანზე. მაგ. eat() მეთოდი ბეჭდავს "Cat
eats a milk”, talk() მეთოდი ბეჭდავს "Cat says miaww”

, walk() მეთოდი ბეჭდავს "Cat

can run 20km/h”.
• კლასის აღწერა: დაამატეთ მეორე კლასი Dog, რომელსაც აქვს იგივე
სახელწოდების მეთოდები eat(), talk(), walk(), თუმცა განსხვავებული
მოქმედებებით. მაგ. eat() მეთოდი ბეჭდავს " Dog eats a bone”, talk() მეთოდი
ბეჭდავს "Dog says Aww”, walk() მეთოდი ბეჭდავს " Dog can run 40km/h”.
• ობიექტის შექმნა: კლასის გარეთ შემოიტანეთ Cat() კლასის ობიექტი, ასევე
შემოიტანეთ Dog() კლასის ობიექტი. გამოიძახეთ ორივე კლასის მეთოდები.
• გამოიძახეთ სამივე ფუნქცია ორივე ობიექტისთვის (უმჯობესია გამოიყენოთ for
ციკლი რომელიც გაირბენს ორივე ობიექტისთვის შედგენილ tuple-ს).

"""

class Cat:
    def eat(self):
        print("Cat eats a milk")

    def talk(self):
        print("Cat says miaww")

    def walk(self):
        print("Cat can run 20km/h.")

class Dog:
    def eat(self):
        print("Dog eats a bone")
    def talk(self):
        print("Dog says Aww")
    def walk(self):
        print("Dog can run 40km/h.")


cat = Cat()
dog = Dog()
tuple_1 = (cat,dog)
# print(type(tuple_1))
# cat.walk()
# dog.walk()
# cat.talk()
# dog.talk()
# cat.eat()
# dog.eat()
# for i in tuple_1:
#     i.walk()
#



class Currency:

    def __init__(self, value, unit = "GEL"):
        self.value = value
        self.unit = unit

    def __str__(self):
        return "{:.2f} {}".format(self.value,self.unit)


    def changeTo(self, valuta):
        dictt = {"1 USD": 2.7 , "1 EUR": 3}

        usd_eur = dictt["1 EUR"] - dictt["1 USD"]

        if self.unit == "GEL" and valuta == "USD":
            changed_obj = self.value / dictt["1 USD"]
            return "{:.2f} {}".format(changed_obj, valuta)

        elif self.unit == "USD" and valuta == "GEL":
            changed_obj = self.value * dictt["1 USD"]
            return "{:.2f} {}".format(changed_obj, valuta)


        elif self.unit == "GEL" and valuta == "EUR":
            changed_obj = self.value / dictt["1 EUR"]
            return "{:.2f} {}".format(changed_obj, valuta)


        elif self.unit == "EUR" and valuta == "GEL":
            changed_obj = self.value * dictt["1 EUR"]
            return "{:.2f} {}".format(changed_obj, valuta)


        elif self.unit == "USD" and valuta == "EUR":
            changed_obj = self.value / usd_eur
            return "{:.2f} {}".format(changed_obj, valuta)


        elif self.unit == "EUR" and valuta == "USD":
            changed_obj = self.value * usd_eur
            return "{:.2f} {}".format(changed_obj, valuta)

        elif self.unit == "GEL":
            changed_obj = self.value
            return "{:.2f} {}".format(changed_obj, valuta)


        elif self.unit == "USD":
            changed_obj = self.value
            return "{:.2f} {}".format(changed_obj, valuta)

        elif self.unit == "EUR":
            changed_obj = self.value
            return "{:.2f} {}".format(changed_obj, valuta)

        else:
            print(f"კონვერტაცია {self.unit}-დან {self.unit}-ზე შეუძლებელია")


    def __add__(self, other):
        if isinstance(self, Currency) and isinstance(other, Currency):
            result =  self.value + other.value
            return Currency(result, self.unit)

        elif isinstance(self, Currency) and isinstance(other,int) or isinstance(other,float):
            result = self.value + other
            return Currency(result, self.unit)

    def __radd__(self, other):

        return self.__add__(other)


        # if isinstance(other, int) or isinstance(other,float) and isinstance(self,Currency):
        #     result = other + self.value
        #     return Currency(result,self.unit)

    def __mul__(self, other):
        try:
            if isinstance(other, int) or isinstance(other, float):
                result = Currency(self.value * other, self.unit)
                return result

            else:
                print("გამრავლების ოპერაცია უნდა შესრულდეს მხოლოდ მთელ ან ათწილად რიცხვზე!")

        except TypeError:
            print ("გამრავლების ოპერაცია უნდა შესრულდეს მხოლოდ მთელ ან ათწილად რიცხვზე!!!")


    def __rmul__(self, other):
        return self.__mul__(other)

        # try:
        #     if isinstance(self, Currency):
        #         if isinstance(other, int) or isinstance(other, float):
        #             result = Currency(self.value * other, self.unit)
        #             return result
        #
        #     else:
        #         print("გამრავლების ოპერაცია უნდა შესრულდეს მხოლოდ მთელ ან ათწილად რიცხვზე!")
        #
        # except TypeError:
        #     print ("გამრავლების ოპერაცია უნდა შესრულდეს მხოლოდ მთელ ან ათწილად რიცხვზე!!!")


    def __gt__(self, other):
        selff = self.changeTo("GEL")
        otherr = other.changeTo("GEL")
        print(f"self: {selff}")
        print(f"other: {otherr}")

        if otherr > selff:
            print(f"{self.value} {self.unit} > {other.value} {other.unit} ?")
            return False

        if selff > otherr:
            print(f"{self.value} {self.unit} > {other.value} {other.unit} ??")
            return True

        elif self.unit == other.unit:
            print(f"{self.value} {self.unit} = {other.value} {other.unit}!")
            return False

        else:
            pass

obj1 = Currency(300, "USD")
obj2 = Currency(299, "EUR")
obj3 = Currency(100, "GEL")
# x = ( obj1 * 3)
# print(5 * obj1)
# print(type(x))
# print(obj1 > obj2)
# print(obj2.__gt__(obj1))
# print(obj3.changeTo("USD"))
# print(100 + obj3)
# print(obj3 * 3)


"""
გაითვალისწინეთ owner-ის მნიშვნელობა არის Person კლასის ობიექტი (instance).
✲ Person კლასში დაამატეთ __str__() მეთოდი, რომელიც დააბრუნებს პიროვნების 
სრულ ინფორმაციას.
✲ კლასების გარეთ შემოიტანეთ 2 ობიექტი Person კლასის (მაგ.ერთი მეპატრონე, მეორე მყიდველი).
 ასევე, შემოტანეთ კონკრეტული ბინა
(House ტიპის, რომელსაც ამჟამინდელ მფლობელად (owner) გადასცემთ ერთ-ერთ შემოტანილ პირს).
✲ House კლასში დაამატეთ ბინის გაყიდვის ფუნქცია/მეთოდი, რომლის დროსაც პარამეტრად გადაეცემა მყიდველი. 
თუ მეტი პარამეტრი არ
გადაეცემა, ამ დროს უნდა შესრულდეს ბინის გაყიდვის ოპერაცია (გამყიდველის deposit უნდა 
გაიზარდოს ბინის ღირებულებით, owner
უნდა შეიცვალოს, status გახდეს “გაყიდული” და დაბეჭდოს შესაბამისი შეტყობინება). 

თუ ამ მეთოდის გამოძახებისას მყიდველის გარდა
კიდევ ერთი პარამეტრი (რიცხვი) გადაეცა, მაშინ შესრულდეს ბინის სესხით გაყიდვის ოპერაცია, 
სადაც პარამეტრად გადაცემული რიცხვი
მიუთითებს კლიენტის მიერ აღებული სესხის ოდენობას. ფუნქციამ კი უნდა 
შეასრულოს შემდეგი ოპერაციები: გამყიდველის deposit უნდა
გაიზარდოს ბინის ღირებულებით, owner უნდა შეიცვალოს, status გახდეს “გაყიდულია სესხით”,
 მყიდველის სესხის (loan) ატრიბუტის
მნიშვნელობა უნდა გაიზარდოს შესაბამისად და დაბეჭდოს ბინის გაყიდვის შესაბამისი შეტყობინება.
✲ კლასის გარეთ მოახდინეთ აღწერილი ფუნქციის გამოძახება და დარწმუნდით მის სისწორეში.
"""


class Person:
    def __init__(self, name, deposit = 1000, loan = 0):
        self.name = name
        self.deposit = deposit
        self.loan = loan

    def __str__(self):
        return f"{self.name}"

    # def __str__(self,):
    #     return f"Name: {self.name} Deposit:{self.deposit} Loan:{self.loan} "

    # def __repr__(self, deposit,loan):
    #     return f"Name: {self.name} Deposit:{self.deposit} Loan:{self.loan} "

class House:
    def __init__(self, ID, price, owner,status):
        self.ID = ID
        self.price = price
        self.owner = owner
        self.status = status

    def sell(self, myidveli,param = None, ):
        if param is None and isinstance(self.owner, Person):
            self.owner.deposit += self.price
            print(self.owner.deposit)
            self.status = "გაყიდული"
            print(f"{self.ID} გაყიდულია")
            self.owner = Person(myidveli)
            return self.owner


        elif type(param) is int:
            self.owner.deposit += self.price
            print(f"{self.owner}-ს Deposit: {self.owner.deposit}")
            self.owner = Person(myidveli)
            self.status = "გაყიდულია სესხით"
            print(f"{self.ID} გაყიდულია სესხით!!!")
            myidveli.loan += param
            print(f"{myidveli.name}-ს Loan: {myidveli.loan}")


#
# def selll(house, param = None):
#     if param is None:
#         house.sell(myidveli)
#     elif type(param) is  int:
#         house.sell(myidveli,param)

#
# mepatrone = Person("ANZ")
# myidveli = Person("NAI")
# house1 = House(1,200, mepatrone ,"av")
# print(house1.owner)
# print(house1.sell(myidveli))
# print(mepatrone.deposit)
# print(house1.status)


mepatrone = Person("ANZ")
myidveli = Person("NAI")
house2 = House(1,500, mepatrone ,"av")
print(house2.owner)
print(house2.sell(myidveli, 100))
print(mepatrone.deposit)
print(myidveli.loan)
print(house2.status)


