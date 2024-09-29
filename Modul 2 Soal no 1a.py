#Soal TA

import numpy as np
import matplotlib.pyplot as plt

R1 = 22 #cm
R2 = 17.5 #cm
n = 1.50

f1 = (n-1)*(1/R1+1/R2)
f = 1/f1
print("Jarak Fokus Lensa = ",f," cm")

# nilai R dari 1 hingga 22 cm
R1_values = np.arange(1, 22, 0.1)

# Menghitung jarak fokus f untuk setiap nilai R1
f_values = (n - 1) * (1 / R1_values + 1 / R2)
f_values = 1 / f_values  # Membalik untuk mendapatkan f

# Membuat desain grafik
plt.figure(figsize=(8, 6))
plt.plot(R1_values, f_values, label='Jarak Fokus f', color='b')

# Menambahkan label dan judul
plt.xlabel('Jari-jari kelengkungan R (cm)')
plt.ylabel('Jarak Fokus f (cm)')
plt.title('Grafik Jarak Fokus Lensa terhadap Jari-jari Kelengkungan R')
plt.grid(True)
plt.legend()

# Menampilkan grafik
plt.show()
