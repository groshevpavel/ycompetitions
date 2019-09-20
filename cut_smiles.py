lines = [
"Я работаю в Гугле :-)))"
,"везет :-) а я туда собеседование завалил:-(("
,"лол:)"
,"Ааааа!!!!! :-))(())"
]

# выпиливаем смайлы из строки
# смайл может иметь произвольное количество улыбок, нужно выпилить все
# смайлом считается только тот, который начинается с :-
# напр, "Ааааа!!!!! :-))(())" --> "Ааааа!!!!! (())";; "лол:)" --> "лол:)"

def cut_smiles(s:str)->str:
    marker = ':-'
    
    smile_sym=""
    i, smile_start_index = 0, 0
    
    while i<len(s):
        if s[i:i+2] == marker: # нашли маркер
            smile_start_index = i
            smile_sym = s[i+2]
            i+=3
        elif s[i] != smile_sym: # смайл закончился
            s = s[:smile_start_index] + s[i:]
            i -= i - smile_start_index
        else:
            i += 1

    return s

def gen_cut_smiles(lines:list)->str:
    return iter([cut_smiles(s) for s in lines])
