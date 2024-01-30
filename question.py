import base64
import itertools
import random
from enum import Enum
import requests


def img_uri_embed(uri: str) -> str:
    img_data = requests.get(uri).content
    img = f'<img src="data:image/png;base64,{base64.b64encode(img_data).decode('utf-8')}" />'
    return img


class Answer:
    def __init__(self, txt: str, img_uri: str, correct: bool):
        self.txt = txt
        self.img_uri = img_uri
        self.correct = correct

    @property
    def is_correct(self) -> bool:
        return self.correct

    def ankiformat(self) -> [str]:
        img = ''
        if self.img_uri is not None:
            img = img_uri_embed(self.img_uri)
        return [self.txt, img]


class Question:
    class Set(Enum):
        M = 0,
        S = 1,
        C = 2

    def __init__(self, question_txt: str, question_uri: str, ans_a: Answer, ans_b: Answer, ans_c: Answer, question_set: Set, question_num: int):
        if sum([ans_a.is_correct, ans_b.is_correct, ans_c.is_correct]) != 1:
            raise ValueError('Exactly one answer must be correct')
        self.question_txt = question_txt
        self.question_uri = question_uri
        self.ans_a = ans_a
        self.ans_b = ans_b
        self.ans_c = ans_c
        self.question_set = question_set
        self.question_num = question_num

    def random_shuffle_answers(self):
        answers = [self.ans_a, self.ans_b, self.ans_c]
        random.shuffle(answers)
        self.ans_a = answers[0]
        self.ans_b = answers[1]
        self.ans_c = answers[2]

    @property
    def answers(self):
        return [self.ans_a, self.ans_b, self.ans_c]

    def ankinum(self) -> str:
        return f'{self.question_set.name}{self.question_num}'

    def ankiformat(self) -> [str]:
        img = ''
        if self.question_uri is not None:
            img = img_uri_embed(self.question_uri)

        self.random_shuffle_answers()
        ans: [[str]] = [self.ans_a.ankiformat(), self.ans_b.ankiformat(), self.ans_c.ankiformat()]
        correct_idx: int = 0
        for i in range(len(self.answers)):
            if self.answers[i].is_correct:
                correct_idx = i
                break

        return [self.question_txt, img, self.ankinum()] + list(itertools.chain(*ans)) + [str(correct_idx)]

    def ankitag(self) -> str:
        return str(self.question_set.name)
