import json
import requests


class UHunt(object):

    def __init__(self, uname=None):
        if uname is not None:
            self.username = uname
            self.uid = self.__get_user_id()

    def get_submission_result(self, submission_id):
        url = f'https://uhunt.onlinejudge.org/api/subs-user/{self.uid}/{submission_id-1}'
        resp = requests.get(url)
        data = json.loads(resp.text)
        submission = []
        for sub in data['subs']:
            if sub[0] == submission_id:
                submission = sub
        return submission

    def get_problem_data(self, problem_id):
        url = f'https://uhunt.onlinejudge.org/api/p/id/{problem_id}'
        resp = requests.get(url)
        data = json.loads(resp.text)
        return data

    def __get_user_id(self):
        url = f'https://uhunt.onlinejudge.org/api/uname2uid/{self.username}'
        uid = requests.get(url).text
        return int(uid)
