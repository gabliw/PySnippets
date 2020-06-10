import time


class ProgressBar(object):

    def __init__(self, end, length=40):
        self.end = end
        self.length = length
        self.present = time.time()

    def progress(self, value):
        percent = float(value) / self.end
        arrow = ''.join(['-' * int(round(percent * self.length) - 1), '>'])
        space = '.' * (self.length - len(arrow))
        return f'[{"".join([arrow, space])}] {int(round(percent * 100))}'

    def eta(self, value):
        duration = time.time() - self.present
        left = duration * (self.end - value)
        self.present = time.time()
        return left

    def display(self, value):
        print(f'\r{self.progress(value)}% - eta: <= {self.eta(value):.3f} s', end='')


iteration = 100
pb = ProgressBar(iteration)

for i in range(iteration):
    pb.display(i + 1)  # because of zero index
    time.sleep(0.1)
