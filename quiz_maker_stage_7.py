# === Stage 7: Генерация идентификаторов ===
# Project: QuizMaker
PREFIX = "quizmaker"


def generate_unique_id() -> str:
    counter = 0
    while True:
        candidate = f"{PREFIX}-{counter}"
        counter += 1
        if candidate not in _id_registry:
            _id_registry[candidate] = True
            return candidate


_id_registry: set[str] = set()


def validate_prefix() -> None:
    if not PREFIX or not all(c.isalnum() for c in PREFIX):
        raise ValueError("Недопустимый префикс проекта")
