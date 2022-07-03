import requests
from bs4 import BeautifulSoup

class craig:
    def __init__(self):
        pass

    def _get_listing_info(self, listing, listing_range):
        info_list = []
        for listed in listing[:listing_range]:
            listing_name = listed.find("a", {"class":"result-title hdrlnk"}).text.strip()
            listing_price = listed.find("span", {"class":"result-price"}).text.strip()
            listing_date = listed.find("time", {"class":"result-date"}).get("datetime")
            listing_link = listed.find("a", {"class":"result-title hdrlnk"}).get("href")

            item = {
                "link": listing_link,
                "name": listing_name,
                "price": listing_price,
                "date": listing_date,
            }
            
            info_list.append(item)
        
        return info_list

    def search(self, query: str = "", listing_range: int = 5):
        url = f"https://philadelphia.craigslist.org/search/cta?query={query}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        listing = soup.find_all("li", {"class":"result-row"})
        
        if listing_range >= len(listing):
            raise ValueError("Requested range was larger than number of listings!")
        
        else:
            return self._get_listing_info(listing, listing_range)


    

cat = craig()

# print(cat.search("tesla"))

with open("output.txt", "w") as f:
    for i in cat.search("tesla", 10):
        f.write(str(i) + "\n")
    f.close()