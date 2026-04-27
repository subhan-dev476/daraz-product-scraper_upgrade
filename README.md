# daraz-product-scraper_upgrade
Python web scraper that extracts product data (price, rating, reviews, seller, discount) from Daraz API and saves it into CSV file.



# 🛒 Daraz Product Scraper (Python)

A Python-based web scraper that extracts product data from Daraz using its public catalog API and saves it into a structured CSV file.

This project is built for learning web scraping, API handling, and data cleaning using real-world e-commerce data.

---

## 🚀 What this project does

This scraper collects product information from Daraz search results and stores it locally.

It extracts:

- Product Title
- Price (cleaned and converted)
- Rating (rounded and normalized)
- Number of Reviews
- Seller Name
- Discount (if available)
- Stock Status (if available)
- Product URL

---

## ⚙️ How it works

1. User enters a product name (example: mobile, laptop)
2. Script sends request to Daraz catalog API
3. JSON response is parsed
4. Data is cleaned and structured
5. Duplicate products are removed
6. Data is saved into CSV file
7. Pagination runs automatically until limit is reached

---

## 🛠 Tech Stack

- Python 3
- Requests library
- CSV module
- Logging module
- Daraz public JSON API

---

## 📂 Project Structure
daraz-product-scraper/
│
├── scraper.py
├── daraz_error.log
├── data_output.csv
└── README.md



---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/daraz-product-scraper.git
cd daraz-product-scraper


Install required library:

pip install requests


▶️ How to Run

Run the script:

python scraper.py

Then enter:

Product name: mobile
Pages to scrape: 10

Output file will be generated automatically:

mobile_data_26_04_12.csv


📊 Features
API based scraping (faster than browser scraping)
Automatic pagination
Duplicate removal system
Error logging system
Clean CSV export
Safe request retry system
Handles missing data gracefully
⚠️ Limitations
Some fields like rating or seller may be missing depending on product
Daraz API structure can change anytime
Rate limiting may block requests if used aggressively
🧠 What I learned

This project helped me understand:

Real-world API scraping
JSON parsing
Data cleaning techniques
Error handling in Python
Pagination logic
Building structured automation scripts
🔮 Future Improvements
Save data into database (SQLite / MySQL)
Add price tracker system
Build GUI version
Add notifications for price drops
Export to Excel with formatting
👨‍💻 Author

Built by Muhammad Subhan

📌 Note

This project is for educational purposes only.
