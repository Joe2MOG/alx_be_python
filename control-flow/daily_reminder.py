# daily_reminder.py

# Prompt the user for a task description
task = input("Enter your task: ")

# Prompt the user for the task's priority
priority = input("Priority (high/medium/low): ").lower()

# Ask if the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the task based on priority and time sensitivity
reminder = f"Reminder: '{task}' is a {priority} priority task"

# Modify the reminder based on whether the task is time-bound
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += "."

# Print the customized reminder
print(reminder)