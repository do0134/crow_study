giho = ("+", "-", "*", "/")

susik = input()
num = list()

for _ in range(len(susik)):
    if susik[_] in giho:
        num.append(susik[:_])
        num.append(susik[_])
        num.append(susik[_+1:])
        break


def calc(num1, num2, sik):
    value = 0
    if int(num1) < 0:
        num1 = int("-0o"+num1[1:], 8)
    else:
        num1 = int("0o"+num1, 8)
    if int(num2) < 0:
        num2 = int("-0o" + num2[1:], 8)
    else:
        num2 = int("0o"+num2, 8)
    if sik == "+":
        value = num1+num2
    elif sik == "-":
        value = num1-num2
    elif sik == "*":
        value = num1*num2
    elif sik == "/":
        if num2 == 0:
            return "invalid"
        value = num1//num2
    if value >= 0 :
        value = oct(value)
        return value[2:]
    else :
        value = oct(value)
        return "-"+ value[3:]


print(calc(num[0],num[2],num[1]))