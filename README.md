<h1 align="center">Домашняя работа №4 - ассемблер и интерпретатор для учебной виртуальной машины 
(УВМ)</a> 
<h3 align="center">Постановка задачи</h3>

Разработать ассемблер и интерпретатор для учебной виртуальной машины 
(УВМ). Система команд УВМ представлена далее. 

Для ассемблера необходимо разработать читаемое представление команд 
УВМ. Ассемблер принимает на вход файл с текстом исходной программы, путь к 
которой задается из командной строки. Результатом работы ассемблера является 
бинарный файл в виде последовательности байт, путь к которому задается из 
командной строки. Дополнительный ключ командной строки задает путь к файлу
логу, в котором хранятся ассемблированные инструкции в духе списков 
“ключ=значение”, как в приведенных далее тестах.

Интерпретатор принимает на вход бинарный файл, выполняет команды УВМ 
и сохраняет в файле-результате значения из диапазона памяти УВМ. Диапазон 
также указывается из командной строки

Форматом для файла-лога и файла-результата является csv. 

Необходимо реализовать приведенные тесты для всех команд, а также 
написать и отладить тестовую программу.

![image](https://github.com/user-attachments/assets/ed4bd88a-48c1-4cf8-9666-5f4a6ee7d041)

![image](https://github.com/user-attachments/assets/748cc00c-ba95-4516-9f8e-df5423b9a6aa)

![image](https://github.com/user-attachments/assets/167c8a36-701b-40ce-a110-56b72f60e6bc)

![image](https://github.com/user-attachments/assets/ed8cc5b2-ac29-437a-8135-9b52bcd58fc1)

### Тестовая программа: 
Выполнить поэлементно операцию побитовое "и" над вектором длины 6 и 
числом 176. Результат записать в исходный вектор.

### Запуск программы
```bash
cd:\Users\user\PycharmProjects\konfig_hw_4
.venv\Scripts\activate
python assembler.py --input test_all.txt --output output.bin --log output_log.csv
python interpreter.py --input output.bin --output memory_output.csv --memory 0 10
```

```bash
cd:\Users\user\PycharmProjects\konfig_hw_4
.venv\Scripts\activate
python test_program.py
```


### Входные данные для тестирования: 

- Входной файл с тестированием всех функций:
  
![image](https://github.com/user-attachments/assets/9f0c67d2-bade-4c8e-b503-0e31fc7e02da)
![image](https://github.com/user-attachments/assets/c0da40ba-22e1-4377-bbcb-b699080207dc)


- Логи:
  
![image](https://github.com/user-attachments/assets/11e5ecba-b50d-4e72-a056-56d2016c3764)


![image](https://github.com/user-attachments/assets/114fd209-441e-427d-83cb-0a3798937cd1)


- Итоговый файл:
  
  ![image](https://github.com/user-attachments/assets/7ea620e6-5f24-41df-a1e6-677e5a501f30)


- Входной файл с тестовой программой

![image](https://github.com/user-attachments/assets/444a3bc6-b9df-47d5-9ac1-e626e6de18a6)
![image](https://github.com/user-attachments/assets/e4774a8c-3c7a-4e74-a7b2-e22c7e53c2f2)


- Логи:

![image](https://github.com/user-attachments/assets/4ce16db4-b0eb-477f-9584-4e89adf4d52f)

![image](https://github.com/user-attachments/assets/641b87a3-7a93-4ed5-83d5-652e0e8d1679)


- Итоговый файл:

![image](https://github.com/user-attachments/assets/f5d036a8-b0d6-4dc8-a79b-3cf7f74e1992)
