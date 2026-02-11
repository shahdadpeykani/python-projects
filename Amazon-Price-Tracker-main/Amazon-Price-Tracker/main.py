from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv

# ___________________________________________GETTING THE PRICE FROM AMAZON WEBSITE____________________________________#
load_dotenv()
URL = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-GB,de;q=0.8,fr;q=0.6,en;q=0.4,ja;q=0.2",
    "Dnt": "1",
    "Priority": "u=1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Sec-Gpc": "1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0",
}

response = requests.get(URL, headers=header)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

price = soup.find(name="span", class_="a-offscreen").getText()
price = price[1:]

title = soup.find(name="span", class_="a-size-large product-title-word-break").getText()
cleaned_title = ' '.join(title.split())

# ---------------------------------------------------------SENDING EMAIL PROCESS-------------------------------------#
if float(price) < 90:
    message = f"{title} is on sale for {price}!"

    with smtplib.SMTP(os.environ["SMTP-ADDRESS"], port=587) as connection:
        connection.starttls()
        result = connection.login(os.environ["MY_EMAIL"], os.environ["PASSWORD"])
        connection.sendmail(
            from_addr=os.environ["MY_EMAIL"],
            to_addrs="brianpaykani@yahoo.com",
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}".encode("utf-8")
        )
