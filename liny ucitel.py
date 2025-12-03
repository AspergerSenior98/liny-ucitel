import json
import random

with open("data.json") as f:
    d = json.load(f)

pocetstudentu = 20
for x in range(1, pocetstudentu):
    znamka = random.randint(1, 5)
    
    jmeno = input("Komu udělím známku "+ str(znamka)+"\n")
    if jmeno == "Souhrada":
        prepsat = input("No... tomuhle ti nechám udělit známku sám \n")
        while prepsat != "5":
            prepsat = input("Error: tato známka nejde uživateli připsat \n")
        prepsat = int(prepsat)
        if jmeno in d:
            d[jmeno].append(prepsat)
        else:
            d[jmeno] = [prepsat]
    elif jmeno in d:
        prepsat = input("Uživatel už známku má. Připsat další? A/N \n")
        if prepsat == "A":
            d[jmeno].append(znamka)
            total = 0
            for znamka in d[jmeno]:
                total+=znamka
            p = total/len(d[jmeno])
            print("Průměr studenta:")

            print(p)
            if p > 4.2:
                print(":(")
        elif prepsat != "N":
            print("ERROR: detekovaná obecná hloupost")
    else:
        d[jmeno] = [znamka]
    with open("data.json", "w") as f:
        print(d)
        json.dump(d, f)
