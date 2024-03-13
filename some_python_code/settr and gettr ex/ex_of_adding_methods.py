class Clock:
    __DAY = 86400

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise ValueError('Seconds must be a integer')

        self.seconds = seconds % self.__DAY

    @classmethod
    def __get_formatted(cls, x):
        return str(x).rjust(2, '0')

    def get_time(self):
        s = self.seconds % 60
        m = (self.seconds // 60) % 60
        h = (self.seconds // 3600) % 24
        return f'{self.__get_formatted(h)}:{self.__get_formatted(m)}:{self.__get_formatted(s)}'

    @classmethod
    def __verify_data(cls, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError('the right operand must be a integer or class instance of Clock')

        if isinstance(other, int):
            return other
        else:
            return other.seconds

    def __add__(self, other):
        return Clock(self.seconds + self.__verify_data(other))

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        self.seconds += self.__verify_data(other)
        return self

    def __sub__(self, other):
        return Clock(self.seconds - self.__verify_data(other))

    def __rsub__(self, other):
        return self - other

    def __isub__(self, other):
        self.seconds -= self.__verify_data(other)
        return self

    def __mul__(self, other):
        return Clock(self.seconds * self.__verify_data(other))

    def __rmul__(self, other):
        return self * other

    def __imul__(self, other):
        self.seconds += self.__verify_data(other)
        return self

    def __eq__(self, other):
        return self.seconds == self.__verify_data(other)

    def __ne__(self, other):
        return self.seconds != self.__verify_data(other)

    def __lt__(self, other):
        return self.seconds < self.__verify_data(other)

    def __gt__(self, other):
        return self.seconds > self.__verify_data(other)

    def __le__(self, other):
        return self.seconds <= self.__verify_data(other)

    def __ge__(self, other):
        return self.seconds >= self.__verify_data(other)


c1 = Clock(1000)
c2 = Clock(2000)
c3 = c1 + 100
c4 = c1 + c2
c5 = 100 + c4
c6 = Clock(0)
c6 += 120
c7 = 2 * c1
c8 = c1 * c2
c9 = 2 * c1
c10 = Clock(1200)
c10 *= 2
print(c3.get_time())
print(c4.get_time())
print(c5.get_time())
print(c6.get_time())
print(c7.get_time())
print(c8.get_time())
print(c9.get_time())
print(c10.get_time())
print(c1 == 1000)
print(c2 < c1)
print(c1 != c2)
print(c8 > c1)
print(c1 >= 100)
