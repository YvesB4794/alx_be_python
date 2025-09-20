# daily_reminder.py
"""
# Ask user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Match Case for priority
match priority:
    case "high":
        message = f"'{task}' is a high priority task"
    case "medium":
        message = f"'{task}' is a medium priority task"
    case "low":
        message = f"'{task}' is a low priority task"
    case _:
        message = f"'{task}' has an unknown priority"

# Add time-bound condition
if time_bound == "yes":
    message += " that requires immediate attention today!"
else:
    message += ". Consider completing it when you have free time."

# Final reminder
print("\nReminder:", message)

# Optional: Simple loop reminder (repeats 3 times for emphasis)
for i in range(3):
    print(f"({i+1}) {message}") """
"""
    # daily_reminder.py

# Prompt user for inputs
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process task using Match Case
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = f"'{task}' has an unknown priority"

# Add time sensitivity with if condition
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."

# Print final reminder
print("\nReminder:", reminder)

# Simple loop to emphasize reminder (repeats twice)
print("\nRepeating Reminder:")
count = 0
while count < 1:
    print(f"({count+1}) {reminder}")
    count += 1
"""
# daily_reminder.py

# Prompt for a non-empty task
while True:
    task = input("Enter your task: ").strip()
    if task:
        break
    print("Please enter a non-empty task.")

# Prompt for priority and validate (accepts full words or single-letter shortcuts)
priority_map = {"h": "high", "m": "medium", "l": "low"}
valid_priorities = {"high", "medium", "low"}
while True:
    priority = input("Priority (high/medium/low): ").strip().lower()
    if priority in valid_priorities:
        break
    if priority in priority_map:
        priority = priority_map[priority]
        break
    print("Invalid priority. Please enter 'high', 'medium', or 'low' (or h/m/l).")

# Prompt for time-bound and validate (accepts yes/no or y/n)
while True:
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()
    if time_bound in {"yes", "no"}:
        break
    if time_bound in {"y", "n"}:
        time_bound = "yes" if time_bound == "y" else "no"
        break
    print("Please answer 'yes' or 'no' (or y/n).")

# Build a customized reminder using match-case for priority
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = f"'{task}' has an unknown priority"

# Modify reminder based on time sensitivity
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."

# Output the final customized reminder
print("\nReminder:", reminder)
