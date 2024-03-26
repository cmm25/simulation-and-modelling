import math
import random

Q_LIMIT = 100
BUSY = 1
IDLE = 0

def initialize():
    """
    Initialize simulation variables.
    """
    global sim_time, server_status, num_in_q, time_last_event, time_next_event, num_custs_delayed, total_of_delays, area_num_in_q, area_server_status
    sim_time = 0
    server_status = IDLE
    num_in_q = 0
    time_last_event = 0.0
    num_custs_delayed = 0
    total_of_delays = 0.0
    area_num_in_q = 0.0
    area_server_status = 0.0
    time_next_event = [0] * 3
    time_next_event[1] = sim_time + expon(mean_interarrival)
    time_next_event[2] = 1.0e+30

def timing():
    """
    Determine the next event and advance simulation time.
    """
    global sim_time, next_event_type
    min_time_next_event = 1.0e+29
    next_event_type = 0
    for i in range(1, num_events + 1):
        if time_next_event[i] < min_time_next_event:
            min_time_next_event = time_next_event[i]
            next_event_type = i
    if next_event_type == 0:
        print("\nEvent list is empty at time", sim_time)
        exit(1)
    sim_time = min_time_next_event

def arrive():
    """
    Handle arrival event.
    """
    global sim_time, server_status, num_in_q, total_of_delays, num_custs_delayed
    time_next_event[1] = sim_time + expon(mean_interarrival)
    if server_status == BUSY:
        num_in_q += 1
        if num_in_q > Q_LIMIT:
            print("\nOverflow of the array time_arrival at time", sim_time)
            exit(2)
        time_arrival[num_in_q] = sim_time
    else:
        delay = 0.0
        total_of_delays += delay
        num_custs_delayed += 1
        server_status = BUSY
        time_next_event[2] = sim_time + expon(mean_service)

def depart():
    """
    Handle departure event.
    """
    global sim_time, num_in_q, total_of_delays, num_custs_delayed, server_status
    if num_in_q == 0:
        server_status = IDLE
        time_next_event[2] = 1.0e+30
    else:
        num_in_q -= 1
        delay = sim_time - time_arrival[1]
        total_of_delays += delay
        num_custs_delayed += 1
        time_next_event[2] = sim_time + expon(mean_service)
        for i in range(1, num_in_q + 1):
            time_arrival[i] = time_arrival[i + 1]

def report():
    """
    Generate a report of simulation results.
    """
    global total_of_delays, num_custs_delayed, sim_time, area_num_in_q, area_server_status
    with open("mm1.out", "w") as outfile:
        outfile.write("Single server queuing system\n\n")
        outfile.write("Mean inter-arrival time%11.3f minutes\n\n" % mean_interarrival)
        outfile.write("Mean service time%16.3f minutes\n\n" % mean_service)
        outfile.write("Number of customers%14d\n\n" % num_delays_required)
        outfile.write("Average delay in queue%11.3f minutes\n\n" % (total_of_delays / num_custs_delayed))
        outfile.write("Average number in queue%10.3f\n\n" %
                      (area_num_in_q / sim_time))
        outfile.write("Server utilization%15.3f\n\n" % (area_server_status / sim_time))
        outfile.write("Time simulation ended%12.3f minutes" % sim_time)

def update_time_avg_stats():
    """
    Update time-average statistical accumulators.
    """
    global sim_time, time_last_event, area_num_in_q, area_server_status
    time_since_last_event = sim_time - time_last_event
    time_last_event = sim_time
    area_num_in_q += num_in_q * time_since_last_event
    area_server_status += server_status * time_since_last_event

def expon(mean):
    """
    Generate an exponential random variable.
    """
    return -mean * math.log(random.random())  # Using random.random() for exponential distribution

# Open input file
with open("mm1.in", "r") as infile:
    mean_interarrival, mean_service, num_delays_required = map(float, infile.readline().split())

# Initialize variables
num_events = 2
time_arrival = [0] * (Q_LIMIT + 1)

# Initialize simulation
initialize()

# Run simulation
while num_custs_delayed < num_delays_required:
    timing()
    update_time_avg_stats()
    if next_event_type == 1:
        arrive()
    elif next_event_type == 2:
        depart()

# Generate report and end simulation
report()