msc_price = 100_000
spb_price = 80_000
ekb_price = 70_000

target = input("Введи направление (msc, spb, ekb): ")

if target == "msc":
    print(f"Стоимость поездки составит {msc_price}")
elif target == "spb":
    print(f"Стоимость поездки составит {spb_price}")
elif target == "ekb":
    print(f"Стоимость поездки составит {ekb_price}")