import base64
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
        anki_correct = 'wrong'
        if self.img_uri is not None:
            img = img_uri_embed(self.img_uri)
        if self.correct:
            anki_correct = 'correct'
        return [self.txt, img, anki_correct]


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

    def ankinum(self) -> str:
        return f'{self.question_set.name}{self.question_num}'

    def ankiformat(self) -> [str]:
        img = ''
        if self.question_uri is not None:
            img = img_uri_embed(self.question_uri)

        return [self.question_txt, img, self.ankinum()] + self.ans_a.ankiformat() + self.ans_b.ankiformat() + self.ans_c.ankiformat()

    def ankitag(self) -> str:
        return str(self.question_set.name)
