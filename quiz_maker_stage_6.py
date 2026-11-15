# === Stage 6: Связи между сущностями ===
# Project: QuizMaker
import sqlite3
from typing import List, Dict, Any, Optional


class QuestionIntegrityError(Exception):
    """Ошибка проверки целостности связи вопросов и ответов."""


def get_answers_for_question(
    question_id: int,
    db_path: str = "quizmaker.db",
) -> List[Dict[str, Any]]:
    """Получить все ответы для заданного вопроса."""
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    try:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, text, is_correct FROM answers WHERE question_id = ?",
            (question_id,),
        )
        rows = cursor.fetchall()
        return [dict(row) for row in rows]
    finally:
        conn.close()


def check_question_answer_integrity(
    question_id: int,
    db_path: str = "quizmaker.db",
) -> bool:
    """
    Проверить целостность связи «вопрос» — «ответ».

    Возвращает True, если для вопроса существуют ответы и их больше одного.
    """
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    try:
        cursor = conn.cursor()

        cursor.execute(
            "SELECT id FROM questions WHERE id = ?",
            (question_id,),
        )
        if not cursor.fetchone():
            raise QuestionIntegrityError(
                f"Вопрос с id={question_id} не существует"
            )

        cursor.execute(
            "SELECT COUNT(*) AS count FROM answers WHERE question_id = ?",
            (question_id,),
        )
        answer_count = cursor.fetchone()["count"]

        if answer_count < 2:
            raise QuestionIntegrityError(
                f"У вопроса с id={question_id} меньше двух ответов"
            )

        return True
    finally:
        conn.close()


def validate_question_with_answers(
    question: Dict[str, Any],
    db_path: str = "quizmaker.db",
) -> bool:
    """
    Валидировать вопрос: существование в БД и целостность связей с ответами.
    """
    question_id = question.get("id")
    if not question_id:
        raise QuestionIntegrityError("Вопрос не имеет идентификатора")

    if not check_question_answer_integrity(question_id, db_path):
        return False

    answers = get_answers_for_question(question_id, db_path)
    correct_answers = [a for a in answers if a.get("is_correct")]

    if not correct_answers:
        raise QuestionIntegrityError(
            f"Среди ответов вопроса с id={question_id} нет правильного"
        )

    return True
