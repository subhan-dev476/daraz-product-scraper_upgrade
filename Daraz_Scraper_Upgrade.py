import requests
import logging
import csv
from datetime import datetime
import time
from urllib.parse import urljoin

logging.basicConfig(
    filename="daraz_error.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json",
    "Referer": "https://www.daraz.pk/"
}


def get_json(url):
    for i in range(3):
        try:
            r = requests.get(url, headers=HEADERS, timeout=10)
            r.raise_for_status()
            return r.json()
        except Exception as e:
            logging.error(f"Attempt {i+1} failed: {e}")
            time.sleep(2)
    return None


def clean_price(price):
    try:
        return int(price.replace("Rs.", "").replace(",", "").strip())
    except:
        return 0


def clean_rating(r):
    try:
        return round(float(r), 1)
    except:
        return 0.0

def safe_get(data, key, default=None):
    value = data.get(key)
    return value if value not in [None, ""] else default


def build_url(link):
    if not link:
        return "N/A"
    return urljoin("https:", link)


def scrape_page(page, query, seen):
    url = f"https://www.daraz.pk/catalog/?ajax=true&page={page}&q={query}"

    data = get_json(url)
    if not data:
        return []

    items = data.get("mods", {}).get("listItems", [])
    results = []

    for i in items:
        key = i.get("itemId")
        if key in seen:
            continue
        seen.add(key)

        results.append({
            "Title": i.get("name"),
            "Price": clean_price(i.get("price", "")),
            "Rating": clean_rating(i.get("ratingScore")),
            "Reviews": int(i.get("review") or 0),
            "Seller": safe_get(i, "sellerName", "Unknown"),
            "Discount": safe_get(i, "discount", "No Discount"),
            "InStock": safe_get(i, "inStock", True),
            "URL": build_url(i.get("itemUrl"))
        })

    return results


def save_csv(data, filename):
    if not data:
        return

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)


def main():
    query = input("Enter product name: ").strip()

    if not query or query.isdigit():
        print("Invalid product name")
        return

    try:
        max_pages = int(input("Enter pages: "))
    except:
        print("Invalid number")
        return

    filename = f"{query}_data_{datetime.now().strftime('%y_%m_%d')}.csv"

    all_data = []
    seen = set()

    print(f"\nScraping: {query}\n")

    for page in range(1, max_pages + 1):

        print(f"Page {page} scraping...")

        page_data = scrape_page(page, query, seen)

        if not page_data:
            print("No data, stopping...")
            break

        all_data.extend(page_data)

        print(f"Page {page} done | Total: {len(all_data)}")

        time.sleep(1)

    save_csv(all_data, filename)

    print("\nDONE")
    print("Total products:", len(all_data))
    print("Saved:", filename)


if __name__ == "__main__":
    main()