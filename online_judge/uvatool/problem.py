from .uhunt import UHunt


class Problem(object):

    def __init__(self, problem_id):

        self._id = problem_id
        self.__get_data()

    def __get_data(self):
        data = UHunt().get_problem_data(self._id)
        self.number = data['num']
        self.name = data['title']
