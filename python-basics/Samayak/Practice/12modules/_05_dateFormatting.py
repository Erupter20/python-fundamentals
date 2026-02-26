# Get the current date and format it to display only the month and year (e.g., October 2024).

from datetime import datetime
month  = datetime.now()
formatted = month.strftime("%m")
print(formatted)
