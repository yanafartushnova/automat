import json

def MaxString(A, s, k):
    st = False
    m = 0
    if (k<len(s)):
        with open(A, 'r', encoding='utf-8') as fh: #открываем файл на чтение
            data = json.load(fh) #загружаем из файла данные в словарь data

        start = data['start'][0]
        finish = data['finish']
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
                for i in finish:
                    if(next_s[0]==i): 
                        m=r
                        f_st = True
                        st = True
                if(matrix.get(next_s[0])):
                    trs = matrix[next_s[0]]
                else: break
    return(st, m)

integer = 'integer.json'
real = 'real.json'
bools = 'bool.json'
keyword = 'keyword.json'
operation = 'operation.json'
whitespace = 'whitespace.json'
ids = 'id.json'
files = [real, integer, keyword, bools, operation, whitespace, ids]

with open('input.txt', 'r') as inp, open('output.txt', 'w') as out:
    s = inp.read()
    print(s)
    k = 0

    while (k <= len(s)):
        fl = True
        for i in files:
            res = MaxString(i, s, k)
            if (res[0] == True):
                out.write("<" + i[:i.find('.')] + ", " + s[k:k + res[1]] + ">" + '\n')
                k += res[1]
                fl = False
                break
        if(fl):k+=1


