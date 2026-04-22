import pandas as pd

data = [
    {"date": "2026-04-01", "item": "Groceries", "amount": 250},
    {"date": "2026-04-02", "item": "Electricity bill", "amount": 180},
    {"date": "2026-04-03", "item": "Transport", "amount": 60},
    {"date": "2026-04-04", "item": "Internet", "amount": 120},
]

df = pd.DataFrame(data)

total = df["amount"].sum()

df.loc[len(df)] = ["TOTAL", "", total]

df.to_excel("expenses.xlsx", index=False)

print("Done")
