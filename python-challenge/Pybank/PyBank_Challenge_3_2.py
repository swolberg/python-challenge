import csv
import os

input_file = os.path.join("Resources", "budget_data.csv")
output_file = os.path.join("analysis", "budget_data_output.txt")

# Initialize variables
total_months = 0
total_sum = 0
monthly_changes = []
months = []
highest_increase = {"month": "", "change": 0}
highest_decrease = {"month": "", "change": float('inf')}

# Open and read CSV file
with open(input_file) as input_data:
    reader = csv.reader(input_data)
    header = next(reader)  # Skip header

    # Process the first row
    first_row = next(reader)
    total_months += 1
    total_sum += int(first_row[1])
    previous_value = int(first_row[1])

    # Process the rest of the rows
    for row in reader:
        total_months += 1
        current_value = int(row[1])
        total_sum += current_value

        # Calculate monthly change
        monthly_change = current_value - previous_value
        previous_value = current_value

        # Append month and change to respective lists
        months.append(row[0])
        monthly_changes.append(monthly_change)

        # Determine highest increase
        if monthly_change > highest_increase["change"]:
            highest_increase["month"] = row[0]
            highest_increase["change"] = monthly_change

        # Determine greatest decrease
        if monthly_change < highest_decrease["change"]:
            highest_decrease["month"] = row[0]
            highest_decrease["change"] = monthly_change

# Calculate average change
average_change = sum(monthly_changes) / len(monthly_changes)

# Prepare output
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_sum}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {highest_increase['month']} (${highest_increase['change']})\n"
    f"Greatest Decrease in Profits: {highest_decrease['month']} (${highest_decrease['change']})\n"
)

# Print output to terminal
print(output)

# Write output to text file
with open(output_file, "w") as txt_file:
    txt_file.write(output)



