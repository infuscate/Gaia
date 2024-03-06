import json, requests, time, random

config = open('config.json')
config = json.load(config)

class Gaia:
    def __init__(self):
        # Config vars
        self.token      = config['token']
        self.recipients = config['recipients']
        self.names      = config['names']
        self.delay      = config['delay']

        # Request vars
        self.url        = "https://discord.com/api/v9/users/@me/channels"
        self.url2       = "https://discord.com/api/v9/channels/"
        self.headers    = {"Authorization": self.token}
        self.json       = {"recipients":["1159399315647758347","833223691365122048"]}

        # Groupchat vars
        self.count      = 0
        self.ratelimted = 0
        self.total      = 0
        self.retry      = 0

    def current(self):
        current = f"COMPLETED - {self.count: ^5}| LIMITED - {self.ratelimted: ^5}| TOTAL - {self.total: ^5}|"
        print(f"\r{current}", end="")
    
    def start(self):
        while True:
            req = requests.post(url=self.url, headers=self.headers, json=self.json)
            gdata = req.json()
            if req.status_code == 429:
                self.ratelimted += 1
                self.retry = float(gdata['retry_after'])
            elif req.status_code == 200:
                if self.names != []:
                    name = random.choice(self.names)
                    req2 = requests.patch(url=self.url2 + gdata['id'], headers=self.headers, json={"name": name})
                if req.status_code == 200: self.count += 1
                else: print(req.status_code)
                self.total += 1
                self.retry = 0
            else:
                print("error")
                continue
            self.current()

            if self.retry > 0: time.sleep(self.retry)
            else: time.sleep(self.delay)

Gaia().start()