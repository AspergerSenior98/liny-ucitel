from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import requests
import json



def main():
    requests = 4
    url = "https://www.kinoaero.cz/"

    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")
    articles = soup.find_all("div", {"class": "program__movie-name"})
    prices = soup.find_all("span", {"class" : "program__ticket"})
    for i in range(requests-1):
        movieName = articles[i].text
        price = str(prices[i].text)
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            page.goto("https://www.imdb.com/?ref_=fn_nv_home")
            page.fill('input[id="suggestion-search"]', movieName)
            page.click('button#suggestion-search-button')
            exactMatches = page.get_by_text("Exact matches")
            rating = "Film Nenalezen na IMDB"
            if exactMatches.count() > 0:
                exactMatches.click()
                page.locator(".ipc-title__text", has_text=movieName).click()
                rating = page.locator('.lbQcRY').first.inner_text()
            print(price)
            with open("peaky.json", "r+") as f:
                data = json.load(f)
                data[movieName] = {"Hodnoceni" : rating, "Cena" : price}
                f.seek(0)
                json.dump(data, f, indent=4)
                f.truncate()
    input("Dej cokoliv pro zavření prohlížeče")

    browser.close()
    
main()