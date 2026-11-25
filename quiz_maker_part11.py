# === Stage 11: Теги ===
# Project: QuizMaker
from typing import List, Dict, Optional


class QuizTag:
    def __init__(self, tag: str):
        self.tag = tag

    def __eq__(self, other):
        return isinstance(other, QuizTag) and self.tag == other.tag

    def __hash__(self):
        return hash(self.tag)

    def __str__(self):
        return self.tag


class QuestionTagManager:
    def __init__(self):
        self._tags: List[QuizTag] = []

    def add_tag(self, tag: str) -> QuizTag:
        normalized = tag.strip().lower()
        if not normalized:
            raise ValueError("Тег не может быть пустым")
        for existing in self._tags:
            if existing.tag == normalized:
                return existing
        new_tag = QuizTag(normalized)
        self._tags.append(new_tag)
        return new_tag

    def remove_tag(self, tag: str) -> bool:
        normalized = tag.strip().lower()
        for index, existing in enumerate(self._tags):
            if existing.tag == normalized:
                del self._tags[index]
                return True
        return False

    def search_by_tag(self, tag: str) -> List[QuestionTagManager]:
        normalized = tag.strip().lower()
        result = []
        for existing in self._tags:
            if normalized in existing.tag:
                result.append(existing)
        return result

    def get_tags(self) -> List[QuizTag]:
        return list(self._tags)
