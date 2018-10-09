kotely = """˓˓ฅ₍˄ุ.͡ ̫.˄ุ₎ฅ˒˒\n"""
print(kotely)

owcaUzytkownik = input("Podaj ile kotelow chcesz generowac ")
try:    
    owcaUzytkownik = int(owcaUzytkownik)
except ValueError as owcaError:
    owcaUzytkownik = 1
    print("Program potrzebuje liczby")

print (kotely * owcaUzytkownik)