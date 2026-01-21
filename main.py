msc_price = 100_000
spb_price = 80_000
ekb_price = 70_000

target = input("Введи направление (msc, spb, ekb): ")
count = int(input("Сколько будет людей: "))

if target == "msc":
    target_price = msc_price
elif target == "spb":
    target_price = spb_price
elif target == "ekb":
    target_price = ekb_price

print(f"Стоимость поездки составит {count * target_price}. Приятного путешествия!")