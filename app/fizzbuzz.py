def fizzbuzz(num):
    if num % 15 == 0:
        return 'fizzbuzz'
    elif num % 5 == 0:
        return 'buzz'
    elif num % 3 == 0:
        return 'fizz'
    else:
        return num

if __name__ == "__main__":
    for i in range(46):
        print(str(fizzbuzz(i)))
