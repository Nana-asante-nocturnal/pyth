import csv
import matplotlib.pyplot as plt
import pandas as pd

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
