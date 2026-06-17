import pandas as pd
from google_play_scraper import app, reviews, Sort, reviews_all

# --- Data ---
APP_ID   = "com.linkit.bimatri"   # ganti dengan app ID yang diinginkan
APP_LANG = "id"
APP_COUNTRY = "id"
MAX_REVIEWS = 10000

scraped = reviews_all(
    APP_ID,
    lang=APP_LANG,
    country=APP_COUNTRY,
    sort=Sort.MOST_RELEVANT,
    count=MAX_REVIEWS
)

raw_df = pd.DataFrame(scraped)
raw_df.to_csv("ulasan_raw.csv", index=False)
