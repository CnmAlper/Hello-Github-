# you can use github website on this code.
import requests
import json

class Github:
    def __init__(self):
        self.api_url = 'https://api.github.com'
        self.token = 'your_token'

    def getUser(self, username):
        response = requests.get(self.api_url+'/users/'+username)
        return response.json()

    def getRepositories(self, username):
        response = requests.get(self.api_url+'/repos/'+ username)
        return response.json()
    
    def createRepository(self, name):
        response = requests.post(self.api_url+'/user/repos?access_token='+ self.token, json={
            "name": name,
            "description": "This is your first repository",
            "homepage": "https://github.com",
            "private": False,
            "has_issues": True,
            "has_projects": True,
            "has_wiki": True
        })
        return response



github = Github()



while True:
    secim = input('1- Find User\n2- Get Repositories\n3- Create Repository\n4- Exit\nSecim: ')

    if secim == '4':
        break
    else:
        if secim == '1':
            username = input('UserName: ')
            result = github.getUser(username)
            print(f"name: {result['name']}, public repos: {result['public_repos']} followers : {result['followers']}")
        elif secim == '2':
            username = input('UserName: ')
            result = github.getRepositories(username)
            for repo in result:
                print(repo['name'])
        elif secim == '3':
            name = input('Repository Name: ')
            result = github.createRepository(name)
            print(result)
        else:
            print('You had wrong choice.')
            
# NOTE =} API; Application Programming Interface: API is a set of programming code that enables data transmission between one software product and another. It also contains the terms of this data exchange.
# CNMALPS




