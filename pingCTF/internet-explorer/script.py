import requests
url = "https://internet-explorer.knping.pl/"
headers = {
    'Host': 'internet-explorer.knping.pl',
    'Sec-Ch-Ua': '"Chromium";v="119", "Microsoft Edge";v="24"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': "Linux",
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Linux NT 10.0; Win64; x64; Trident/7.0; AS; rv:11.0) like Gecko',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Priority': 'u=0, i'
}

response = requests.get(url=url, headers=headers)
print(response.text)