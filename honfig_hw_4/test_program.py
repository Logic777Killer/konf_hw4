from assembler import assembler
from interpreter import interpreter

def test_vector():
    # Подготовка программы
    input_program = "test_program.txt"
    output_binary = "output.bin"
    output_log = "output_log.csv"
    output_csv = "memory_output.csv"

    # Создаем текстовую программу
    with open(input_program, 'w') as file:
        file.write("0 255\n")
        file.write("0 176\n")
        file.write("4 0\n")
        file.write("6 0\n")
        file.write("\n")

        file.write("0 200\n")
        file.write("0 176\n")
        file.write("4 0\n")
        file.write("6 1\n")
        file.write("\n")

        file.write("0 128\n")
        file.write("0 176\n")
        file.write("4 0\n")
        file.write("6 2\n")
        file.write("\n")

        file.write("0 100\n")
        file.write("0 176\n")
        file.write("4 0\n")
        file.write("6 3\n")
        file.write("\n")

        file.write("0 50\n")
        file.write("0 176\n")
        file.write("4 0\n")
        file.write("6 4\n")
        file.write("\n")

        file.write("0 0\n")
        file.write("0 176\n")
        file.write("4 0\n")
        file.write("6 5\n")

    # Ассемблируем программу
    assembler(input_program, output_binary, output_log)
    print(f"Собранный бинарный файл: {output_binary}")
    print(f"Лог-файл ассемблера: {output_log}")

    # Выполняем интерпретацию
    interpreter(output_binary, output_csv, (0, 5))
    print(f"Результат интерпретации: {output_csv}")

if __name__ == "__main__":
    test_vector()
