# === Stage 1: Каркас модуля ===
# Project: QuizMaker
quizmaker_questions.py

from dataclasses import dataclass, field
from typing import List


@dataclass
class Question:
    """Сущность «вопрос» для конструктора викторин QuizMaker."""
    text: str
    topic: str
    difficulty: str
    points: int
    variants: List[str] = field(default_factory=list)


def create_demo_questions() -> List[Question]:
    """Формирует набор демонстрационных вопросов для теста каркаса."""
    return [
        Question(
            text="Столица Франции?",
            topic="География",
            difficulty="easy",
            points=10,
            variants=["Париж", "Лyon", "Марсель", "Нант"],
        ),
        Question(
            text="Кто написал 'Войну и мир'?",
            topic="Литература",
            difficulty="easy",
            points=10,
            variants=["Достоевский", "Толстой", "Чехов", "Пушкин"],
        ),
        Question(
            text="Сколько планет в Солнечной системе?",
            topic="Астрономия",
            difficulty="medium",
            points=20,
            variants=["7", "8", "9", "10"],
        ),
    ]


def main() -> None:
    """Выводит краткую информацию о сгенерированных демонстрационных вопросах."""
    questions = create_demo_questions()
    print("QuizMaker — Конструктор викторин")
    print("Сгенерировано демонстрационных вопросов:", len(questions))
    for index, question in enumerate(questions, start=1):
        print(f"  {index}. [{question.topic}] {question.text} "
              f"(сложность: {question.difficulty}, баллы: {question.points})")


if __name__ == "__main__":
    main()
