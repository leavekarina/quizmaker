# === Stage 9: Сортировка записей ===
# Project: QuizMaker
import datetime


def sort_questions_by_text(records, ascending=True):
    key_fn = lambda record: record.get("text", "")
    return sorted(records, key=key_fn, reverse=not ascending)


def sort_questions_by_created_at(records, ascending=True):
    key_fn = lambda record: record.get("created_at", datetime.datetime.min)
    return sorted(records, key=key_fn, reverse=not ascending)


def sort_records(records, field, ascending=True):
    key_fn = lambda record: record.get(field, "")
    return sorted(records, key=key_fn, reverse=not ascending)


def get_created_at_timestamp(record):
    if "created_at" in record and record["created_at"]:
        created_at = record["created_at"]
        if isinstance(created_at, str):
            return datetime.datetime.fromisoformat(created_at)
        if isinstance(created_at, datetime.datetime):
            return created_at
    return datetime.datetime.min
