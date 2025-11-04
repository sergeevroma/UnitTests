# Геометрическая библиотека с Unit-тестами

Простая библиотека для вычисления геометрических параметров различных фигур с unit-тестами.

## Поддерживаемые фигуры

### Круг (`circle.py`)
- **Площадь круга** - `area(r)`
- **Длина окружности** - `perimeter(r)` 
- **Диаметр** - `diameter(r)`
- **Площадь сектора** - `sector_area(r, angle)`

### Прямоугольник (`rectangle.py`)
- **Площадь** - `area(a, b)`
- **Периметр** - `perimeter(a, b)`
- **Диагональ** - `diagonal(a, b)`
- **Проверка на квадрат** - `is_square(a, b)`

### Квадрат (`square.py`)
- **Площадь** - `area(a)`
- **Периметр** - `perimeter(a)`
- **Диагональ** - `diagonal(a)`
- **Площадь вписанной окружности** - `inscribed_circle_area(a)`

### Треугольник (`triangle.py`)
- **Площадь** - `area(a, h)`
- **Периметр** - `perimeter(a, b, c)`
- **Проверка на равносторонность** - `is_equilateral(a, b, c)`
- **Проверка на прямоугольность** - `is_right_triangle(a, b, c)`

##  Запуск тестов

### Способ 1: Запуск всех тестов
```bash
python main.py
```

### Способ 2: Запуск конкретного класса тестов
```bash
python -m unittest test_geometry.TestRectangle -v
python -m unittest test_geometry.TestCircle -v
```
