#homework1
numbers = [4, 5, 10, 20, 40, 60, 80]
new_list = []

for num in numbers:
    if num > 10:
        new_list.append(num) 

print(new_list)

#homework2
def area_of_circle(r):
    area = 22/7 * r ** 2
    return area

radius = float(input("Enter the radius of the circle: "))
area = area_of_circle(radius)

print(f"The area of the circle with radius {radius} is {area}")

#homework3
a = int(input("Enter A: "))
b = int(input("Enter B: "))

def perform_operations(a, b):
    addition = a + b
    multiplication = a * b
    highest = max(a, b)
    return addition, multiplication, highest

addition, multiplication, highest = perform_operations(a, b)

print(f"The addition of {a} and {b} is: {addition}")
print(f"The multiplication of {a} and {b} is: {multiplication}")
print(f"The highest number between {a} and {b} is: {highest}")

#homework4
def kasir():
    daftar_barang = {
        "Baju": 50000,
        "Celana": 70000,
        "Sepatu": 150000,
        "Topi": 30000,
        "Tas": 100000
    }
    nama_pelanggan = input("Masukkan nama pelanggan: ")
    
    total_item = 0
    total_harga = 0
    
    print("\nDaftar Barang yang Tersedia:")
    for item, harga in daftar_barang.items():
        print(f"{item}: Rp{harga}")
    
    while True:
        item_pilihan = input("\nMasukkan nama barang yang ingin dibeli (ketik 'selesai' untuk selesai): ").capitalize()
        
        if item_pilihan.lower() == 'selesai':
            break
        
        if item_pilihan in daftar_barang:
            jumlah = int(input(f"Berapa banyak {item_pilihan} yang ingin dibeli? "))
            total_item += jumlah
            total_harga += daftar_barang[item_pilihan] * jumlah
        else:
            print("Barang tidak tersedia. Silakan pilih barang yang ada dalam daftar.")
    
    print(f"\nNama Pelanggan: {nama_pelanggan}")
    print(f"Jumlah Item: {total_item} item")
    print(f"Total Harga: Rp{total_harga}")
    
kasir()
