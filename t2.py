"""Task 2:
Find and Count Duplicates in a List and print it on screen.
numbers = [4, 5, 6, 4, 7, 8, 5, 9, 4, 7, 6, 10]
# this list may have N number of element
Expected output:
Duplicate Numbers and Their Counts:
4 appears 3 times
5 appears 2 times
6 appears 2 times
7 appears 2 times"""

numbers = [4, 5, 6, 4, 7, 8, 5, 9, 4, 7, 6, 10]

duplicates = {}

for n in numbers:
    if n in duplicates:
        duplicates[n] += 1
    else:
        duplicates[n] = 1

for number, count in duplicates.items():
    if count > 1:
        print(f"{number} appears {count} times")