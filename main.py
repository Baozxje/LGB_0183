#sum a b
def sum(a,b):
    total = a + b
    signal = a - b
    return total, signal
a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))

total, signal = sum(a,b)
print("Tổng của a và b là: ", total)
print("Hiệu của a và b là: ", signal)