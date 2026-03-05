import numpy as np
import matplotlib.pyplot as plt

hari = np.array(["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"])
suhu_kotaA = np.array([29, 30, 28, 31, 32, 33, 30])
suhu_kotaB = np.array([27, 29, 26, 28, 30, 31, 29])
suhu_kotaC = np.array([25, 26, 28, 29, 31, 32, 30]) 

rata_rata_kotaA = suhu_kotaA.mean()
rata_rata_kotaB = suhu_kotaB.mean()
rata_rata_kotaC = suhu_kotaC.mean()

print(f"Rata-rata suhu Kota A: {rata_rata_kotaA:.2f}°C")
print(f"Rata-rata suhu Kota B: {rata_rata_kotaB:.2f}°C")
print(f"Rata-rata suhu Kota C: {rata_rata_kotaC:.2f}°C")

plt.figure(figsize=(8, 6))
plt.plot(hari, suhu_kotaA, label="Kota A", color='orange', marker='o', linestyle='--')
plt.plot(hari, suhu_kotaB, label="Kota B", color='skyblue', marker='s', linestyle='--')
plt.plot(hari, suhu_kotaC, label="Kota C", color='green', marker='^', linestyle='-')  

plt.axhline(y=rata_rata_kotaA, color='orange', linestyle='-', linewidth=1.5, label=f"Rata-rata Kota A ({rata_rata_kotaA:.2f}°C)")
plt.axhline(y=rata_rata_kotaB, color='skyblue', linestyle='-', linewidth=1.5, label=f"Rata-rata Kota B ({rata_rata_kotaB:.2f}°C)")
plt.axhline(y=rata_rata_kotaC, color='green', linestyle='-', linewidth=1.5, label=f"Rata-rata Kota C ({rata_rata_kotaC:.2f}°C)")

plt.title("Perbandingan Suhu Rata-Rata Kota A, Kota B, dan Kota C")
plt.xlabel("Hari")
plt.ylabel("Suhu (°C)")
plt.legend()
plt.grid(True)
plt.show()
