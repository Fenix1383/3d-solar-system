from celestial import *


def update_physics(cels: list[Celestial], dt: float):
    # 1. Рассчитываем текущие ускорения для всех тел
    # acceleration = Force / mass
    current_accels = []
    for cel in cels:
        force = result_force(cel, cels)
        current_accels.append(force / cel.mass)

    # 2. Обновляем позиции и делаем "полушаг" скорости
    for i, cel in enumerate(cels):
        acc = current_accels[i]
        
        # Обновляем позицию: pos = pos + v*dt + 0.5*a*dt^2
        cel.position += (cel.velocity * dt) + (acc * (0.5 * dt**2))
        
        # Полушаг скорости: v = v + 0.5*a*dt
        # Мы сохраняем это прямо в cel.velocity временно
        cel.velocity += acc * (0.5 * dt)

    # 3. Рассчитываем НОВЫЕ ускорения на основе НОВЫХ позиций
    # Это критически важный момент метода Верле
    new_accels = []
    for cel in cels:
        new_force = result_force(cel, cels)
        new_accels.append(new_force / cel.mass)

    # 4. Завершаем обновление скорости
    for i, cel in enumerate(cels):
        new_acc = new_accels[i]
        
        # Вторая половина шага скорости: v = v + 0.5*new_a*dt
        cel.velocity += new_acc * (0.5 * dt)