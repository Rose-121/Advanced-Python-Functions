num = int(input("Enter your number:"))
l1 = []

for i in range(0,num+1):
    l1.append(i)

print(l1)

odd = [l1 for l1 in num if l1%2 == 0]
print("List of odd numbers from original:",odd)

students = ["nusaiba","nabila","rose"]

capstudents = []

capstudents.append(students[0].capitalize())

print(capstudents)