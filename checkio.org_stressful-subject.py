# Задачка py.checkio.org
# https://py.checkio.org/mission/stressful-subject

# Sofia has had a very stressful month and decided to take a vacation for a week.
# To avoid any stress during her vacation she wants to forward emails with a stressful subject line to Stephen.

# The function should recognise if a subject line is stressful. 
# A stressful subject line means that all letters are in uppercase, and/or ends by at least 3 exclamation marks,
# and/or contains at least one of the following “red” words: "help", "asap", "urgent". 
# Any of those "red" words can be spelled in different ways - "HELP", "help", "HeLp", "H!E!L!P!", "H-E-L-P",
# even in a very loooong way "HHHEEEEEEEEELLP"

# Input: Subject line as a string.

# Output: Boolean.

# Example:

# is_stressful("Hi") == False

# is_stressful("I neeed HELP") == True

# Precondition: Subject can be up to 100 letters 


# Нюанс в том, что если проверять побуквенное вхождение букв из стоп-слова в проверяемое то может быть ложное срабатывание
# например в "Headlamp, wastepaper bin and supermagnificently" - первое слово сработает на "help", второе на "asap", третье на "urgent"
# по-буквенно стоп-слово "help" входит в "Headlamp"



from string import punctuation

def is_stressful(subj):
    """
        recoognise stressful subject
    """
    def y_words(subj):
        return iter([w for w in subj.split(' ') if w != ""])

    def check_red(w, red_words):
        w = w.lower()
        for red in red_words:
            if len(w) < len(red): continue
            for ww in w:
                if ww not in red and ww not in punctuation:
                    break
                else:
                    continue
            else:
                return True
        return False
            
    
    if subj.isupper(): return True
    if subj.endswith("!!!"): return True

    red_words = ["help", "asap", "urgent"]
    
    for w in y_words(subj):
        if check_red(w, red_words): return True
    
    return False
