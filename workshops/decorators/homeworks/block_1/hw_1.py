# Написать простую функцию, которая на вход принимает строку ('test') и целое число (3),
# а возвращает строку вида 'testTESTtest' - исходную строку, умноженную на 3, в разном регистре.

def str_mul(some_string: str, multiplier: int):
    result = "" if multiplier != 0 else None
    for i in range(multiplier):
        result += some_string if i % 2 == 0 else some_string.upper()
    return result


if __name__ == "__main__":
    some_variable = str_mul
    print(some_variable)
