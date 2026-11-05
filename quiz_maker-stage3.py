# === Stage 3: Хранилище в памяти ===
# Project: QuizMaker
memory_store.py

from typing import Any, Dict, List, Optional


class Entity:
    def __init__(self, entity_id: str, name: str):
        self.entity_id = entity_id
        self.name = name

    def __repr__(self):
        return f"{self.__class__.__name__}(id={self.entity_id}, name={self.name})"


class Question:
    def __init__(self, question_id: str, text: str, topic: str, difficulty: str, points: int):
        self.question_id = question_id
        self.text = text
        self.topic = topic
        self.difficulty = difficulty
        self.points = points

    def __repr__(self):
        return (
            f"Question(id={self.question_id}, text={self.text!r}, topic={self.topic!r}, "
            f"difficulty={self.difficulty!r}, points={self.points})"
        )


class Answer:
    def __init__(self, answer_id: str, question_id: str, is_correct: bool, text: str):
        self.answer_id = answer_id
        self.question_id = question_id
        self.is_correct = is_correct
        self.text = text

    def __repr__(self):
        return (
            f"Answer(id={self.answer_id}, question_id={self.question_id!r}, "
            f"is_correct={self.is_correct}, text={self.text!r})"
        )


class Round:
    def __init__(self, round_id: str, name: str, questions: List[Question]):
        self.round_id = round_id
        self.name = name
        self.questions = questions

    def __repr__(self):
        return f"Round(id={self.round_id}, name={self.name!r}, questions_count={len(self.questions)})"


class QuizResult:
    def __init__(self, result_id: str, round_id: str, score: int, total: int):
        self.result_id = result_id
        self.round_id = round_id
        self.score = score
        self.total = total

    def __repr__(self):
        return f"QuizResult(id={self.result_id}, round_id={self.round_id!r}, score={self.score}/{self.total})"


class MemoryStore:
    def __init__(self):
        self._questions: Dict[str, Question] = {}
        self._answers: Dict[str, Answer] = {}
        self._rounds: Dict[str, Round] = {}
        self._results: Dict[str, QuizResult] = {}
        self._counter = 0

    def _next_id(self, prefix: str) -> str:
        self._counter += 1
        return f"{prefix}_{self._counter}"

    def add_question(self, text: str, topic: str, difficulty: str, points: int) -> Question:
        question_id = self._next_id("q")
        question = Question(question_id, text, topic, difficulty, points)
        self._questions[question_id] = question
        return question

    def get_question(self, question_id: str) -> Optional[Question]:
        return self
