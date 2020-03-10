def saat():
    num_chas1=int(input('vvedite chasy: '))
    num_min1=int(input('vvedite min: '))
    num_sec1=int(input('vvedite sec: '))
    num_chas2=int(input('vvedite chasy-2: '))
    num_min2=int(input('vvedite min-2: '))
    num_sec2=int(input('vvedite sec-2: '))
    return(((num_chas1-num_chas2)*3600)+((num_min1-num_min2)*60)+(num_sec1-num_sec2))
print(saat())