def create_phone_number(num_tuple):
    # Проверяем, что кортеж содержит ровно 10 цифр
    if len(num_tuple) != 10:
        raise ValueError("Кортеж должен содержать ровно 10 цифр.")

    # Форматируем номер телефона
    area_code = ''.join(map(str, num_tuple[:3]))
    first_part = ''.join(map(str, num_tuple[3:6]))
    second_part = ''.join(map(str, num_tuple[6:]))

    phone_number = f"({area_code}) {first_part}-{second_part}"
    return phone_number
