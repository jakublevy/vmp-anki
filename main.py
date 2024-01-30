from lxml import html
import requests
from requests.models import Response
from lxml.html import HtmlElement
import genanki

import html_css_constants
from question import Answer, Question

M_QUESTIONS_URI = 'http://www.spspraha.cz/zkousky/otazky.asp?zp=M%202015'
S_QUESTIONS_URI = 'http://www.spspraha.cz/zkousky/otazky.asp?zp=S%202015'
C_QUESTIONS_URI = 'http://www.spspraha.cz/zkousky/otazky.asp?zp=C'

MODEL_ID = 1167192610
DECK_ID = 7548399843


def main():
    questions: [Question] = parse()
    create_anki_pkg(questions)


def parse() -> [Question]:
    questions = []
    for uri in [M_QUESTIONS_URI, S_QUESTIONS_URI, C_QUESTIONS_URI]:
        qset = question_set(uri)
        page: Response = requests.get(uri)
        tree: HtmlElement = html.fromstring(page.content)

        questions_numbers: [HtmlElement] = tree.xpath('//tr[@class = "bg"]/td/span[not(child::i)]')
        question_row: [HtmlElement] = tree.xpath('//tr[@class = "bg"]/following-sibling::tr[1]')
        a_answer_row: [HtmlElement] = tree.xpath('//tr[@class = "bg"]/following-sibling::tr[3]')
        b_answer_row: [HtmlElement] = tree.xpath('//tr[@class = "bg"]/following-sibling::tr[4]')
        c_answer_row: [HtmlElement] = tree.xpath('//tr[@class = "bg"]/following-sibling::tr[5]')

        assert len(questions_numbers) == len(question_row) == len(a_answer_row) == len(b_answer_row) == len(c_answer_row), "The page has changed, parsing needs fixing"
        questions_count = len(questions_numbers)

        for i in range(questions_count):
            question = question_row[i].findall('td')
            question_uri = None
            question_txt = question[0].text if question[0].text is not None else ''
            if len(question) == 2:
                img = question[1].find('img')
                question_uri = img.attrib['src']
            elif len(question) > 2 or len(question) < 1:
                raise ValueError('Parsing needs fixing')

            ans_a: Answer = parse_answer_row(a_answer_row[i])
            ans_b: Answer = parse_answer_row(b_answer_row[i])
            ans_c: Answer = parse_answer_row(c_answer_row[i])
            q: Question = Question(question_txt, question_uri, ans_a, ans_b, ans_c, qset, int(questions_numbers[i].text))
            questions.append(q)
    return questions


def parse_answer_row(answer_row: HtmlElement) -> Answer:
    ans_title = answer_row.find('th')
    ans_data = answer_row.findall('td')
    correct = True if 'Správná odpověď' in ans_title.text else False
    ans_img_uri = None
    ans_text = ans_data[0].text if ans_data[0].text is not None else ''
    if len(ans_data) == 2:
        img = ans_data[1].find('img')
        ans_img_uri = img.attrib['src']
    elif len(ans_data) > 2 or len(ans_data) < 1:
        raise ValueError('Parsing needs fixing')
    return Answer(ans_text, ans_img_uri, correct)


def question_set(uri: str) -> Question.Set:
    if uri == C_QUESTIONS_URI:
        return Question.Set.C
    elif uri == M_QUESTIONS_URI:
        return Question.Set.M
    elif uri == S_QUESTIONS_URI:
        return Question.Set.S
    raise ValueError('Invalid question URI')


def create_anki_pkg(questions: [Question]):
    vmp_model = genanki.Model(MODEL_ID, name='vmp',
        fields=[
            {'name': 'question'},
            {'name': 'question_img'},
            {'name': 'question_num'},
            {'name': 'a'},
            {'name': 'a_img'},
            {'name': 'b'},
            {'name': 'b_img'},
            {'name': 'c'},
            {'name': 'c_img'},
            {'name': 'correct'}
        ],
        templates=[{
            'name': 'Card 1',
            'qfmt': html_css_constants.front_template,
            'afmt': html_css_constants.back_template
        }],
        css=html_css_constants.styling,
        sort_field_index=2
    )
    deck = genanki.Deck(
        DECK_ID,
        'VMP – Vůdce malého plavidla'
    )

    for question in questions:
        vmp_note = genanki.Note(
            model=vmp_model,
            fields=question.ankiformat(),
            tags=[question.ankitag()]
        )
        deck.add_note(vmp_note)

    genanki.Package(deck).write_to_file('vmp_deck.apkg')


if __name__ == '__main__':
    main()
