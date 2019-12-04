class Airplane:
    def __init__(self, make, model, year, max_speed):
        self.make = make
        self.model = model
        self.year = year
        self.max_speed = max_speed
        self.odometr = 0
        self.is_flying = False
        
    def take_off(self):
        self.is_flying = True
        sms_t = 'Vzletel v 18:00'
        return sms_t

    def fly(self, km):
        self.odometr += km
        sms_f = 'Uchak-09 letit na vysote 3000m'
        return sms_f

    def land(self):
        self.is_flying = False
        sms_l = 'Uchak-09 prizemlilsya v 23:50'
        return sms_l
         
    def result(self):
        print(f"Aircraft brand {self.make}, model {self.model} {self.year} year")

fly1 = Airplane('Kyrgyzstan', 'Uchak-09', '2020', 800)
fly1.result()
print(fly1.take_off())
print(fly1.fly(900))
print(fly1.fly(900))
print(fly1.land())
print(fly1.odometr)
print(fly1.year)
