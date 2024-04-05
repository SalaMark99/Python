import matplotlib.pyplot as plt
import numpy as np

# Adatok a piaci előrejelzéshez
years = np.array([2022, 2023, 2030])
market_values_grandview = np.array([80.21, 93.98, 338.28])  # Grand View Research adatai (2022-2030)
market_values_marketsandmarkets = np.array([80.21, 93.98, 338.28])  # Markets and Markets adatai (2022-2030)

plt.figure(figsize=(12, 6))

plt.title('Okosotthon piaci előrejelzés (2022-2030)')
plt.xlabel('Év')
plt.ylabel('Piaci érték (Milliárd USD)')
plt.xticks(years)
plt.legend()
plt.grid(True)

plt.show()