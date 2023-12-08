import sys

def calculate_downtime(input):
    # Parsing the input
    system, failures, downtime, restart = input.split()
    failures, downtime, restart = int(failures), int(downtime), int(restart)

    # Calculating total downtime per month
    total_downtime = (failures * downtime) + (failures * restart)

    return system, total_downtime

def find_most_reliable_system(inputs):
    min_downtime = float('inf')
    most_reliable_system = None

    for input in inputs:
        system, downtime = calculate_downtime(input)
        
        if downtime < min_downtime:
            min_downtime = downtime
            most_reliable_system = system

    return most_reliable_system

def main():
    inputs = sys.stdin.readlines()
    most_reliable_system = find_most_reliable_system(inputs)
    print(most_reliable_system)

if __name__ == "__main__":
    main()
