#from calculator import Calculator, Car, ElectricCar  # первый вариант обращения
import calculator

if __name__ == '__main__':
    calc = calculator.Calculator(years=3)
    calc.add_car(
        calculator.Car("Toyota Corolla", price=120000, fuel_economy=7, service_cost=1200, insurance_cost=2500),  # нажав ctrl+D можно продублировать строчку
    )
    calc.add_car(
        calculator.ElectricCar("Tesla Model 3", 200000, 5500, 150),
    )
    calc.add_car(
        calculator.Car("Range Rover", 650000, 3, service_cost=3000, insurance_cost=7000),
    )
    calc.add_car(
        calculator.Car("Audi", 450000, 3, service_cost=2000, insurance_cost=5000),
    )
    calc.add_car(
        calculator.Car("Skoda Yeti", 250000, 2, service_cost=1000, insurance_cost=2000),
    )
    calc.print_cars()
