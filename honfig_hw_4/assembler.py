import struct
import csv

def assembler(input_file, output_binary, output_log):
    commands = []
    with open(input_file, 'r') as file:
        for line in file:
            # Пропускаем пустые строки и комментарии
            line = line.strip()
            if not line or line.startswith('#'):
                continue

            parts = line.split()
            if len(parts) != 2:
                print(f"Неверный формат команды: {line}")
                continue

            command = {
                "A": int(parts[0]),
                "B": int(parts[1])
            }
            commands.append(command)

    with open(output_binary, 'wb') as binary_file, open(output_log, 'w', newline='') as log_file:
        writer = csv.writer(log_file)
        writer.writerow(["A", "B"])
        for command in commands:
            a = command["A"] & 0x7  # Биты 0-2
            b = command["B"] & 0xFFFFFF  # Биты 3-25
            instruction = (a << 25) | b
            binary_file.write(struct.pack(">I", instruction))
            writer.writerow([a, b])

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Ассемблер для УВМ.")
    parser.add_argument("--input", required=True, help="Входной текстовый файл программы")
    parser.add_argument("--output", required=True, help="Выходной бинарный файл")
    parser.add_argument("--log", required=True, help="Лог-файл ассемблера")
    args = parser.parse_args()
    assembler(args.input, args.output, args.log)
