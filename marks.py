import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Data
tests = ['Test 1', 'Test 2', 'Test 3', 'Test 4', 'Test 5']
marks = [0, 0, 22, 18, 0]  # 0 for not attended/missed

# Create DataFrame
df = pd.DataFrame({
    'Test': tests,
    'Marks': marks
})

print(df)

# ---------------- BAR CHART ----------------
plt.figure()
plt.bar(df['Test'], df['Marks'])
plt.title('Marks in Weekly Tests')
plt.xlabel('Tests')
plt.ylabel('Marks (Out of 25)')
plt.show()

# ---------------- PIE CHART ----------------
# Only attended tests for meaningful pie
attended_marks = df[df['Marks'] > 0]

plt.figure()
plt.pie(attended_marks['Marks'], labels=attended_marks['Test'], autopct='%1.1f%%')
plt.title('Marks Distribution (Attended Tests)')
plt.show()

# ---------------- HISTOGRAM ----------------
plt.figure()
plt.hist(df['Marks'], bins=5)
plt.title('Histogram of Marks')
plt.xlabel('Marks')
plt.ylabel('Frequency')
plt.show()
