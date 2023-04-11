
def calc (m):
    a = 0
    for m1 in ['', '-', '+']:
        if a == 1:
            break
        for m2 in ['', '-', '+']:
            for m3 in ['', '-', '+']:
                for m4 in ['', '-', '+']:
                    for m5 in ['', '-', '+']:
                        for m6 in ['', '-', '+']:
                            for m7 in ['', '-', '+']:
                                for m8 in ['', '-', '+']:
                                    n = '1' + m1 + '2' + m2 + '3' + m3 + '4' + m4 + '5' + m5 + '6' + m6 + '7' + m7 + '8' + m8 + '9'
                                    if eval(n) == m and a == 0:
                                        a = 1
                                        return n
    if a == 0:
        return 'Нет решений'

print(
f"""
{calc(122)=}
{calc(218)=}
{calc(221)=}
"""
)