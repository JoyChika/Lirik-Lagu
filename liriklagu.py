import time
import sys

#Warna terminal
MERAH = "\033[91m"
HIJAU = "\033[92m"
BIRU = "\033[94m"
RESET = "\033[0m"

#Lirik 
lirik = [
    "Ku tak bisa jauh darimu",
    "Walau kini kau bukan milikmu",
    "Tiap malam ku selalu rindu",
    "Kini hanya bayanganmu yang tersisa..."
]

waktu_jeda = 2

print(f"{BIRU}Memulai lagu dalam 3 detik...{RESET}")

for i in range(3, 0, -1):
    print(f"{HIJAU}{i}...{RESET}")
    time.sleep(1)


time.sleep(3)
print("\n======= LIRIK LAGU MULAI =======\n")

for baris in lirik:
    for huruf in baris:
        sys.stdout.write(huruf)
        sys.stdout.flush()
        time.sleep(0.05)
    print()  
    time.sleep(waktu_jeda)

print(f"\n{MERAH}lagu selesai! Tertimakasih sudah menonton jangan lupa like{RESET}")
