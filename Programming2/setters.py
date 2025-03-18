budget = 30000
print(f"\nIs car1 affordable? {car1.is_affordable(budget)}")
print(f"Is car3 affordable? {car3.is_affordable(budget)}")


# Checking senior status
print(f"Is {patient1.get_name()} a senior? {patient1.is_senior()}")  # Output: True
print(f"Is {patient2.get_name()} a senior? {patient2.is_senior()}")  # Output: False
print(f"Is {patient3.get_name()} a senior? {patient3.is_senior()}")  # Output: True
