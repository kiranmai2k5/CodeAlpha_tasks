import re

# File names
input_file = "data.txt"
output_file = "emails.txt"

# Step 1: Open and read the text file
with open(input_file, "r") as file:
    text = file.read()

# Step 2: Find email addresses using regular expression
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)

# Step 3: Save emails to another file
with open(output_file, "w") as file:
    for email in emails:
        file.write(email + "\n")

print("Task completed! Emails saved to emails.txt")
