class Vehicle:
    def __init__(self, name, seating_capacity):
        self.name = name
        self.seating_capacity = seating_capacity

    def fare(self):
        # Default fare is seating capacity * 100
        return self.seating_capacity * 100

class Bus(Vehicle):
    def fare(self):
        # Get the base fare from the parent (Vehicle) class
        base_fare = super().fare()
        
        # Add a 10% maintenance charge to the full fare
        total_fare = base_fare + (0.10 * base_fare)
        return total_fare

# Testing the implementation
School_Bus = Bus("School Volvo", 50)
print(f"Total Bus fare is: INR {School_Bus.fare()}")
