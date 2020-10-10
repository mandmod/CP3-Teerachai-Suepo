def vatCalculate(totalPrice):
    result = totalPrice + (totalPrice * 7 / 100)
    return result


inputPrice = int(input("Input price : "))
print(vatCalculate(inputPrice))
