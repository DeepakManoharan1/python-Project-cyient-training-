# 1. Basic function accepting any 'data' parameter
def display_data(data):
    print(f"Received ({type(data).__name__}): {data}")

# 2. Function with a default value for the 'data' parameter
def greet_user(data="Guest"):
    print(f"Welcome, {data}!")

# 3. Function processing a list of numbers passed as 'data'
def calculate_total(data):
    total = sum(data)
    return total

# 4. Function reading a dictionary passed as 'data'
def print_profile(data):
    name = data.get("name", "Unknown")
    role = data.get("role", "Member")
    print(f"User Profile -> Name: {name} | Role: {role}")

# --- Main execution block ---
if __name__ == "__main__":
    print("--- 1. Basic Data ---")
    display_data("Hello, Python!")
    display_data(42)

    print("\n--- 2. Default Parameter ---")
    greet_user()              # Uses default value
    greet_user("Aarav")       # Uses passed argument

    print("\n--- 3. List Data ---")
    scores = [10, 20, 30, 40]
    result = calculate_total(scores)
    print(f"Total Score: {result}")

    print("\n--- 4. Dictionary Data ---")
    user_info = {"name": "Priya", "role": "Developer"}
    print_profile(user_info)
