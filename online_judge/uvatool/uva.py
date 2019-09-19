import os
import re
import pickle
from lxml.html import fromstring

from online_judge import OnlineJudge
from .utils import ActionMethod, languages
from .uhunt import UHunt
from .verdict import Verdict

HOME_URL = lambda: 'http://uva.onlinejudge.org/'
SESSIONS_DIR = lambda: 'data/sessions'
SUBMIT_URL = lambda: 'https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=25&page=save_submission'


class UVA(OnlineJudge):

    def __init__(self):
        super().__init__()

        self.sessions_path = f'{self.sessions_path}/uva'
        self.home_url = 'http://uva.onlinejudge.org/'
        self.submit_url = 'https://onlinejudge.org/index.php' \
            '?option=com_onlinejudge&Itemid=25&page=save_submission'

    def login(self, username, password, remember=False, force=False):

        if not self.__validate_username(username):
            print("Invalid username.")
            return False

        if force:
            self.__make_login(self.home_url, username, password, remember)
        else:
            if self.__load_session(username):
                if not self.__check_login(self.home_url):
                    self.__make_login(self.home_url, username, password, remember)
            else:
                self.__make_login(self.home_url, username, password, remember)

    def logout(self, username=None):

        if username is None:
            if not self.__logout("active_user"):
                print("Failed to logout active user")
            else:
                print("")

        else:
            if not self.__validate_username(username):
                print("Invalid username.")
                return

            if not self.__logout(username):
                print(f"Failed to logout user {username}.")
                return
            else:
                print(f"")

            if not self.__logout("active_user"):
                print("Failed to logout active user.")
            else:
                print(f"")

    def submit(self, problem_number, language_id, filename):

        if not self.__load_session("active_user"):
            print("User is not logged in.")
            return None

        data = {}
        data['localid'] = problem_number

        if language_id not in languages.keys():
            print("Language ID invalid.")
            return None
        data['language'] = language_id

        # data['codeupl'] = '/home/pabolo/Dropbox/maratona/uva/submit/uva-11057.cpp'

        code = ''
        with open(filename, 'r') as file:
            code = ''.join(file.readlines())
        data['code'] = code

        resp = self.session.post(self.submit_url, data, verify=False)
        regex = r'mosmsg=Submission\+received\+with\+ID\+(\d+)'
        sid = re.findall(regex, resp.text)
        return sid[0]

    def check_verdict(self, username, submission_id):
        sub = UHunt(username).get_submission_result(submission_id)
        return Verdict(sub)

    def __validate_username(self, username):
        if username == '':
            return False
        regex = r'[<>\"\'\%\;\(\)&\+\- ]'
        return re.findall(regex, username) == []

    def __make_login(self, url, username, password, remember):
        tree = self.__get_html_tree(url)
        forms_list = tree.cssselect('#mod_loginform')
        if forms_list == []:
            return False

        form = forms_list[0]
        url = form.get('action')
        params = self.__get_params(form)
        params['username'] = username
        params['passwd'] = password

        tree = self.__get_html_tree(url, action=ActionMethod.POST, params=params)
        if not self.__check_login(self.home_url, tree):
            print("Failed")
            return False

        if remember:
            self.__save_session(username)
        return True

    def __logout(self, username):
        if not os.path.isfile(f'{self.sessions_path}/{username}'):
            return True

        os.remove(f'{self.sessions_path}/{username}')
        return os.path.isfile(f'{self.sessions_path}/{username}')

    def __get_html_tree(self, url, action=ActionMethod.GET, params=None):
        request = None
        if action == ActionMethod.GET:
            request = self.session.get(url, verify=False)
        elif action == ActionMethod.POST:
            request = self.session.post(url, params, verify=False)
        else:
            print('Invalid action method')
            return None

        html = request.text
        tree = fromstring(html)
        return tree

    def __get_params(self, form):
        params = {}
        inputs = form.cssselect('input')
        for i in inputs:
            name = i.get('name')
            value = i.get('value')
            if name:
                params[name] = value if value else ''
        return params

    def __check_login(self, url, tree=None):
        if tree is None:
            tree = self.__get_html_tree(url, action=ActionMethod.GET)

        return tree.cssselect("#mod_loginform") == []

    def __save_session(self, username):
        if not os.path.exists(self.sessions_path):
            os.makedirs(self.sessions_path)
        with open(f'{self.sessions_path}/{username}', 'wb') as file:
            pickle.dump(self.session.cookies, file)

        with open(f'{self.sessions_path}/active_user', 'wb') as file:
            pickle.dump(self.session.cookies, file)

    def __load_session(self, username):
        if not os.path.isfile(f'{self.sessions_path}/{username}'):
            return False

        with open(f'{self.sessions_path}/{username}', 'rb') as file:
            self.session.cookies.update(pickle.load(file))

        return True
