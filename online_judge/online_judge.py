import urllib3
import requests
import os

class OnlineJudge(object):

    def __init__(self):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.session = requests.session()
        self.username = ''
        self.password = ''
        self.remember = False

        home_path = os.getenv('HOME')
        self.sessions_path = f'{home_path}/.cache/online_judge_tool/sessions'
        self.home_url = ''
        self.submit_url = ''

    def login(self, username, password, remember=False, force=False):
        pass

    def logout(self, username=None):
        pass

    def submit(self, problem_number, language_id, filename):
        pass

    def check_verdict(self, username, submission_id):
        pass
