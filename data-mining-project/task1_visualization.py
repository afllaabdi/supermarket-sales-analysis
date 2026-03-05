import pandas as pd 
import matplotlib.pyplot as plt

data_transaksi = {
    "tanggal": [
        "2025-01-02", "2025-01-05", "2025-01-12", "2025-01-18", "2025-01-21",
        "2025-02-01", "2025-02-05", "2025-02-11", "2025-02-15", "2025-02-22"
    ], 
    "kategori": [
        "Bonus", "Makanan", "Transport", "Belanja", "Bonus",
        "Makanan", "Belanja", "Transport", "Lainnya", "Bonus"
    ], 
    "nominal": [
        3000000, 25000, 150000, 1200000, 500000,
        200000, 175000, 20000, 50000, 2000000
    ], 
    "metode": [
        "Transfer", "Cash", "Cash", "E-Wallet", "Transfer",
        "Cash", "Transfer", "E-Wallet", "Cash", "Transfer"
    ] 
}

df = pd.DataFrame(data_transaksi)
print("=== DataFrame Transaksi ===")
print(df) 

plt.style.use('seaborn-v0_8')

fig, ax = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("Visualisasi Data Transaksi Keuangan", fontsize=16, fontweight='bold')

ax[0,0].plot(
    df["tanggal"], 
    df["nominal"], 
    marker='o',    
    linestyle='-', 
    color="#1f77b4" 
)
ax[0,0].set_title("Line Plot: Nominal per Tanggal") 
ax[0,0].set_xlabel("Tanggal") 
ax[0,0].set_ylabel("Nominal (Rp)") 
ax[0,0].tick_params(axis='x', rotation=20) 
ax[0,0].grid(True) 


ax[0,1].scatter(
    df["kategori"], 
    df["nominal"], 
    s=120, 
    color="#ff7f0e" 
)
ax[0,1].set_title("Scatter Plot: Nominal per Kategori") 
ax[0,1].set_xlabel("Kategori")
ax[0,1].set_ylabel("Nominal (Rp)")


total_kategori = df.groupby("kategori")["nominal"].sum()
ax[1,0].bar(
    total_kategori.index, 
    total_kategori.values,
    color="#2ca02c"
)
ax[1,0].set_title("Bar Chart: Total Nominal per Kategori") 
ax[1,0].set_xlabel("Kategori")
ax[1,0].set_ylabel("Total (Rp)")
ax[1,0].grid(axis="y") 


metode_count = df["metode"].value_counts()

ax[1,1].pie(
    metode_count.values, 
    labels=metode_count.index, 
    autopct='%1.1f%%', 
    colors=["#ff9999", "#66b3ff", "#99ff99"] 
)
ax[1,1].set_title("Pie Chart: Metode Pembayaran") 


plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()