def fizz_buzz_plus(number):
    list_divide = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    list_result = ["fizz", "buzz", "bizz", "bazz", "boom",
                   "bing", "bang", "bong", "fozz", "fazz", "woof"]

    length_divide_by = len(list_divide)   
    text = "" 
    for i in range(length_divide_by):
        result = list_result[i]
        divisible_by = list_divide[i]
        if number % divisible_by == 0:
            text += result
            print(text)

    return number if text == "" else text

fizz_buzz_plus(2145)
