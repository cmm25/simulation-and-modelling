import vehicles

def main():
    # Create a list to store multiple Car objects
    cars = [
        vehicles.Car('BMW', 2001, 70000, 15000.0, 4),
        vehicles.Car('Toyota', 2005, 60000, 10000.0, 4),
        vehicles.Car('Ford', 2008, 80000, 12000.0, 4),
        vehicles.Car('Chevrolet', 2010, 55000, 13000.0, 4),
        vehicles.Car('Honda', 2015, 40000, 17000.0, 4),
        vehicles.Car('Nissan', 2018, 30000, 19000.0, 4),
        vehicles.Car('Hyundai', 2019, 20000, 20000.0, 4),
        vehicles.Car('Volkswagen', 2016, 35000, 18000.0, 4),
        vehicles.Car('Mercedes-Benz', 2014, 45000, 25000.0, 4),
        vehicles.Car('Audi', 2017, 28000, 22000.0, 4),
        vehicles.Car('Subaru', 2012, 50000, 15000.0, 4),
        vehicles.Car('Kia', 2013, 48000, 14000.0, 4),
        vehicles.Car('Lexus', 2011, 60000, 27000.0, 4),
        vehicles.Car('Mazda', 2009, 65000, 11000.0, 4),
        vehicles.Car('Buick', 2007, 75000, 10000.0, 4),
        vehicles.Car('Chrysler', 2006, 85000, 8000.0, 4),
        vehicles.Car('Dodge', 2004, 90000, 7000.0, 4),
        vehicles.Car('Jeep', 2003, 95000, 6000.0, 4),
        vehicles.Car('Lincoln', 2000, 100000, 5000.0, 4),
        vehicles.Car('Cadillac', 1998, 105000, 4000.0, 4)
    ]

    # Create a list to store multiple Truck objects
    trucks = [
        vehicles.Truck('Toyota', 2002, 40000, 12000.0, '4WD'),
        vehicles.Truck('Ford', 2006, 50000, 15000.0, '2WD'),
        vehicles.Truck('Chevrolet', 2010, 55000, 17000.0, '4WD'),
        vehicles.Truck('Nissan', 2015, 45000, 19000.0, '2WD'),
        vehicles.Truck('GMC', 2018, 35000, 20000.0, '4WD'),
        vehicles.Truck('Ram', 2019, 30000, 22000.0, '4WD'),
        vehicles.Truck('Honda', 2016, 38000, 18000.0, '2WD'),
        vehicles.Truck('Jeep', 2014, 42000, 23000.0, '4WD'),
        vehicles.Truck('Dodge', 2017, 32000, 21000.0, '2WD'),
        vehicles.Truck('Mercedes-Benz', 2013, 40000, 25000.0, '4WD'),
        vehicles.Truck('BMW', 2011, 48000, 27000.0, '4WD'),
        vehicles.Truck('Volkswagen', 2009, 52000, 16000.0, '2WD'),
        vehicles.Truck('Subaru', 2007, 55000, 14000.0, '4WD'),
        vehicles.Truck('Kia', 2005, 60000, 12000.0, '2WD'),
        vehicles.Truck('Audi', 2003, 65000, 18000.0, '4WD'),
        vehicles.Truck('Mazda', 2001, 70000, 15000.0, '2WD'),
        vehicles.Truck('Hyundai', 1999, 75000, 13000.0, '4WD'),
        vehicles.Truck('Buick', 1997, 80000, 11000.0, '2WD'),
        vehicles.Truck('Chrysler', 1995, 85000, 10000.0, '4WD'),
        vehicles.Truck('Lincoln', 1993, 90000, 9000.0, '2WD')
    ]

    # Create a list to store multiple SUV objects
    suvs = [
        vehicles.SUV('Volvo', 2000, 30000, 18500.0, 5),
        vehicles.SUV('Honda', 2008, 35000, 20000.0, 7),
        vehicles.SUV('Nissan', 2012, 40000, 22000.0, 5),
        vehicles.SUV('Toyota', 2015, 25000, 24000.0, 8),
        vehicles.SUV('Chevrolet', 2019, 20000, 26000.0, 7),
        vehicles.SUV('Ford', 2017, 30000, 23000.0, 6),
        vehicles.SUV('GMC', 2013, 40000, 21000.0, 5),
        vehicles.SUV('Jeep', 2018, 35000, 22000.0, 6),
        vehicles.SUV('Dodge', 2016, 32000, 19000.0, 8),
        vehicles.SUV('Mercedes-Benz', 2014, 38000, 27000.0, 5),
        vehicles.SUV('BMW', 2012, 42000, 25000.0, 7),
        vehicles.SUV('Volkswagen', 2010, 45000, 23000.0, 6),
        vehicles.SUV('Subaru', 2008, 48000, 20000.0, 5),
        vehicles.SUV('Kia', 2006, 50000, 18000.0, 7),
        vehicles.SUV('Audi', 2004, 55000, 24000.0, 8),
        vehicles.SUV('Mazda', 2002, 60000, 16000.0, 6),
        vehicles.SUV('Hyundai', 2000, 65000, 15000.0, 5),
        vehicles.SUV('Buick', 1998, 70000, 14000.0, 7),
        vehicles.SUV('Chrysler', 1996, 75000, 12000.0, 8),
        vehicles.SUV('Lincoln', 1994, 80000, 11000.0, 6)
    ]

    print('USED CAR INVENTORY')
    print('=====================')

    # Display car data
    print('Cars in inventory:')
    for car in cars:
        print('Make:', car.get_make())
        print('Model:', car.get_model())
        print('Mileage:', car.get_mileage())
        print('Price:', car.get_price())
        print('Number of doors:', car.get_doors())
        print()

    # Display truck data
    print('Trucks in inventory:')
    for truck in trucks:
        print('Make:', truck.get_make())
        print('Model:', truck.get_model())
        print('Mileage:', truck.get_mileage())
        print('Price:', truck.get_price())
        print('Drive type:', truck.get_drive_type())
        print()

    # Display SUV data
    print('SUVs in inventory:')
    for suv in suvs:
        print('Make:', suv.get_make())
        print('Model:', suv.get_model())
        print('Mileage:', suv.get_mileage())
        print('Price:', suv.get_price())
        print('Passenger Capacity:', suv.get_pass_cap())
        print()

# Call the main function
main()

