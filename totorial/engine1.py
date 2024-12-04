from abc import ABCMeta, abstractmethod

class FuelStorage(metaclass=ABCMeta):
    def __init__(self, capacity: float):
        self._capacity = capacity
        self._level = 0 #by default, this is zero, also protected

    @property
    def capacity(self):
        return self._capacity
    @property
    def level(self):
        return self._level
    @property
    def percentage(self):
        return 100*self.level / self.capacity
    def __change_fuel_level(self, amount: float):
        new_level = self._level + amount

        #logic
        if new_level < 0:
            new_level = 0
            pass
        elif new_level > self.capacity:
            new_level = self.capacity
            pass
        self.level = new_level
        return
    def _increase_fuel(self, amount: float):
        return self.__change_fuel_level(amount)
    def _decrease_fuel(self, amount: float):
        return self.__change_fuel_level(-amount)
    pass
class FuelTank(FuelStorage):
    def __init__(self, capacity):
        super().__init__(capacity)
    def add_fuel(self, amount):
        return self._increase_fuel(amount)
    def use_fuel(self, amount):
        return self._decrease_fuel(amount)
    def drain_tank(self):
        return self.use_fuel(self.level)
    pass

class Battery(FuelStorage):
    def __init__(self, capacity):
        super().__init__(capacity)
        return
    
    def recharge(self, amount:float):
        return self._increase_fuel(amount)
    def decharge(self, amount: float):
        return self._decrease_fuel(amount)
    pass

class Engine(metaclass=ABCMeta):
    def __init__(self, fuel_storage: FuelStorage):
        self.__is_running = False
        self.__speed = 0
        self._fuel_storage = fuel_storage
        return
    @property
    def is_running(self):
        return self.__is_running
    @property
    def speed(self):
        return self.__speed
    @abstractmethod
    def start(self):
        self.__is_running = True
        return
    @abstractmethod
    def stop(self):
        self.__is_running = False
        return
    def accelerate(self, amount: float):
        return self.__change_speed(amount)
    def decelerate(self,amount: float):
        return self.__change_speed(-amount)
    def reverse(self, amount):
        return self.__change_speed(-2*amount)
    def __change_speed(self, amount: float):
        return self.__speed + amount
    pass

class CombustionEngine(Engine):
    def __init__(self, fuel_storage: FuelTank):
        return
    def start(self):
        return super().start()
    def stop(self):
        return super().stop()
    pass

class ElectricEngine(Engine):
    def __init__(self, fuel_storage: Battery):
        super().__init__(fuel_storage)
        return
    def start(self):
        return super().start()
    def stop(self):
        return super().stop()
    pass

class HybridEngine(Engine):
    def __init__(self, combustion_engine: CombustionEngine, electric_engine: ElectricEngine):
        self.combustion_engine = combustion_engine
        self.electric_engine = electric_engine
        return
    def start(self):
        return super.start()
    def stop(self):
        return super().stop()
    def refuel(self, fuel: float):
        return
    def recharge(self, charge: float):
        return
    pass

hybrid_engine = HybridEngine(CombustionEngine(FuelTank(500))), ElectricEngine(Battery(120000))

print(hybrid_engine)
print(hybrid_engine.combustion_engine)
print(hybrid_engine.electric_engine)
print(hybrid_engine.combustion_engine.fuel_storage)
print(hybrid_engine.electric_engine.fuel_storage)
    

        

    

    
    


