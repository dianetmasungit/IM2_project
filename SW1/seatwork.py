def currency_converter(dollars):
    peso_rate = 57.17
    yen_rate = 146.67

    peso = dollars * peso_rate
    yen = dollars * yen_rate

    return peso ,yen

dollars = float(input("Enter dollars: "))
peso , yen = currency_converter(dollars)

print("\nDollars($)\tPhil Peso(P)\tJpn Yen(Y)")
print(f"{dollars}\t\t{peso:.2f}\t\t{yen:.2f}")