import math
import vehicles
# import subprocess
import random
# from flower import *
import flower as fl
import truck as tr
import suv as sv
import turtle
from turtle import Screen
from tkinter import *
import random

# Function to generate random length for the car
def generate_random_length():
    a = 300
    b = 500
    u = random.random()

    return (a + u*(b -a)) # Adjust the range as needed

# # Function used to generate colors randomly
def gencolors():
    return ((random.random(),random.random(),random.random()))

# Function to draw the Car
def drawcar():

    # Dimensions of rectangle
    # rec_length = len() # Length of car is randomly generated
    rec_length = generate_random_length()
    rec_height = rec_length / 8

    # Dimensions of roof - trapezium shape with angle of 45 degrees
    roof_height = rec_height * 1.4
    roof_splitter = math.sin(math.radians(45)) * roof_height
    # roof splitter has same values as y since angle is 45

    # Ratio of areas of rectangle and roof is 1.475
    rec_area = rec_length * rec_height
    roof_area = rec_area / 1.475
    roof_length = (roof_area - (roof_splitter * roof_splitter)) / roof_splitter

    # Dimensions of parallelogram
    seat_height = roof_height / 2.5
    seat_length = roof_length / 15
    # Dimensions of tire.
    # Ratio of areas of rectangle and tires is 14.75
    tire_area = rec_area / 10
    tire_radius = math.sqrt(tire_area / math.pi)

    # Various coordinates used to draw
    rec_coords= [0,0]
    roof_coords = [(rec_length/8),(rec_height)]
    window_coords = [(roof_coords[0]*4.5),roof_coords[1]]
    seat_1_coords = [(roof_coords[0]*2.5),roof_coords[1]]
    seat_2_coords = [(roof_coords[0]*5.0),roof_coords[1]]
    tire_1_coords = [(rec_length/6),(rec_height/3)]
    tire_2_coords = [(rec_length/1.121),(rec_height/3)]

    # Below code for drawing rectangular upper body
    turtle.fillcolor(gencolors())
    turtle.penup()
    turtle.setheading(360)

    turtle.goto(rec_coords[0],rec_coords[1]) # rec_coords
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(rec_length)
    turtle.left(90)
    turtle.forward(rec_height)
    turtle.left(90)
    turtle.forward(rec_length)
    turtle.left(90)
    turtle.forward(rec_height)
    turtle.end_fill()


    # Below code for drawing roof and window
    turtle.penup()
    turtle.goto(roof_coords[0],roof_coords[1]) # roof coords
    turtle.pendown()
    turtle.setheading(45)
    turtle.forward(roof_height)
    turtle.setheading(0)
    turtle.forward(roof_length)

    turtle.setheading(-45)
    turtle.forward(roof_height)
    turtle.setheading(90)
    turtle.penup()
    turtle.goto(window_coords[0],window_coords[1]) # window coords
    turtle.pendown()
    turtle.forward(roof_splitter)

    # Below code for drawing seats 
    turtle.fillcolor(gencolors())
    turtle.setheading(90)
    turtle.penup()
    turtle.goto(seat_1_coords[0],seat_1_coords[1]) # window coords
    turtle.pendown()
    turtle.begin_fill()
    turtle.setheading(45)
    turtle.forward(seat_height)
    turtle.setheading(360)
    turtle.forward(seat_length)
    turtle.setheading(-135)
    turtle.forward(seat_height)
    turtle.setheading(-180)
    turtle.forward(seat_length)
    turtle.end_fill()

    turtle.fillcolor(gencolors())
    turtle.setheading(90)
    turtle.penup()
    turtle.goto(seat_2_coords[0],seat_2_coords[1]) # window coords
    turtle.pendown()
    turtle.begin_fill()
    turtle.setheading(45)
    turtle.forward(seat_height)
    turtle.setheading(360)
    turtle.forward(seat_length)
    turtle.setheading(-135)
    turtle.forward(seat_height)
    turtle.setheading(-180)
    turtle.forward(seat_length)
    turtle.end_fill()

    # Below code for drawing two tires
    turtle.penup()
    turtle.goto(tire_1_coords[0],tire_1_coords[1])
    turtle.pendown()
    turtle.fillcolor((0.0, 0.0, 0.0))
    turtle.begin_fill()
    turtle.circle(tire_radius)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(tire_2_coords[0],tire_2_coords[1])
    turtle.pendown()
    turtle.fillcolor((0.0, 0.0, 0.0))


    turtle.begin_fill()
    turtle.circle(tire_radius)
    turtle.end_fill()

