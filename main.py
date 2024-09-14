from prettytable import PrettyTable
import matplotlib.pyplot as plt
import pandas as pd
import csv

# Question 1
myTable = PrettyTable(["Flower name", "Color", "Petal Count"])
myTable.add_row(["Rose", "Red", "20"])
myTable.add_row(["Sunflower", "Yellow", "50"])
myTable.add_row(["Tulip", "Pink", "10"])
myTable.add_row(["Daisy", "White", "15"])

print(myTable)

plt.style.use('bmh')
df = pd.read_csv('scores.csv')

x = df['Name']
y = df["Math Score"]

plt.xlabel('Name', fontsize=10)
plt.ylabel("Math Score", fontsize=16)
plt.bar(x, y)

plt.style.use('bmh')
df = pd.read_csv('scores.csv')

x = df['Name']
y = df["English Score"]

plt.xlabel('Name', fontsize=10)
plt.ylabel("Math Score", fontsize=16)
plt.bar(x, y)

meanMath = []
with open("scores.csv", 'r', newline="") as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        meanMath.append(float(row["Math Score"]))

mathAverage = sum(meanMath) / len(meanMath)

meanEnglish = []
with open("scores.csv", 'r', newline="") as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        meanEnglish.append(float(row["English Score"]))

englishAverage = sum(meanEnglish) / len(meanEnglish)

meanScience = []
with open("scores.csv", 'r', newline="") as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        meanScience.append(float(row["Science Score"]))
scienceAverage = sum(meanScience) / len(meanScience)

meanHistory = []
with open("scores.csv", 'r', newline="") as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        meanHistory.append(float(row["History Score"]))

historyAverage = sum(meanHistory) / len(meanHistory)

meanScore = [mathAverage, englishAverage, scienceAverage, historyAverage]

print(meanScore)

subjects = ["Math", "English", "Science", "History"]

plt.style.use('bmh')


x = subjects
y = meanScore

plt.xlabel('Name', fontsize=10)
plt.ylabel("Math Score", fontsize=16)
plt.bar(x, y)

plt.show()
