from collections import Counter

class PersonInfo:
    def __init__(self, fi, age, *deps):
        self.fi = fi
        self.age = age
        self.deps = deps

    def short_name(self):
        # делю строку на имя и фамилию
        first_name, last_name = self.fi.split()
        # Возвраю строку в формате "Фамилия И."
        return f"{last_name} {first_name[0]}."

    def path_deps(self):
        # Возвращаю путь подразделений соединенных стрелками
        return " --> ".join(self.deps)

    def new_salary(self):
        # Объединяю все подразделения в одну строку
        all_deps = " ".join(self.deps)
        # Подсчитываю вхождения каждой буквы
        letter_counts = Counter(all_deps)
        # Нахожу три часто встречающиеся буквы
        most_common_letters = letter_counts.most_common(3)
        # Суммирую количество вхождений этих букв
        total_count = sum(count for _, count in most_common_letters)
        # Вычисляю новую зарплату
        return 1337 * self.age * total_count

