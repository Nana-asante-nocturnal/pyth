import pandas as pd

# Correct the number of entries to ensure all lists have the same length
data = {
    "Seriel Number": range(1, 11),  # 1 through 10 (10 entries)
    "Student Id": [""] * 10,  # 10 empty entries
    "Index Number": [
        "3377122", "3415222", "3402322", "3381622", "3369122",
        "3406522", "3419222", "3394222", "3390222", "3365122"
    ],
    "Full Name": [
        "Francis Nana Asante", "Richmond Tamakloe", "Naomi Nketsiah",
        "Baddoo Jeremiah Nii Adotei", "Caleb Frimpong Amoafo",
        "Kelvin Kwaku Opoku", "Donatus Zagla", "William Johnson",
        "Emmanuel Eli Komla Dzeble", "Agyapong Samuel Oduro"
    ],
    "Position": [
        "PROJECT MANAGER", "UI/UX DESIGNER", "UI/UX DESIGNER",
        "FRONT END", "FRONT END", "FRONT END", "BACKEND",
        "SYSTEMS DESIGNERS", "SYSTEMS DESIGNERS", "DEVOPS ENGINEER"
    ],
    "Punctuality": [None] * 10,
    "Input or Contribution": [None] * 10,
    "Communication and Feedback": [None] * 10,
    "Efficiency and Effectiveness": [None] * 10,
    "Compliance": [None] * 10,
    "Comments": [None] * 10
}

# Creating a DataFrame from the data
df_populated = pd.DataFrame(data)

# Save the DataFrame to an Excel file
df_populated.to_excel("output.xlsx", index=False)
