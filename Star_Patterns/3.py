"""
    * * * * *
    * * * *
    * * *
    * *
    *
"""

n = int(input("Please enter a odd number : "))

for i in range(n):
    for j in range(n - i):
        print("* ", end = "")
    print()