def convertidor_c_f(celsius):
    return (celsius * 9/5)+32


def convertidor_f_c(Fahrenheit):
    return (Fahrenheit-32)*5/9

#3815
def convertidor_d_p(dolar):
    return dolar*3815

def convertidor_p_d(peso):
    return float(peso/3815)

print(convertidor_c_f(25))
print(convertidor_f_c(77))


print("1 dolar equivale a ", convertidor_d_p(1), "pesos colombianos")
print("100.000 peso colombiano corresponde a", convertidor_p_d(100000)," dolares")