import sys
from uvatool.uva import UVA

if len(sys.argv) < 2:
    exit()

uva = UVA()

cmd = sys.argv[1]

if cmd == "login":
    if len(sys.argv) < 4:
        exit()
    uva.login(sys.argv[2], sys.argv[3], True)

elif cmd == "logout":
    if len(sys.argv) > 3:
        print("Invalid number of arguments.")
        exit()

    if len(sys.argv) < 3:
        uva.logout()
    else:
        uva.logout(sys.argv[2])

elif cmd == "submit":
    if len(sys.argv) < 5:
        exit()
    problem_number = int(sys.argv[2])
    language_id = int(sys.argv[3])
    filename = sys.argv[4]
    sid = uva.submit(problem_number, language_id, filename)

    print(f"Submission ID: {sid}")

elif cmd == "check_submission":
    if len(sys.argv) < 4:
        exit()
    username = sys.argv[2]
    sid = int(sys.argv[3])
    print(uva.check_verdict(username, sid))

else:
    print("Command invalid.")
