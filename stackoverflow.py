import requests
from pprint import pprint


class StackQuestion:
    def questions(self, url, params):
        results = {}
        res = requests.get(url=url, params=params).json()
        for item in res['items']:
            results[item['title']] = item['link']
        return results


if __name__ == '__main__':
    params = {
        'site': 'stackoverflow',
        'fromdate': '2022-06-02',
        'todate': '2022-06-05',
        'order': 'desc',
        'sort': 'activity',
        'tagged': 'Python',
        'filter': 'default'
    }
    url = 'https://api.stackexchange.com/2.3/questions#fromdate=2022-06-02&todate=2022-06-05&order=desc&sort=activity&tagged=Python&filter=default&site=stackoverflow'
    pprint(StackQuestion.questions(StackQuestion, url, params))