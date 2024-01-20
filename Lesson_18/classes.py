class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def moves(self):
        print("Moves along...")

    def get_make_model(self):
        print(f"I'm a {self.make} {self.model}")

my_car = Vehicle("Tesla", "Model 3")

# print(my_car.make)
# print(my_car.model)
my_car.get_make_model()
my_car.moves()


your_car = Vehicle("Cadillac", "Escalade")
your_car.get_make_model()
your_car.moves()

class Airplane(Vehicle):
    def __init__(self, make, model, faa_id):
        super().__init__(make, model) #inherit from parent
        self.faa_id = faa_id
    def moves(self):
        print("Flies along...")

class Truck(Vehicle):
    def moves(self):
        print("Rumbles along...")

class GolfCart(Vehicle):
        pass

cessna = Airplane("Cessna", "172", "N-735634")
mack = Truck("Mack", "Pinnacle")
golfwagon = GolfCart("Yamaha", "G724")

cessna.get_make_model()
cessna.moves()
mack.get_make_model()
mack.moves()
golfwagon.get_make_model()
golfwagon.moves()

print("\n\n")

for v in (my_car, your_car, cessna, mack, golfwagon):
    v.get_make_model()
    v.moves()