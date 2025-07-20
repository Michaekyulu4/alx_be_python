# Prompt for task
task = input("Enter your task: ").strip()
while not task:
    task = input("Task cannot be empty. Please enter your task: ").strip()

# Prompt for priority
priority = input("Priority (high/medium/low): ").lower()
while priority not in ["high", "medium", "low"]:
    priority = input("Please enter a valid priority (high, medium, low): ").lower()

# Prompt for time sensitivity
time_bound = input("Is it time-bound? (yes/no): ").lower()
while time_bound not in ["yes", "no"]:
    time_bound = input("Please enter 'yes' or 'no': ").lower()

# Match case for priority
match priority:
    case "high":
        reminder = f"{task} is a high priority task"
    case "medium":
        reminder = f"{task} is a medium priority task"
    case "low":
        reminder = f"{task} is a low priority task"
    case _:
        reminder = f"Unspecified Priority Task: '{task}'"

# Add time-bound note
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."

# Print the final reminder
print(reminder)
