import matplotlib.pyplot as plt
import numpy as np

# Gegevens
problemen = ['Voeding', 'Moederbord', 'Hotend', 'Cooling Fan', 'CR Touch Sensor', 'Mechanisch', 'Overig', 'Anders']
frequenties = [50, 30, 20, 15, 10, 8, 7, 3]

# Cumulatieve frequentie en percentage berekenen
cumulatieve_frequenties = np.cumsum(frequenties)
total = sum(frequenties)
percentages = [freq / total * 100 for freq in frequenties]
cumulatieve_percentages = np.cumsum(percentages)

# Balkdiagram
fig, ax1 = plt.subplots()

ax1.bar(problemen, frequenties, color='C0')
ax1.set_xlabel('Problemen')
ax1.set_ylabel('Frequentie', color='C0')
ax1.tick_params(axis='y', labelcolor='C0')

# Lijndiagram
ax2 = ax1.twinx()
ax2.plot(problemen, cumulatieve_percentages, color='C1', marker='o', ms=5)
ax2.set_ylabel('Cumulatief Percentage', color='C1')
ax2.tick_params(axis='y', labelcolor='C1')

plt.title('Pareto-analyse van Creality Ender 3 V2 Problemen')
plt.show()
