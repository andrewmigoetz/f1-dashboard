import fastf1 as f1
import os
import pandas as pd

os.makedirs("cache", exist_ok=True)
os.makedirs("results", exist_ok=True)
f1.Cache.enable_cache('cache')

gps = ['australia', 'china', 'japan', 'bahrain', 'saudi', 'miami', 'emilia']
sessions = {}
all_results = []

for gp in gps:
    session = f1.get_session(2025,gp,'R')
    session.load()
    sessions[gp] = session
    df = session.results.copy()

    df['Grand Prix'] = session.event['EventName']
    df['Date'] = session.date.date()
    df['Round'] = session.event['RoundNumber']

    filename = f"results/{gp}_2025_results.csv"
    df.to_csv(filename, index=False)
    print(f"Saved: {filename}")
    all_results.append(df)

combined = pd.concat(all_results, ignore_index=True)

combined.to_csv("results/f1_2025_combined_results.csv", index=False)
print("Saved: results/f1_2025_combined_results.csv")

combined.to_excel("results/f1_2025_combined_results.xlsx", index=False, engine='openpyxl')

print("Saved: results/f1_2025_combined_results.xlsx")

