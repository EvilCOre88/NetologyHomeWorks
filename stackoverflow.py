import requests
from pprint import pprint


class StackQuestion:
    def questions(self, url, params):
        results = {}
        response = requests.get(url=url, params=params).json()
        for item in response['items']:
            results[item['title']] = item['link']
        return results


if __name__ == '__main__':
    params = {
        'site': 'stackoverflow',
        'fromdate': '2022-06-03',
        'order': 'desc',
        'sort': 'activity',
        'tagged': 'Python',
        'filter': 'default'
    }
    url = 'https://api.stackexchange.com/2.3/questions'
    sq = StackQuestion().questions(url, params)
    pprint(sq)
