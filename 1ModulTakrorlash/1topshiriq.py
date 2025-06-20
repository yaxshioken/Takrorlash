# #1. Foydalanuvchining ism va familiyasini qabul qiladigan
# # va ularni teskari tartibda ular orasida bo'sh joy qoldirib chop etadigan
# # Python dasturini yozing.
# Ism = str(input("Ismingizni kiriting = > "))
# Familiya = str(input("Familiyangizni kiriting = > "))
# print(Familiya + " " + Ism)


# #2. Kun boshlangandan keyin (00:00) N sekund o’tdi, yani N sekundni kiritamiz.
# #Kun boshlangandan keyin nechinchi soatda o’tganligini aniqlang
#
# Sekund = int(input("Sekundni kiriting -> "))
# Soat = Sekund/3600
# print(f"Soat: {Soat:.2f}")


# # 3. Kun boshlangandan keyin (00:00) N sekund o’tdi, yani N sekundni kiritamiz.
# # Kun boshlangandan keyin nechinchi mi	nutda ekanligini aniqlang.
# Sekund = int(input("Sekundni kiriting -> "))
# Minut = Sekund/60
# print(f"Minut: {Minut:.2f}")

#4. Kun boshlangandan keyin (00:00) N sekund o’tdi, yani N sekundni kiritamiz.
#Nechinchi soatda, munit va sekund o’tganini aniqlang.
Sekund = int(input("Sekundni kiriting -> "))
Soat = Sekund//3600
Minut = Sekund//60
Sekund=Sekund-Soat*3600-Minut*60
print(f"Soat: {Soat:.2f}")
print(f"Minut: {Minut:.2f}")




