
import math
import vehicles
import turtle
# from flower import *
import flower as fl
import random

def generate_random_length():
    a = 400
    b = 600  
    u = random.random()
    return a + u * (b - a)
    

# Function used to generate colors randomly
def gencolors():
    return ((random.random(),random.random(),random.random()))

# Function to draw the truck
def drawtruck():
    # Adjust these parameters to change the size of the truck
    rec_length = generate_random_length()  # Adjust the range of random values
    rec_height = rec_length / 2

    #truck head
    square_height = rec_height 
    square_length = rec_height / 1.5
    #WINDOW
    small_square_height = square_length/1.4
    
    #side mirror

    side_mirror_length = small_square_height/5
    side_mirror_height = small_square_height/4
    
    # Area of rectangle
    rec_area = rec_length * rec_height

    # Dimensions of parallelogram
    seat_height = small_square_height / 3.5
    seat_length = small_square_height / 3.5

    # Dimensions of tire.
    # Ratio of areas of rectangle and tire is 25.75
    rec_tire_area = rec_area / 20.75
    tire_radius = math.sqrt(rec_tire_area / math.pi)

    # Various coordinates used to draw
    rec_coords= [0,0]
    tire_1_coords = [-(square_length/2),-(square_height/4)]
    tire_2_coords = [(rec_length/1.141),-(rec_height/4)]
    small_square_coords = [-(square_length/4.3),(square_height/1.05)]
    square_coords = [0, rec_length / 2]
    seat_1_coords = [(small_square_coords[0]*2.5),small_square_coords[1]*0.5]
    side_mirror_coords = [-(square_length/1.245),(square_length)]


    # truck head
    turtle.fillcolor(gencolors())
    turtle.penup()
    turtle.setheading(180)
    turtle.goto(square_coords[0],square_coords[1]) 
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(square_length)
    turtle.left(90)
    turtle.forward(square_height)
    turtle.left(90)
    turtle.forward(square_length)
    turtle.left(90)
    turtle.forward(square_height)
    turtle.end_fill()

   # window
    
    turtle.fillcolor(1.0, 0.95, 0.85)
    turtle.penup()
    turtle.setheading(180)
    turtle.goto(small_square_coords[0],small_square_coords[1]) 
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(small_square_height)
    turtle.left(90)
    turtle.forward(small_square_height)
    turtle.left(90)
    turtle.forward(small_square_height)
    turtle.left(90)
    turtle.forward(small_square_height)
    turtle.end_fill()
    
    #side mirror
    turtle.fillcolor((0.0,0.0,0.0))
    turtle.penup()
    turtle.setheading(180)
    turtle.goto(side_mirror_coords[0],side_mirror_coords[1]) 
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(side_mirror_length)
    turtle.left(90)
    turtle.forward(side_mirror_height)
    turtle.left(90)
    turtle.forward(side_mirror_length)
    turtle.left(90)
    turtle.forward(side_mirror_height)
    turtle.end_fill()
    
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

    # Below code for drawing seat
    turtle.fillcolor((0.0, 0.0, 0.0))
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


    # Drawing two tires
    turtle.setheading(360)
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

def generate_random_truck():
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
    vehicles.Truck('Kia', 2005, 60000, 12000.0, '2WD'),
    vehicles.Truck('Audi', 2003, 65000, 18000.0, '4WD'),
    vehicles.Truck('Mazda', 2001, 70000, 15000.0, '2WD'),
    vehicles.Truck('Hyundai', 1999, 75000, 13000.0, '4WD'),
    vehicles.Truck('Buick', 1997, 80000, 11000.0, '2WD'),
    vehicles.Truck('Chrysler', 1995, 85000, 10000.0, '4WD'),
    vehicles.Truck('Lincoln', 1993, 90000, 9000.0, '2WD'),
    vehicles.Truck('Tesla', 2023, 0, 50000.0, 'Electric')

]

    truck = random.choice(trucks)
    return truck

def main():
    fl.main()

    drawtruck()
    
    #Create a Truck object for a used 2002
    #Toyota pickup with 40 000 miles, priced 
    #at $12, 000, with a 4-wheel drive.
    truck = generate_random_truck()
    
    # Writing the text on screen for details about the BMW
    boldfont=("Times",14, "bold") # Font used for writing on screen
    regfont = ("Times",12, "normal") # Regular font
    turtle.penup()
    turtle.goto(-635,325)
    turtle.right(90)
    turtle.write("SIMULATION INVENTORY",font=boldfont)
    turtle.goto(-635,315)
    turtle.write('======================',font=boldfont)
    turtle.goto(-635,305)
    turtle.write('The following truck is in inventory:',font=regfont)
    turtle.goto(-635,285)
    turtle.write('Make:',font=boldfont)
    turtle.goto(-550,285)
    turtle.write(f'{truck.get_make()}',font=regfont)
    turtle.goto(-635,265)
    turtle.write('Model:',font=boldfont)
    turtle.goto(-550,265)
    turtle.write(f'{truck.get_model()}',font=regfont)
    turtle.goto(-635,245)
    turtle.write('Mileage:',font=boldfont)
    turtle.goto(-550,245)
    turtle.write(f'{truck.get_mileage()}',font=regfont)
    turtle.goto(-635,225)
    turtle.write('Price:',font=boldfont)
    turtle.goto(-550,225)
    turtle.write(f'{truck.get_price()}',font=regfont)
    turtle.goto(-635,205)
    turtle.write('Drive type:',font=boldfont)
    turtle.goto(-540,205)
    turtle.write(f'{truck.get_drive_type()}',font=regfont)
    turtle.done()