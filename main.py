temp = int(input("Какая на улице температура?: "))
rain = input("На улице идет дождь? Да\Нет: ")
r = False
if rain == "да" or rain == "Да":
    r = True

if temp <= 5 and r:
    print(f"На улице {temp}°С, холодно и дождливо, одевайся теплее!!!")
elif temp <= 5 and not r:
    print(f"На улице {temp}°С, холодно, одевайся теплее!!!")
elif temp > 5 and temp <= 18 and r:
    print(f"На улице {temp}°С, тепло, но не забудь зонт")
elif temp > 5 and temp <= 18 and not r:
    print(f"На улице {temp}°С, тепло, но не забудь зонт")
elif temp > 18 and r:
    print(f"На улице {temp}°С, жарко, но не забудь зонт")
else:
    print(f"На улице {temp}°С , жарко")