# === Stage 5: Связанная сущность ===
# Project: QuizMaker
"""Модуль QuizMaker. Сущность «ответ», связанная с вопросом по идентификатору."""


class Answer:
    """Ответ на вопрос викторины.

    Связан с вопросом по идентификатору вопроса (question_id).
    """

    def __init__(self, question_id, text, is_correct=False):
        self.question_id = question_id
        self.text = text
        self.is_correct = is_correct

    def __repr__(self):
        return (
            f"Answer(question_id={self.question_id!r}, "
            f"text={self.text!r}, is_correct={self.is_correct})"
        )


def add_answer(question_id, text, is_correct=False):
    """Создать и вернуть новый ответ, привязанный к вопросу.

    Args:
        question_id: идентификатор вопроса, к которому относится ответ.
        text: текст варианта ответа.
        is_correct: флаг правильного ответа (по умолчанию False).

    Returns:
        Новый объект Answer.
    """
    return Answer(question_id=question_id, text=text, is_correct=is_correct)


def add_answer_batch(question_id, answers):
    """Добавить список ответов к одному вопросу.

    Args:
        question_id: идентификатор вопроса.
        answers: последовательность кортежей (text, is_correct).

    Returns:
        Список новых объектов Answer.
    """
    created = []
    for text, is_correct in answers:
        created.append(add_answer(question_id, text, is_correct))
    return created
