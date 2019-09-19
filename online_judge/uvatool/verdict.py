from datetime import datetime

from .problem import Problem
from .utils import verdicts, languages


class Verdict(object):

    def __init__(self, sub):
        self.submission_id = sub[0]
        self.problem = Problem(sub[1])
        self.verdict_message = self.__get_veredit_message(sub[2])
        self.runtime = self.__get_runtime(sub[3], sub[2])
        self.date = self.__get_date(sub[4])
        self.language = self.__get_language(sub[5])
        self.rank = sub[6]

    def __get_veredit_message(self, verdict_id):
        return verdicts.get(verdict_id, "Unknown verdict")

    def __get_runtime(self, runtime_mili, verdict_id):
        if verdict_id not in verdicts.keys():
            return -1
        return runtime_mili / 1000.0

    def __get_date(self, timestamp):
        date = datetime.fromtimestamp(timestamp)
        return date.strftime('%Y-%m-%d %H:%M:%S')

    def __get_language(self, language_id):
        return languages.get(language_id, "Unknown language")

    def __str__(self):
        data_str = '\n'
        data_str += f"Submission ID: {self.submission_id}\n"
        data_str += f"Problem: {self.problem.number} - {self.problem.name}\n"
        data_str += f"Verdict: {self.verdict_message}\n"

        if self.runtime == -1:
            data_str += f"Run Time: -\n"
        else:
            data_str += f"Run Time: {self.runtime:.3f}s\n"

        data_str += f"Submission Date: {self.date}\n"
        data_str += f"Language: {self.language}\n"
        data_str += f"Rank: {self.rank}\n"

        return data_str
