rows = int(input("Enter rows: "))
cols = int(input("Enter columns: "))

matrix = {}

for r in range(rows):
    print(f"Row {r+1}")
    for c in range(cols):
        num = float(input(f"Enter number {c+1}: "))
        matrix[(r,c)] = num

print("\nThe numbers are:")
for r in range(rows):
    for c in range(cols):
        print(matrix[(r,c)], end=" ")
    print()

search = float(input("Enter search value: "))

for r in range(rows):
    for c in range(cols):
        if matrix[(r,c)] == search:
            print(f"The number is found at Row {r+1}, Col {c+1}")