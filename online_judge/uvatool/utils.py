from enum import Enum

languages = {
    1: "ANSI C",
    2: "Java",
    3: "C++",
    4: "Pascal",
    5: "C++11",
    6: "Python3",
}

verdicts = {
    10: "Submission error",
    15: "Can't be judged",
    20: "In queue",
    30: "Compile error",
    35: "Restricted function",
    40: "Runtime error",
    45: "Output limit",
    50: "Time limit",
    60: "Memory limit",
    70: "Wrong answer",
    80: "Presentation Error",
    90: "Accepted",
}


class ActionMethod(Enum):
    GET = 0
    POST = 1
    