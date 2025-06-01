# Prompt for user input
task = input("Enter your task: ")
priority = input("Enter the priority level (high/medium/low): ").lower()
time_bound = input("Is the task time-bound? (yes/no): ").lower()

# Start building the reminder message
reminder = f"Reminder: '{task}' is a {priority} priority task"

# Match-case block for priority levels (Python 3.10+ required)
match priority:
    case "high":
        reminder += ". Handle it with top urgency"
    case "medium":
        reminder += ". Plan to complete it soon"
    case "low":
        reminder += ". You can do it at your convenience"
    case _:
        reminder += ". (Unrecognized priority level)"

# If the task is time-sensitive, append an urgent note
if time_bound == "yes":
    reminder += " that requires immediate attention today!"

# Print the final reminder
print("\n" + reminder)
