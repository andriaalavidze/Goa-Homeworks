def filter_odd(numbers):
    even = []
    for i in numbers:
        if i % 2 == 0:
            even.append(i)
    print(even)
filter_odd([1,2,3,4,5,6,7,8,9])