import os

import requests
from django.contrib.sites.models import Site


class Unauthorized(Exception):
    pass


class Bitgo:
    def __init__(self, token=os.environ.get('BITGO_TOKEN')):
        self.api_url = "https://app.bitgo.com/api/v2"
        self.token = token

    def _send_api_request(self, method, url, json={}):
        r = requests.request(
            url=f'{self.api_url}{url}',
            method=method,
            json=json,
            headers={f'Authorization': f'Bearer {self.token}',
                     'Content-Type': 'application/json'})

        if str(r.status_code).startswith('2'):
            return r
        else:
            if r.json()['name'] == 'Unauthorized':
                raise Unauthorized(r.json()['error'])

    def get_wallet(self, coin='btc', id=os.environ.get('WALLET_ID')):
        return self.Wallet(coin, id, self)

    class Wallet:
        def __init__(self, coin, id, bitgo):
            self.coin = coin
            self.id = id
            self.bitgo = bitgo

            webhooks = self.list_wallet_webhook()
            if len(webhooks) == 0: self.add_wallet_webhook()

        def create_address(self):
            address_data = self.bitgo._send_api_request("POST", f"/{self.coin}/wallet/{self.id}/address").json()
            return self.Address(address_data['id'], address_data['address'], 0, self.bitgo, self)

        def get_address(self, address):
            address_data = self.bitgo._send_api_request("GET",
                                                        f"/{self.coin}/wallet/{self.id}/address/{address}").json()
            return self.Address(address_data['id'], address_data['address'], address_data['dalance']['balance'],
                                self.bitgo, self)

        def adresses(self):
            adresses = self.bitgo._send_api_request("GET", f"/{self.coin}/wallet/{self.id}/addresses").json()
            return [self.Address(address_data['id'], address_data['address'], address_data['dalance']['balance'],
                                 self.bitgo, self) for address_data in adresses['addresses']]

        def add_wallet_webhook(self):
            return self.bitgo._send_api_request("POST", f"/{self.coin}/wallet/{self.id}/webhooks",
                                                json={"type": "transaction",
                                                      "url": f"{Site.objects.get()}/payment/bitcoin/webhook"}).json()

        def list_wallet_webhook(self):
            return self.bitgo._send_api_request("GET", f"/{self.coin}/wallet/{self.id}/webhooks").json()['webhooks']

        class Address:
            def __init__(self, id, address, balance, bitgo, wallet):
                self.id = id
                self.adress = address
                self.balance = balance
                self.bitgo = bitgo
                self.wallet = wallet