def open_suv_window():
    turtle.clearscreen()
    sv.main()


def open_truck_window():
    # Clear existing drawings
    turtle.clearscreen()
    # Draw the truck
    tr.main()  # main() in truck.py contains the code to draw the truck

def open_car_window():
    turtle.clearscreen()
    fl.main()
    main()

def exit_program(screen):
    screen.bye()  # Close the window


def generate_random_car():
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
   
    car = random.choice(cars)
    return car

def main():
    screen = Screen()
    screen.bgcolor("#E0E0E0")
    screen.setup(width=1000, height=700)
 
    drawcar()
    canvas = screen.getcanvas()
    button_car = Button(canvas.master, text="See CAR", command=open_car_window, bg="#FFA07A", font=("Arial", 12), padx=10, pady=5)
    button_suv = Button(canvas.master, text="See SUV", command=open_suv_window, bg="#98FB98", font=("Arial", 12), padx=10, pady=5)
    button_truck = Button(canvas.master, text="See TRUCK", command=open_truck_window, bg="#87CEFA", font=("Arial", 12), padx=10, pady=5)
    button_exit = Button(canvas.master, text="Exit", command=lambda: exit_program(screen), bg="#FFD700", font=("Arial", 12), padx=10, pady=5)

    # Pack and place the buttons with padding
    button_exit.pack(pady=5)
    button_exit.place(x=10, y=160)

    button_car.pack(pady=5)
    button_car.place(x=10, y=10)

    button_suv.pack(pady=5)
    button_suv.place(x=10, y=60)

    button_truck.pack(pady=5)
    button_truck.place(x=10, y=110) 

    #Create a Car object for a used 2001 BMW
    #with 70,000 miles, priced at $15,000, with
    #4 doors.
    car = generate_random_car()

    # Writing the text on screen for details about the BMW
    boldfont=("Times",14, "bold") # Font used for writing on screen
    regfont = ("Times",12, "normal") # Regular font
    turtle.penup()
    turtle.goto(-635,325)
    turtle.right(90)
    turtle.write("SIMULATION INVENTORY",font=boldfont)
    turtle.goto(-635,315)
    turtle.write('=====================',font=boldfont)
    turtle.goto(-635,305)
    turtle.write('The following car is in inventory:',font=regfont)
    turtle.goto(-635,285)
    turtle.write('Make:',font=boldfont)
    turtle.goto(-550,285)
    turtle.write(f'{car.get_make()}',font=regfont)
    turtle.goto(-635,265)
    turtle.write('Model:',font=boldfont)
    turtle.goto(-550,265)
    turtle.write(f'{car.get_model()}',font=regfont)
    turtle.goto(-635,245)
    turtle.write('Mileage:',font=boldfont)
    turtle.goto(-550,245)
    turtle.write(f'{car.get_mileage()}',font=regfont)
    turtle.goto(-635,225)
    turtle.write('Price:',font=boldfont)
    turtle.goto(-550,225)
    turtle.write(f'{car.get_price()}',font=regfont)
    turtle.goto(-635,205)
    turtle.write('Number of doors:',font=boldfont)
    turtle.goto(-485,205)
    turtle.write(f'{car.get_doors()}',font=regfont)
    turtle.done()

   
    screen.mainloop()

main()
# mainloop()