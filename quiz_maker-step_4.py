# === Stage 4: Редактирование записей ===
# Project: QuizMaker
from dataclasses import dataclass, field
from typing import Any


@dataclass
class Question:
    id: str
    text: str
    topic: str
    difficulty: str
    points: int
    meta: dict = field(default_factory=dict)

    ALLOWED_FIELDS = (
        "text",
        "topic",
        "difficulty",
        "points",
    )

    VALID_DIFFICULTIES = ("easy", "medium", "hard")

    def __post_init__(self):
        if self.difficulty not in self.VALID_DIFFICULTIES:
            raise ValueError(
                f"Недопустимая сложность: {self.difficulty}. "
                f"Допустимы: {self.VALID_DIFFICULTIES}"
            )
        if self.points < 0:
            raise ValueError("Баллы не могут быть отрицательными")

    def patch(self, changes: dict) -> "Question":
        unknown = set(changes) - set(self.ALLOWED_FIELDS)
        if unknown:
            raise ValueError(f"Недопустимые поля: {sorted(unknown)}")

        new_text = changes.get("text", self.text)
        new_topic = changes.get("topic", self.topic)
        new_difficulty = changes.get("difficulty", self.difficulty)
        new_points = changes.get("points", self.points)

        if new_difficulty not in self.VALID_DIFFICULTIES:
            raise ValueError(
                f"Недопустимая сложность: {new_difficulty}. "
                f"Допустимы: {self.VALID_DIFFICULTIES}"
            )
        if new_points < 0:
            raise ValueError("Баллы не могут быть отрицательными")

        return Question(
            id=self.id,
            text=new_text,
            topic=new_topic,
            difficulty=new_difficulty,
            points=new_points,
            meta=self.meta,
        )


def edit_question(question: Question, changes: dict) -> Question:
    if not isinstance(changes, dict):
        raise TypeError("Изменения должны быть представлены в виде словаря")

    if question.id not in changes:
        raise ValueError("ID вопроса должен присутствовать в изменениях")

    return question.patch(changes)


def load_question_changes(data: dict) -> dict:
    if not isinstance(data, dict):
        raise TypeError("Данные для редактирования должны быть словарём")

    question_id = data.get("id")
    if not question_id:
        raise ValueError("Отсутствует идентификатор вопроса")

    return {"id": question_id}
