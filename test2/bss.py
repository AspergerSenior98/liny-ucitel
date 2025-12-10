from bs4 import BeautifulSoup 
import requests
import json

ingredience_cesnecka = [
    "česnek",
    "voda",
    "kmín",
    "sůl",
    "houba",
    "libeček",
    "pivo",
    "krutony",
    "cizrna",
    "mariánka",
    "pepř"
]



def main():

    url = "https://souhrada.github.io/bsoup-exam/"
    response = requests.get(url)
    
    # BeautifulSoup(response.content, "html.parser") <--- Úkol: popiš krátce, co tohle dělá
    # vrátí stránku jako html přes který pak můžeme vyzobávat co chcem
    pushToJson = [

    ]
    soup = BeautifulSoup(response.content, "html.parser")
    ingredience = soup.select(".stuff")
    for element in ingredience:
        text = element.getText()
        if text in ingredience_cesnecka:
            print(text)
            pushToJson.append(text)
    with open("recept.json", "w") as f:
        json.dump(pushToJson, f, indent=4)

        
if __name__ == "__main__":
    main()