import requests
from bs4 import BeautifulSoup

class craig:
    def __init__(self, query: str = None, listing_range: int = None):
        self._url = f"https://philadelphia.craigslist.org/search/cta?query={query}"
        self.listing_range = listing_range

    def listing_info(self):
        response = requests.get(self._url)
        soup = BeautifulSoup(response.text, 'html.parser')
        listing = soup.find_all("li", {"class":"result-row"})
        
        if self.listing_range >= len(listing):
            raise ValueError("Requested range was larger than number of listings!")
        
        else:
            info_list = []
            for listed in listing[:self.listing_range]:
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

    

cat = craig("tesla", 300)

# print(cat.listing_info())

with open("output.txt", "w") as f:
    for i in cat.listing_info():
        f.write(str(i) + "\n")
    f.close()