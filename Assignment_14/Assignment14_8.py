class Vehicle:
    def start(self):
        print("in parent vehicle")

class Car(Vehicle):
    def start(self):
        print("in child car")

    def stop(self):
        print("in child stop")

vobj = Car()
vobj.start()
