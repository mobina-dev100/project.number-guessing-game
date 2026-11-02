import random

def play():
    s, n = random.randint(1, 100), 5
    print(f"\nعددی بین 1 تا 100 حدس بزن! {n} فرصت داری.\n")
    for i in range(1, n + 1):
        print(f"تلاش {i} از {n} | جان باقی‌مانده: {n - i + 1}")
        while True:
            try:
                g = int(input("حدس: "))
                if 1 <= g <= 100: break
                print("بین 1 تا 100 وارد کن!")
            except ValueError:
                print("فقط عدد وارد کن!")
        if g == s:
            r = {1:"نمونه‌ای", 2:"بسیار خوبی", 3:"خوب", 4:"قبول", 5:"با شانس بردی"}
            print(f"بردی! عدد {s} بود. رتبه: {r[i]}\n")
            return
        d = abs(g - s)
        m = "خیلی نزدیکی!" if d <= 5 else "نزدیکی!" if d <= 15 else "خیلی دوری!"
        print(f"{'بزرگ‌تر' if g < s else 'کوچک‌تر'} | {m}\n")
    print(f"باختی! عدد مخفی {s} بود.\n")

while True:
    play()
    if input("دوباره؟ (y/n): ").lower() != "y":
        break