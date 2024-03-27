import tls_client
from logger import *
import threading
session = tls_client.Session(
    client_identifier="chrome_112",
    random_tls_extension_order=True
)
import ctypes
reacted = 0
failed = 0
def set_console_title():
    ctypes.windll.kernel32.SetConsoleTitleW(f'Discord Token Reactor | Reacted: {reacted} | Failed: {failed} | Proccessed: {reacted + failed} | Time Right Now: {format_current_time()}')
set_console_title()
class Reactor:
    def __init__(self, token: str, channelid: str, guildId: str, ep: str, messageid: str):
        self.token = token
        self.channelid = channelid
        self.endpoint = ep
        self.guildid = guildId
        self.messageid = messageid
        self.session = tls_client.Session(
       client_identifier="chrome_112",
       random_tls_extension_order=True
)
    def React(self):
        global reacted, failed
        headers = {
            'authority': 'discord.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'authorization': self.token,
            'origin': 'https://discord.com',
            'referer': f'https://discord.com/channels/{self.guildid}/{self.channelid}',
            'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Microsoft Edge";v="122"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0',
            'x-debug-options': 'bugReporterEnabled',
            'x-discord-locale': 'en-US',
            'x-discord-timezone': 'Europe/Budapest',
            'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyMi4wLjAuMCBTYWZhcmkvNTM3LjM2IEVkZy8xMjIuMC4wLjAiLCJicm93c2VyX3ZlcnNpb24iOiIxMjIuMC4wLjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6Imh0dHBzOi8vZGlzY29yZC5jb20vP2Rpc2NvcmR0b2tlbj1NVEEzTURReU56RXhNVGM1TVRJNE5ESTROQS5HYWNhYnIuVE9NZUVzbHdiczJ2OFRlck4wOTM3SzVvS0ZFMFZyZW5fdWF6Q1kiLCJyZWZlcnJpbmdfZG9tYWluIjoiZGlzY29yZC5jb20iLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MjcxMjE2LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==',
        }

        params = {
            'location': 'Message',
            'type': '0',
        }
        response = self.session.put(
            f'https://discord.com/api/v9/channels/{self.channelid}/messages/{self.messageid}/reactions/{self.endpoint}',
            params=params,
            headers=headers,
        )
        if response.status_code == 204:
            Sprint(self.token)
            reacted += 1
            set_console_title()
            with open('reacted.txt', 'a') as r:
                r.write(f'{self.token}\n')
            return 'success'
        else:
            Eprint(self.token)
            failed += 1
            with open('failed.txt', 'a') as f:
                f.write(f'{self.token}\n')
            set_console_title()
            return 'fail'

def worker(token, channelid, guildid, endpoint, messageid):
    reactor = Reactor(token, channelid, guildid, endpoint, messageid)
    result = reactor.React()

def main():
    with open('tokens.txt', 'r') as file:
        tokens = file.read().splitlines()
    channel_id = Inp('Enter the id of the channel where the message lies: ')
    guild_id = Inp('Enter id of the guild where the given channel lies: ')
    message_id = Inp('Enter id of the message where to react: ')
    endpoint = Inp('Enter the api endpoint ( dm response for help ): ')
    threads = []
    for token in tokens:
        thread = threading.Thread(target=worker, args=(token, channel_id, guild_id, endpoint, message_id))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
    Iprint(str(reacted+failed), str(failed), str(reacted))
    input()
