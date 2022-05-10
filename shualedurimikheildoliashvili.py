class Health:
    def __init__(self,age,sex,normal_impulse):
        self.age = age
        self.sex = sex
        self.normal_pulse= normal_impulse

    def __str__(self):
        return  f"ასაკი - {self.age}, სქესი - {self.sex}, ნორმალური გულისცემა - {self.normal_pulse}"

    def heartbeat(self):
        print("საშუალო ხანგრძლივობაა - ", 2600000000 / 365*self.age) # ანუ ეს ესე იმიტომ დავწერე რომ პირობაში რაღაც არასწორედაა იმიტომ რომ საშუალო სიცოცხლის ხანგრძლივობა როგორ უნდა გავიგო თუ ისედაც ვაწვდით ასაკს, დაახლოებით როგორც მივხვდი ისე დავწერე ;დ

    def pulse_count(self):
        if self.sex== 'Female':
            print(f"ქალების მაქსიმალური გულისცემა არის", (226-0.9*self.age))
        elif self.sex == "Male":
            print(f"კაცების მაქსიმალური გულისცემა არის", (226-0.9*self.age))

    def heartbeatonwork(self,factor):
        self.factor = factor



        if self.sex == "Female" and factor ==0.8:
            print("რთული დონის ვარჯიშებისას გულისცემაა -",226-0.9*self.age - factor + self.normal_pulse)
        elif self.sex == "Female" and factor == 0.6:
            print("საშუალო დონის ვარჯიშებისას გულისცემაა -", 226 - 0.9 * self.age - factor + self.normal_pulse)
        elif self.sex == "Female" and factor == 0.5:
            print("იოლი დონის ვარჯიშებისას გულისცემაა -", 226 - 0.9 * self.age - factor + self.normal_pulse)
        elif self.sex == "Male" and factor == 0.8:
            print("რთული დონის ვარჯიშებისას გულისცემაა -",226-0.9*self.age - factor + self.normal_pulse)
        elif self.sex == "Male" and factor == 0.6:
            print("საშუალო დონის ვარჯიშებისას გულისცემაა -", 226 - 0.9 * self.age - factor + self.normal_pulse)
        elif self.sex == "Male" and factor == 0.5:
            print("იოლი დონის ვარჯიშებისას გულისცემაა -", 226 - 0.9 * self.age - factor + self.normal_pulse)


person1= Health(20, "Male", 62)
print(person1)
person1.pulse_count()
person1.heartbeatonwork(0.6)
person2= Health(50, "Female", 55)
print(person2)
person2.pulse_count()
person2.heartbeatonwork(0.8)
person3=Health(41,"Female", 53)
person3.heartbeat()
