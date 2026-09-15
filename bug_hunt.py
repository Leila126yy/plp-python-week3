count = 1
total = 0

while count <=5
    total = total + count
    count = count + 1

# BUG: total is a number, so I used an f-string to print it with the text.
print(f"Sum of 1 to 5 is: {total}")
