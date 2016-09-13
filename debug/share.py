from multiprocessing import Process, Value, Array


def f(n, a):
    n.value = n.value + 1
    for i in range(len(a)):
        a[i] = a[i] * 10


if __name__ == '__main__':
    num = Value('i', 1)
    arr = Array('i', range(10))
    print(arr)
    p = Process(target=f, args=(num, arr))
    p.start()
    p.join()
    print(num.value)
    print(arr[:])

    p2 = Process(target=f, args=(num, arr))
    p2.start()
    p2.join()
    print(num.value)
    print(arr[:])