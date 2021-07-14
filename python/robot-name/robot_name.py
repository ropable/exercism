from datetime import datetime
import random
import string


class Robot:
    def __init__(self):
        self.name = None
        self.reset()

    def reset(self):
        random.seed(datetime.now().timestamp())
        self.name = '{}{}{}'.format(
            random.choice(string.ascii_uppercase),
            random.choice(string.ascii_uppercase),
            str(random.randint(0, 999)).zfill(3),
        )
