from time import sleep


class cloock:
    def __init__(self, h, m, s):
        self._h = h
        self._m = m
        self._s = s

    def run(self):
        self._s += 1
        if self._s == 60:
            self._s = 0
            self._m += 1
            if self._m == 60:
                self._m = 0
                self._h += 1
                if self._h == 24:
                    self._h = 0

    def show(self):
        print('%02d:%02d:%02d' % (self._h, self._m, self._s))


def main():
    clocks = cloock(23, 59, 59)
    while True:
        clocks.show()
        clocks.run()
        sleep(1)


if __name__ == '__main__':
    main()
