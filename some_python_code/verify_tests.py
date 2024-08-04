class Verify:

    def __init__(self, right_answers, answers, test_name=""):
        self.right_answers = right_answers
        self.answers = answers
        self.test_name = test_name

    @classmethod
    def verify_dict(cls, dict_answers):
        for value in dict_answers.values():
            if not isinstance(value, str):
                raise TypeError('The list of answers is invalid')

    def verify_answers(self, r_ans: dict, ans: dict):
        count = 0
        for key, right_ans in r_ans.items():
            if ans.get(key) == right_ans:
                count += 1
        return count

    def __str__(self):
        total_q = len(self.right_answers)
        cor_answers = self.verify_answers(self.right_answers, self.answers)
        return f'The result of {self.test_name} is {cor_answers}/{total_q}'


class Test1(Verify):
    def __init__(self, right_answers, answers, test_name=""):
        super().__init__(right_answers, answers, test_name)
        self.verify_answers(self.right_answers, self.answers)

    def verify_answers(self, r_ans: dict, ans: dict):
        EX_10 = {'iteration', 'Iteration', 'ITERATION'}
        count = super().verify_answers(r_ans, ans)
        if ans.get('10 ex') in EX_10:
            count += 1
        return count


class Test2(Verify):
    def __init__(self, right_answers, answers, test_name=""):
        super().__init__(right_answers, answers, test_name)
        self.verify_answers(self.right_answers, self.answers)

    def verify_answers(self, r_ans: dict, ans: dict):
        EX_11 = {'left', 'Left', "LEFT"}
        count = super().verify_answers(r_ans, ans)
        if ans.get('11 ex') in EX_11:
            count += 1
        return count


r_answers = {
    '1 ex': 'a',
    '2 ex': 'a',
    '3 ex': 'c',
    '4 ex': 'b',
    '5 ex': 'd',
    '6 ex': 'a',
    '7 ex': 'c',
    '8 ex': 'b',
    '9 ex': 'b',
    '10 ex': 'a'
}
r1_answers = {
    '1 ex': 'a',
    '2 ex': 'a',
    '3 ex': 'c',
    '4 ex': 'b',
    '5 ex': 'd',
    '6 ex': 'a',
    '7 ex': 'c',
    '8 ex': 'b',
    '9 ex': 'b',
    '10 ex': 'iteration'
}
r2_answers = {
    '1 ex': 'd',
    '2 ex': 'c',
    '3 ex': 'a',
    '4 ex': 'b',
    '5 ex': 'd',
    '6 ex': 'b',
    '7 ex': 'c',
    '8 ex': 'a',
    '9 ex': 'a',
    '10 ex': 'c',
    '11 ex': 'left'
}
s3_answers = {
    '1 ex': 'b',
    '2 ex': 'a',
    '3 ex': 'd',
    '4 ex': 'c',
    '5 ex': 'd',
    '6 ex': 'a',
    '7 ex': 'c',
    '8 ex': 'b',
    '9 ex': 'd',
    '10 ex': 'Iteration'
}
s1_answers = {
    '1 ex': 'b',
    '2 ex': 'a',
    '3 ex': 'd',
    '4 ex': 'b',
    '5 ex': 'd',
    '6 ex': 'a',
    '7 ex': 'c',
    '8 ex': 'b',
    '9 ex': 'a',
    '10 ex': 'a'
}
s2_answers = {
    '1 ex': 'b',
    '2 ex': 'a',
    '3 ex': 'd',
    '4 ex': 'c',
    '5 ex': 'd',
    '6 ex': 'a',
    '7 ex': 'c',
    '8 ex': 'b',
    '9 ex': 'd',
    '10 ex': 'iteration'
}

s1 = Verify(right_answers=r_answers, answers=s1_answers, test_name='Alice Smith')
s2 = Verify(right_answers=r_answers, answers=s2_answers, test_name='George Soul')
s3 = Test1(r1_answers, s3_answers, 'Claus Wrong')
print(s1)
print(s2)
print(s3)
