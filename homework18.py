class Car:
    def __init__(self, year, manufacturer, model, fuel_consumption):
        self.year = year
        self.manufacturer = manufacturer
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.mileage = 0

    def drive(self):
        print(f"Я авто марки {self.model}, їду по справам господаря")

    @property
    def cost_of_service(self):
        return self.mileage * 7.6

car1 = Car(2020, "Toyota", "Corolla", 6.5)
car2 = Car(2019, "Honda", "Civic", 7.2)
car3 = Car(2021, "Ford", "Focus", 6.8)

car1.mileage = 15000

print(f"Вартість обслуговування для {car1.model}: {car1.cost_of_service}")

car2.drive()
