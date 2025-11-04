import math

def area(r: int) -> float:
    ''' 
    Возвращает площадь круга

        Параметры:
                r (int): радиус круга
        Возвращаемое значение:
                Площадь круга (float)
    '''
    return math.pi * r * r

def perimeter(r: int) -> float:
    ''' 
    Возвращает длину окружности 

        Параметры:
                r (int): радиус окружностиs
        Возвращаемое значение:
                Длина окружности (float)
    '''
    return 2 * math.pi * r

def diameter(r: int) -> float:
    '''
    Возвращает диаметр круга
    
        Параметры:
                r (int): радиус круга
        Возвращаемое значение:
                Диаметр круга (float)
    '''
    return 2 * r

def sector_area(r: int, angle: float) -> float:
    '''
    Возвращает площадь сектора круга
    
        Параметры:
                r (int): радиус круга
                angle (float): угол сектора в градусах
        Возвращаемое значение:
                Площадь сектора (float)
    '''
    return (math.pi * r * r * angle) / 360

