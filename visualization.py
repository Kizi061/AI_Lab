import pandas as pd 
import matplotlib.pyplot as plt

data = {
    "Student": ["Alice", "Bob", "Eve", "David"],
    "Math": [23,54,65,75],
    "Science":[76,78,76,76],
    "English":[86,65,76,97],
    "Gender": ["Female", "Male", "Male", "Male"]
    }

df2 = pd.DataFrame(data)

print(df2)

# plt.figure(figsize=(10, 6))
# plt.bar(df2["Student"], df2["Math"], color="blue", label="Math")
# plt.bar(df2["Student"], df2["Science"], color="green", label="Science")
# plt.bar(df2["Student"], df2["English"], color="red", label="English")
# plt.legend()
# plt.show()

plt.figure(figsize=(10, 6))
plt.plot(df2["Student"], df2["Math"], color="blue", label="Math")
plt.plot(df2["Student"], df2["Science"], color="green", label="Science")
plt.plot(df2["Student"], df2["English"], color="red", label="English")
plt.legend()
plt.show()

# plt.figure(figsize=(10, 6))
# plt.plot(df2["Student"], df2["Math"], color="blue", label="Math")
# # plt.plot(df2["Student"], df2["Science"], color="green", label="Science")
# # plt.plot(df2["Student"], df2["English"], color="red", label="English")
# plt.legend()
# plt.show()

# plt.figure(figsize=(10, 6))
# # plt.plot(df2["Student"], df2["Math"], color="blue", label="Math")
# plt.plot(df2["Student"], df2["Science"], color="green", label="Science")
# plt.plot(df2["Student"], df2["English"], color="red", label="English")
# plt.legend()
# plt.show()