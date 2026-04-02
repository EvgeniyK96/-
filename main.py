temp = int(input("Какая на улице температура?: "))
if temp <= 5:
    print(f"На улице {temp}°С, холодно")
elif temp > 5 and temp <= 18:
    print(f"На улице {temp}°С, тепло!!!")
else:
    print(f"На улице {temp}°С , жарко")