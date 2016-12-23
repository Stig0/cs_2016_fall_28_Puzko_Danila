from functools import reduce
import math
import matplotlib.pyplot as plt
import numpy as np


while True:

    print("Добро пожадовать")
    print("Введите '1.1' для вычисления суммы for-циклом")
    print("Введите '1.2' для вычисления суммы с while-циклом")
    print("Введите '1.3' для вычисления суммы рекурсией")
    print("Введите '2' для вычисления степени двойки")
    print("Введите '3' для вычисления cреднего арифметического")
    print("Введите '4' для вычисления номера числа в последовательности Фибоначчи")
    print("Введите '5' для вычисления факториала")
    print("Введите '6' для замены максимального на минимальное и наоборот")
    print("Введите '7' для нахождения расстояния между точками")
    print("Введите '8' для построения  графика траектории снаряда")
    print("Введите '0' для выхода")


    user_input = input(":")

    if user_input == "0":
        break

    elif user_input == "1.1":
        a = [int(x) for x in input("Введите числа через пробел").split()]
        b = 0
        for i in a:
            b += i

        print(b)

    elif user_input == "1.2":
        s = [int(x) for x in input("Введите числа через пробел").split()]

        i = 0

        summa = 0

        while i < len(s):
            summa += s[i]
            i += 1

        print(summa)

    elif user_input == "1.3":
        def summa(n):
            if len(n) == 1:
                return n[0]
            else:
                return n[0] + summa(n[1:])

        print(summa([int(x) for x in input("Введите числа через пробел:").split()]))



    elif user_input == "2":
        n = int(input("Введите число:"))
        i = 0
        while 2 ** i <= n:
            i += 1

        print(i - 1)

    elif user_input == "3":
        d = [int(x) for x in input("Введите числа через пробел:").split()]
        q = reduce(lambda x, y: x + y, d)
        res = q / len(d)
        print(res)

    elif user_input == "4":
        fib1 = 0
        fib2 = 1
        n = int(input("Введите число:"))
        fib_sum = 0
        k = 2
        while fib_sum < n:
            fib_sum = fib2 + fib1
            fib1 = fib2
            fib2 = fib_sum
            k += 1
        if fib_sum == n:
            print(k)
        if fib_sum > n:
            print(-1)

    elif user_input == "5":
        n = int(input("Введите число:"))

        factorial = 1
        for i in range(1, n + 1):
            factorial *= i

        print(factorial)


    elif user_input == "6":
        q = [int(x) for x in input("Введите числа через пробел:").split()]

        i = 0
        while q[i] < max(q):
            i += 1

        k = 0
        while q[k] > min(q):
            k += 1

        q[i], q[k] = q[k], q[i]
        print(q)


    elif user_input == "7":
        c = [int(x) for x in input("Введите числа через пробел:").split()]
        x1 = float(c[0])
        y1 = float(c[1])
        x2 = float(c[2])
        y2 = float(c[3])
        s = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        print(s)

    elif user_input == "8":
        g = 3.711

        v = float(input("Введите скорость:"))

        alpha = float(input("Введите угол в градусах:"))

        m = alpha * math.pi / 180
        t1 = 1
        t2 = 1
        while t2 > 0:
            t2 = v * math.sin(m) * t1 - (g * t1 ** 2) / 2
            t1 += 0.01

        t = np.arange(0, t1, 0.01)
        s = v * math.cos(m) * t
        h = (v * math.sin(m) * t - (g * t ** 2) / 2)
        plt.plot(s, h)

        plt.axis('equal')

        plt.xlabel(r'$s$')

        plt.ylabel(r'$h$')

        plt.title(r'$Trajectory$')

        plt.grid(True)

        plt.show()


    else:
        print("Команда не найдена")
