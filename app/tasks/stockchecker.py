import requests

from app.utils.ItemStatusChangeNotifier import ItemStatusChangeNotifier
from app.utils.itemstatustracker import ItemStatusTracker


class StockCheckTask:
    def __init__(self, pincode: str, sku: str):
        self.url = "https://api.bhawar.com/edt/api/get-edt.php"
        self.params = {
            "pincode": pincode,
            "sku": sku
        }
        self.headers = {
            "accept": "application/json",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
            "content-type": "application/json",
            "origin": "https://casiostore.bhawar.com",
            "priority": "u=1, i",
            "referer": "https://casiostore.bhawar.com/",
            "sec-ch-ua": '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"macOS"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
        }
        self.sku = sku

    def execute(self):
        in_stock = False
        try:
            response = requests.get(self.url, headers=self.headers, params=self.params, timeout=5)
            if response.status_code == 200:
                in_stock = True
        except requests.RequestException:
            print("❌ Request failed")
        if ItemStatusTracker.is_status_changed(ItemStatusTracker.CASIO_SKU, self.sku, str(in_stock)):
            print("There is a change in the status")
            ItemStatusChangeNotifier().notify("The stock status of {0} {1} is {2}".format(ItemStatusTracker.CASIO_SKU, self.sku, in_stock))
            ItemStatusTracker.add_item_status(ItemStatusTracker.CASIO_SKU, self.sku, str(in_stock))
        print("sku", self.sku, in_stock)
