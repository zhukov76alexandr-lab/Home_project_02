msc_price = 100_000
spb_price = 80_000
ekb_price = 70_000
kaz_price = 70_000

target = input("Введи направление (msc, spb, ekb, kaz): ")

if target == "msc":
    target_price = msc_price
elif target == "spb":
    target_price = spb_price
elif target == "ekb":
    target_price = ekb_price
elif target == "kaz":
    target_price = kaz_price

print(f"Стоимость поездки составит {target_price}. Приятного путешествия!")