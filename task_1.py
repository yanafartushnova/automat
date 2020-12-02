import json

def MaxString(A, s, k):
    st = False
    m = 0
    if (k<len(s)):
        with open(A, 'r', encoding='utf-8') as fh: #открываем файл на чтение
            data = json.load(fh) #загружаем из файла данные в словарь data

        start = data['start'][0]
        finish = data['finish'][0]
        matrix = data['matrix']

        f_st = False
        cur_st = True
        r = 0
        trs = matrix[start]
        while(k < len(s) and cur_st):
            next_s = trs.get(s[k])
            if(next_s == None or k == len(s)):
                if(f_st):
                    st = True
                    m=r
                else: cur_st = False
                break
            else:
                r+=1
                k+=1
                if(next_s[0]==finish):
                    m=r
                    f_st = True
                    st = True
                trs = matrix[next_s[0]]
    return(st, m)

s = input("Введите строку: ")
A = 'data1.json'
res = MaxString(A, s, 0)
print(res)
        
