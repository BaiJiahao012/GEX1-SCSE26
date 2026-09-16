###########################################################
""" Do not rename the variables or functions.
Do not change the function parameters.
Do not add input() calls inside airport_manager.py.
The file must be importable by the tests. """
###########################################################

airport_info = ("OUL", 1, "14-09-2026")
allowed_gates = {"A1", "A2", "A3", "A4", "B1", "B2"}
restricted_destinations = {"Moscow", "Pyongyang"}
flights = {
    "AY450": {
        "destination": "Helsinki",
        "departure": "08:30",
        "gate": "A2",
        "capacity": 5,
        "passengers": ["Alice Wong", "David Kim", "Fatima Ali"]
    },
    "SK271": {
        "destination": "Stockholm",
        "departure": "10:15",
        "gate": "B1",
        "capacity": 4,
        "passengers": ["Chen Wei", "George Smith"]
    },
    "LH2491": {
        "destination": "Munich",
        "departure": "12:40",
        "gate": "A4",
        "capacity": 5,
        "passengers": ["Hana Lee", "Maria Garcia", "Noah Wilson"]
    }
}


## Logic to find if a flight exists
def find_flight(flights, flight_number):
    # Check if the flight number is empty
    if not flight_number:
        return None
        
    # Convert to string, remove spaces, and change to uppercase
    flight_num_str = str(flight_number)
    flight_num_clean = flight_num_str.strip()
    flight_key = flight_num_clean.upper()
    
    # Check if it exists in the dictionary
    if flight_key in flights:
        return flight_key
    else:
        return None


## Logic to find if a passenger exists
def passenger_exists(passengers, passenger_name):
    # Check if the input name is empty
    if not passenger_name:
        return False
        
    # Process name: convert to string, remove spaces, and lower case for comparison
    name_str = str(passenger_name)
    name_clean = name_str.strip()
    name_lower = name_clean.lower()
    
    # Loop through each passenger in the list
    for p_name in passengers:
        if p_name.lower() == name_lower:
            return True
            
    return False


## Logic to check in a passenger
def check_in_passenger(flights, flight_number, passenger_name, restricted_destinations):
    flight_key = find_flight(flights, flight_number)
    
    # Check if flight exists
    if not flight_key:
        return "FLIGHT_NOT_FOUND"
        
    # Check if the name is empty or None
    if not passenger_name:
        return "EMPTY_NAME"
        
    name_str = str(passenger_name)
    name_clean = name_str.strip()
    if not name_clean:
        return "EMPTY_NAME"
        
    target_flight = flights[flight_key]
    flight_dest = target_flight["destination"]
    
    # Check if the destination is restricted
    if flight_dest in restricted_destinations:
        return "RESTRICTED"
        
    # Check if passenger already exists in the list to avoid duplicate
    flight_passengers = target_flight["passengers"]
    if passenger_exists(flight_passengers, name_clean):
        return "DUPLICATE"
        
    # Validate if the flight capacity is full
    current_count = len(flight_passengers)
    max_capacity = target_flight["capacity"]
    if current_count >= max_capacity:
        return "FULL"
        
    # Format name to Title Case before appending
    name_formatted = name_clean.title()
    
    # All validations passed, append new data to list
    target_flight["passengers"].append(name_formatted)
    return "OK"


## Logic to remove a passenger from a flight
def remove_passenger(flights, flight_number, passenger_name):
    flight_key = find_flight(flights, flight_number)
    
    if not flight_key:
        return "FLIGHT_NOT_FOUND"
        
    if not passenger_name:
        return "PASSENGER_NOT_FOUND"
        
    name_str = str(passenger_name)
    name_clean = name_str.strip()
    name_lower = name_clean.lower()
    
    target_flight = flights[flight_key]
    flight_passengers = target_flight["passengers"]
    
    # Use enumerate to find the index and remove the participant
    for index, p_name in enumerate(flight_passengers):
        if p_name.lower() == name_lower:
            flight_passengers.pop(index)
            return "OK"
            
    return "PASSENGER_NOT_FOUND"


# Logic to change the gate of a flight
def change_gate(flights, flight_number, new_gate, allowed_gates):
    flight_key = find_flight(flights, flight_number)
    
    if not flight_key:
        return "FLIGHT_NOT_FOUND"
        
    # Process new gate input
    gate_str = str(new_gate)
    gate_clean = gate_str.strip()
    gate_upper = gate_clean.upper()
    
    # Check if the new gate is valid
    if gate_upper not in allowed_gates:
        return "INVALID_GATE"
    else:
        target_flight = flights[flight_key]
        target_flight["gate"] = gate_upper
        return "OK"


# Logic to get the status of a flight
def flight_status(flight):
    flight_passengers = flight["passengers"]
    passenger_count = len(flight_passengers)
    max_capacity = flight["capacity"]
    
    # Calculate the percentage
    percentage = (passenger_count / max_capacity) * 100
    
    # Return status based on the percentage
    if percentage >= 100:
        return "FULL"
    elif percentage >= 75:
        return "ALMOST FULL"
    else:
        return "AVAILABLE"


# Logic to get the sorted manifest of a flight
def sorted_manifest(flights, flight_number):
    flight_key = find_flight(flights, flight_number)
    
    if not flight_key:
        return None
        
    target_flight = flights[flight_key]
    flight_passengers = target_flight["passengers"]
    
    # Create and return a sorted list
    sorted_list = sorted(flight_passengers)
    return sorted_list


# Logic to get the total number of passengers across all flights
def total_passengers(flights):
    total_count = 0
    
    # Use a for loop to calculate the total passenger count
    for flight_info in flights.values():
        flight_passengers = flight_info["passengers"]
        passenger_count = len(flight_passengers)
        total_count = total_count + passenger_count
        
    return total_count


# Logic to check if any flight is full
def any_full_flight(flights):
    for flight_info in flights.values():
        flight_passengers = flight_info["passengers"]
        passenger_count = len(flight_passengers)
        max_capacity = flight_info["capacity"]
        
        # Check if the current flight is full
        if passenger_count >= max_capacity:
            return True
            
    return False


# Logic to check if all flights have at least one passenger
def all_flights_have_passengers(flights):
    if not flights:
        return False
        
    for flight_info in flights.values():
        flight_passengers = flight_info["passengers"]
        passenger_count = len(flight_passengers)
        
        if passenger_count == 0:
            return False
            
    return True
'''
AI Usage Declaration:
In accordance with the course guidelines, 
I used a free, open-source AI (local LLM) purely as a supplementary tool for non-core development tasks.
Specifically, the AI assisted with identifying minor syntax errors, formatting the code to maintain a consistent personal style, and generating code comments to improve readability. 
The core algorithmic logic, step-by-step implementation, and data structure selection (Tuples, Sets, Dictionaries, Lists) were developed entirely independently. 
I strictly complied with the course rules and confirm that no AI agent frameworks (such as OpenClaw, Dify, or MetaGPT) or paid models were used in the development of this assignment.
'''