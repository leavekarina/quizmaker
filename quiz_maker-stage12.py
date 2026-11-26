# === Stage 12: Группировка ===
# Project: QuizMaker
def group_by_topic(questions):
    groups = {}
    for question in questions:
        topic = question.get('topic') or question.get('тема')
        groups.setdefault(topic, []).append(question)
    return groups


def count_by_topic(questions):
    return {topic: len(qs) for topic, qs in group_by_topic(questions).items()}


def summary(questions):
    counts = count_by_topic(questions)
    total = sum(counts.values())
    return {
        'by_topic': counts,
        'total': total,
    }


def report(questions):
    summary_ = summary(questions)
    lines = ['Отчёт по темам викторины']
    for topic, count in summary_['by_topic'].items():
        lines.append(f'{topic}: {count}')
    lines.append(f'Всего вопросов: {summary_["total"]}')
    return '\n'.join(lines)
