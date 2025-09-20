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
