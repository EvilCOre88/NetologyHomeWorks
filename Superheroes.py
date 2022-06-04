import requests


class Superheroes:
    def __init__(self):
        with open('token.txt', 'r') as token_file:
            self.token = token_file.read().strip()

    def superhero(self, name):
        url = f'https://superheroapi.com/api/{self.token}/search/{name}'
        res = requests.get(url)
        return res

    def superheroes_intelligence(self, names_of_superheroes):
        superheroes_intelligence = {}
        for name in names_of_superheroes:
            superheroes_intelligence[name] = self.superhero(name).json()['results'][0]['powerstats']['intelligence']
        return superheroes_intelligence

    def highest_intelligence(self):
        highest_int = max([int(i) for i in list(self.superheroes_intelligence(name_of_superheroes).values())])
        for name, intelligence in self.superheroes_intelligence(name_of_superheroes).items():
            if int(intelligence) == highest_int:
                return f'Самый высокий интелект - {highest_int} у персонажа: {name}'


if __name__ == '__main__':
    name_of_superheroes = ['Hulk', 'Captain America', 'Thanos']
    superheroes = Superheroes()
    superheroes.superheroes_intelligence(name_of_superheroes)
    highest_intelligence = superheroes.highest_intelligence()
    print(highest_intelligence)
