# === Stage 8: Фильтрация записей ===
# Project: QuizMaker
import datetime


def filter_by_topic(questions, topic):
    if not topic:
        return list(questions)
    return [q for q in questions if q.get("тема") == topic]


def filter_by_date_range(questions, start=None, end=None):
    results = []
    for q in questions:
        date_field = q.get("дата") or q.get("дата_создания")
        if not date_field:
            continue
        value = date_field[:10] if isinstance(date_field, str) else date_field.date()
        try:
            date_obj = datetime.datetime.strptime(value, "%Y-%m-%d").date()
        except (ValueError, TypeError):
            continue
        if start and date_obj < start:
            continue
        if end and date_obj > end:
            continue
        results.append(q)
    return results


def filter_questions(questions, topic=None, start=None, end=None):
    result = filter_by_topic(questions, topic)
    result = filter_by_date_range(result, start, end)
    return result


if __name__ == "__main__":
    sample = [
        {"текст": "Вопрос 1", "тема": "Наука", "сложность": 2, "баллы": 10, "дата": "2024-01-15"},
        {"текст": "Вопрос 2", "тема": "История", "сложность": 3, "баллы": 15, "дата": "2024-02-20"},
        {"текст": "Вопрос 3", "тема": "Наука", "сложность": 1, "баллы": 5, "дата": "2023-12-05"},
    ]
    print(filter_questions(sample, topic="Наука"))
    print(filter_questions(sample, start=datetime.date(2024, 1, 1)))
