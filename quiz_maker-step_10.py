# === Stage 10: Поиск по нескольким словам ===
# Project: QuizMaker
def find_questions(questions, keywords, exclude=None):
    exclude = exclude or []
    exclude_set = set()
    for item in exclude:
        exclude_set.update(item.lower().split())
    results = []
    for question in questions:
        text = question.get("text", "").lower()
        topic = question.get("topic", "").lower()
        combined = text + " " + topic
        match = True
        for keyword in keywords:
            key = keyword.lower()
            if key not in combined:
                match = False
                break
        if match:
            for excluded in exclude_set:
                if excluded and excluded not in combined:
                    match = False
                    break
        if match:
            results.append(question)
    return results


def parse_keywords(keywords):
    tokens = []
    for keyword in keywords:
        keyword = keyword.strip()
        if not keyword:
            continue
        if keyword.startswith("-"):
            tokens.append("-" + keyword[1:].strip())
        else:
            tokens.append(keyword)
    return tokens


def filter_keywords(keywords):
    return [keyword for keyword in parse_keywords(keywords) if keyword]


def search_questions(questions, keywords):
    filtered = filter_keywords(keywords)
    return find_questions(questions, filtered)


if __name__ == "__main__":
    sample = [
        {"text": "Столица Франции", "topic": "География", "difficulty": "easy", "points": 10},
        {"text": "Париж - столица Франции", "topic": "География", "difficulty": "easy", "points": 10},
        {"text": "История Великой Отечественной войны", "topic": "История", "difficulty": "hard", "points": 20},
    ]
    print(search_questions(sample, ["франция", "география"]))
    print(search_questions(sample, ["франция", "-география"]))
    print(search_questions(sample, ["война", "история"]))
