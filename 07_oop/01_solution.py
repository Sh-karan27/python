class Car:
    total_car=0
    def __init__(self,brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1

    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def get_brand(self):
        return self.__brand
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_description():
        return "Cars are means for transport"
    
    @property
    def model(self):
        return self.__model
    


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    
    def fuel_type(self):
        return "Electric charge"


# my_car= Car("Toyota", "Supa")
# my_car.model = "City"

# Car("Tata","Nexom")
# print(my_car.general_description())

# print(my_car.model)




# my_tesla = ElectricCar("Tesla", "Model S", "85kwh" )


# print(
# isinstance(my_tesla,Car))
# print(isinstance(my_tesla,ElectricCar))



# print(my_tesla.fuel_type())
# print(my_car.fuel_type())



# print(my_tesla.full_name())
# print(my_tesla.get_brand())


# print(my_car.brand )
# print(my_car.model )
# print(my_car.full_name())


class Battery:
    def battery_info(self):
        return "thiis is battery"

class Engine:
    def engine_infor(self):
        return "this is engiine"



class ElectricCarTwo(Battery,Engine,Car):
    pass


my_new_tesla = ElectricCarTwo("Tesla", "Model5")

print(my_new_tesla.engine_infor())
print(my_new_tesla.battery_info())