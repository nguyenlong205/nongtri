from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import re

class CommodityPrice:
    def __init__(self, commodity):
        self.commodity = commodity.lower()
        self.urls = {
            "coffee": "https://giacaphe.com/gia-ca-phe-noi-dia/",
            "ri6": "https://tanixa.com/gia-sau-rieng-hom-nay/",
            "pepper": "https://giatieu.com/gia-tieu-hom-nay/"
        }
        self.url = self.urls.get(self.commodity)
        
        options = Options()
        options.add_argument("--headless")  # Run without opening a browser
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    def retrieve(self):
        if not self.url:
            return {"Error": "Commodity not supported"}

        try:
            self.driver.get(self.url)
            self.driver.implicitly_wait(5)  # Wait for content to load

            if self.commodity == "coffee":
                return self._get_coffee_price()
            elif self.commodity == "ri6":
                return self._get_ri6_price()
            elif self.commodity == "pepper":
                return self._get_pepper_price()
            else:
                return {"Error": "Commodity not implemented"}
        finally:
            self.driver.quit()

    def _get_coffee_price(self):
        try:
            trung_binh_tag = self.driver.find_element(By.CLASS_NAME, "_trung-binh-gia")
            trung_binh_gia = trung_binh_tag.text.strip()
        except:
            trung_binh_gia = "N/A"

        try:
            thay_doi_tag = self.driver.find_element(By.CLASS_NAME, "_change.price_change")
            thay_doi_gia = thay_doi_tag.get_attribute("data-price")
        except:
            thay_doi_gia = "N/A"

        return {
            "Commodity": "Coffee",
            "Price": trung_binh_gia,
            "Change": thay_doi_gia
        }

    def _get_ri6_price(self):
        try:
            price_tag = self.driver.find_element(By.CSS_SELECTOR, "td.column-2")
            price_text = price_tag.text.strip()
            
            # Tìm tất cả các số trong chuỗi giá
            prices = re.findall(r"\d{2,3}(?:\.\d{3})*", price_text)
            prices = [int(p.replace(".", "")) for p in prices]  # Chuyển sang số nguyên
            
            avg_price = sum(prices) // len(prices) if prices else "N/A"
        except:
            avg_price = "N/A"

        return {
            "Commodity": "Durian RI6",
            "Price": avg_price
        }
    def _get_pepper_price(self):
        try:
            desc_tag = self.driver.find_element(By.CLASS_NAME, "giatieu-desc")
            price_match = re.search(r"(\d{1,3}(?:,\d{3})*) VNĐ/kg", desc_tag.text)
            price = price_match.group(1) if price_match else "N/A"
        except:
            price = "N/A"

        return {
            "Commodity": "Pepper",
            "Price": price
        }

# Chạy thử từng loại
commodities = ["coffee", "ri6", "pepper"]
for c in commodities:
    scraper = CommodityPrice(c)
    print(scraper.retrieve())
