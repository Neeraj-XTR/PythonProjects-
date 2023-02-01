def vi():
    yield "Do you want to Shut down the computer sir"
    yield "In how much time do you want to shut down the computer, Please Answer in seconds as the unit of time"


def ti(time):
    yield "Shutting down the computer in T minus {} seconds".format(time)
