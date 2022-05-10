class Ticket:
    def __init__(self,filmname,filmticketprice,numberoftickets,language='Geo'):
        self.filmname=filmname
        self.filmticketprice=filmticketprice
        self.numberoftickets=numberoftickets
        self.language=language

    def __str__(self):
        return  f'ფილმის დასახელება - {self.filmname}, ფილმის ბილეთის ფასი - {self.filmticketprice}, ბილეთების რაოდენობა - {self.numberoftickets}, ენა - {self.language}'

    def __ge__(self, other):
        n1=self.filmticketprice
        n2=other.filmticketprice
        if n1>=n2:
            return 'პირველი ფილმის ბილეთების რაოდენობა მეტია ან ტოლი მეორეზე'
        else:
            return 'პირველი ფილმის ბილეთების რაოდენობა ნაკლებია ან ტოლი მეორეზე'



class User(Ticket):

    def __init__(self,buyer,money,filmname,filmticketprice,numberoftickets,language='Geo'):
        Ticket.__init__(self,filmname,filmticketprice,numberoftickets,language)
        self.buyer= buyer
        self.money = money

    def __str__(self):
        return f'მყიდველი - {self.buyer}, ანგარიშზე არსებული თანხა - {self.money}GEL'

    def buyticket(self,other):
        if isinstance(other,Ticket):
            if self.filmticketprice < self.money and self.numberoftickets > 0:
                a = self.money - self.filmticketprice*self.numberoftickets
                print(f'თქვენ წარმატებით შეიძინეთ {self.filmname}-ის  {self.numberoftickets} ბილეთი, რომლის ფასიც არის {self.filmticketprice} ლარი ! თქვენი ანგარიში ახლა შეადგენს {a} ლარს')
            elif self.numberoftickets==0:
                print(f'სამწუხაროდ ამჟამად ბილეთების რაოდენობა {self.numberoftickets}-ის ტოლია')
            elif self.filmticketprice > self.money:
                print(f'თქვენ არგაქვთ ანგარიშზე საკმარისი თანხა ({self.money}GEL), რომ შეიძინოთ ბილეთი, რომლის ღირებულებაა - {self.filmticketprice}GEL')


    def deposit(self):
        i=input('გსურთ ანგარიშზე თანხის შეტანა? (დაწერეთ მხოლოდ yes ან no)')

        if i == 'yes':
                other = float(input("შეიტანეთ თანხა: "))
                self.money += other
                print('შეტანილი თანხა:',other)
                print(f'ჯამური თანხა:',self.money-self.numberoftickets*self.filmticketprice)
        elif i == 'no':
            print()
        else:
            print("ინფორმაცია არასწორად იქნა შეყვანილი, სცადეთ ახლიდან")


c2=Ticket('batman',150,4)
print(c2)
c1=Ticket('spiderman',200,3)
print(c1)
u2=User('john',1200,'spiderman',200,3)
print(u2)
u2.buyticket(c1)
u2.deposit()
print(c2>=c1)









