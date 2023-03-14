# ID решения 83952088
import operator


def data_input():
    example = list(input().split())
    return example


def calculation(example):
    stack = []
    OPERATORS = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.floordiv
        }
    for operand in example:
        if operand in OPERATORS:
            stack.append(
                OPERATORS[operand](int(stack.pop(-2)), int(stack.pop()))
                )
        else:
            stack.append(int(operand))
    return stack.pop()


def main():
    example = data_input()
    print(example)
    print(calculation(example))


if __name__ == '__main__':
    main()
