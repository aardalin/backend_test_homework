from typing import Callable

# Callable[[<тип аргумента 1>, <тип аргумента 2>,...], <возвращаемый тип>]

def printer() -> None:
    print("Вызови меня!")


def returner(word: str) -> str:
    return word


def app(printed_inside: Callable[[], None], returned_inside: Callable[[str], str]) -> None:
    printed_inside()
    print(returned_inside('Нет, вызови меня!'))


# При таком вызове всё будет ok:
app(printer, returner)