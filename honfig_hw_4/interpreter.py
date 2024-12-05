import struct
import csv

def interpreter(input_binary, output_csv, memory_range):
    memory = [0] * 1024  # Простая память
    stack = []

    with open(input_binary, 'rb') as binary_file:
        while chunk := binary_file.read(4):
            instruction = struct.unpack(">I", chunk)[0]
            a = (instruction >> 25) & 0x7
            b = instruction & 0x1FFFFFF

            # Обработка команд
            if a == 0:  # Загрузка константы
                stack.append(b)
            elif a == 1:  # Операция сложения
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(op1 + op2)
            elif a == 2:  # Операция вычитания
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(op1 - op2)
            elif a == 3:  # Операция умножения
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(op1 * op2)
            elif a == 4:  # Операция побитового "И"
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(op1 & op2)
            elif a == 5:  # Операция взятия остатка
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(op1 % op2)
            elif a == 6:  # Запись в память
                addr = b
                value = stack.pop()
                memory[addr] = value
            elif a == 7:  # Чтение из памяти
                addr = b
                stack.append(memory[addr])

    # Сохранение памяти
    start, end = memory_range
    with open(output_csv, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        for i in range(start, end + 1):
            writer.writerow([i, memory[i]])

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Интерпретатор для УВМ.")
    parser.add_argument("--input", required=True, help="Входной бинарный файл")
    parser.add_argument("--output", required=True, help="Файл с результатами работы")
    parser.add_argument("--memory", nargs=2, type=int, required=True, help="Диапазон памяти (начало и конец)")
    args = parser.parse_args()
    interpreter(args.input, args.output, tuple(args.memory))
