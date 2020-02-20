import requests
import rumps

class StatusBarAppBitcoin(rumps.App):
    def __init__(self):
        super(StatusBarAppBitcoin,self).__init__("Price Bitcoin EUR")
        self.menu = ["Searching..."]

    @rumps.timer(60)
    def toShow(self, _):
        head = {
            'Content-type': 'applicacion/json',
        }

        r = requests.get("https://api.coinbase.com/v2/exchange-rates?currency=BTC")
        print(r.json()['data']['rates']['EUR'])
        self.title = r.json()['data']['rates']['EUR']

if __name__ == "__main__":
    StatusBarAppBitcoin().run()