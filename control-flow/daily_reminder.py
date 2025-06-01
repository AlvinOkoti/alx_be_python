# Prompt user for task details
task = input("Enter your task: ")
priority = input("Enter the priority level (high/medium/low): ").lower()
time_bound = input("Is the task time-bound? (yes/no): ").lower()

# Base reminder message
reminder = f"Reminder: '{task}' is a {priority} priority task"

# Use match-case to tailor the message based on priority
match priority:
    case "high":
        reminder += ". Handle it with top urgency"
    case "medium":
        reminder += ". Try to get it done soon"
    case "low":
        reminder += ". You can do this at your convenience"
    case _:
        reminder += ". (Unrecognized priority)"

# Modify the reminder if the task is time-bound
if time_bound == "yes":
    reminder += " that requires immediate attention today!"

# Print the customized reminder
print("\n" + reminder)