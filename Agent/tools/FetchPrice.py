import requests
from bs4 import BeautifulSoup

def FETCH_PRODUCT_DETAILS(url: str):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    response = requests.get(url, headers=headers, timeout=15)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    # ---------- Product Name ----------
    title_tag = soup.find("h1")
    product_name = title_tag.get_text(strip=True) if title_tag else None

    # ---------- Prices ----------
    current_price = None
    original_price = None

    # Current price
    current_price = None
    price_div = soup.select_one("div.normal-price.green p span")
    if price_div:
        current_price = price_div.text.strip()

    # Striked price
    strike_tag = soup.find("del")
    if strike_tag:
        original_price = strike_tag.get_text(strip=True).replace("$", "")

    return {
        "product_name": product_name,
        "current_price": current_price,
        "original_price": original_price
    }

if __name__ == "__main__":
    url = "http://localhost:8000/bjs-webcam.html"
    result = fetch_product_details(url)
    print(result)
