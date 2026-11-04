# === Stage 2: Проверка полей ===
# Project: QuizMaker
from typing import Any, Dict, List, Optional, Tuple

ERRORS: Dict[str, List[str]] = {}


def normalize_input(value: Any) -> Any:
    if value is None:
        return value
    if isinstance(value, str):
        return value.strip()
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        return value
    if isinstance(value, list):
        return [normalize_input(v) for v in value]
    return value


def validate_difficulty(difficulty: Any) -> Optional[str]:
    valid = {"easy", "medium", "hard"}
    normalized = normalize_input(difficulty)
    if normalized not in valid:
        return "Недопустимое значение сложности. Используйте easy, medium или hard."
    return None


def validate_points(points: Any) -> Optional[str]:
    normalized = normalize_input(points)
    try:
        if isinstance(normalized, str):
            normalized = float(normalized)
        if not isinstance(normalized, (int, float)) or isinstance(normalized, bool):
            return "Баллы должны быть числом."
        if normalized <= 0:
            return "Баллы должны быть положительным числом."
    except (ValueError, TypeError):
        return "Баллы должны быть числом."
    return None


def validate_question_fields(question: Dict[str, Any]) -> Tuple[Dict[str, Any], List[str]]:
    normalized = {k: normalize_input(v) for k, v in question.items()}

    text = normalized.get("text")
    topic = normalized.get("topic")
    difficulty = normalized.get("difficulty")
    points = normalized.get("points")

    if not isinstance(text, str) or text == "":
        ERRORS["text"] = "Текст вопроса не может быть пустым."
    else:
        ERRORS["text"] = []

    if not isinstance(topic, str) or topic == "":
        ERRORS["topic"] = "Тема вопроса не может быть пустой."
    else:
        ERRORS["topic"] = []

    difficulty_error = validate_difficulty(difficulty)
    if difficulty_error:
        ERRORS["difficulty"] = difficulty_error
    else:
        normalized["difficulty"] = difficulty_error

    points_error = validate_points(points)
    if points_error:
        ERRORS["points"] = points_error
    else:
        normalized["points"] = points_error

    return normalized, list(ERRORS.values())
