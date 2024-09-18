# daily_reminder.py

# Prompt the user for a task description
task = input("Enter your task: ")

# Prompt the user for the task's priority
priority = input("Priority (high/medium/low): ").lower()

# Ask if the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Initialize the reminder variable with 'Reminder' for time-bound tasks, 'Note' for non-time-bound tasks
if time_bound == "yes":
    reminder_prefix = "Reminder"
else:
    reminder_prefix = "Note"

# Start building the reminder
reminder = f"{reminder_prefix}: '{task}' is a "

# Process the task based on priority
match priority:
    case "high":
        reminder += "high priority task"
    case "medium":
        reminder += "medium priority task"
    case "low":
        reminder += "low priority task"
    case _:
        reminder = "Invalid priority level."

# Modify the reminder based on whether the task is time-bound
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."

# Print the customized reminder
print(reminder)