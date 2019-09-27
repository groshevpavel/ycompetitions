def rle_str(str_to_encode: str) -> str:
    rc = 1
    prev_s, _res = "", ""

    for index in range(0, len(str_to_encode)-1):
        #prev_s = s[index - 1]
        next_s = str_to_encode[index + 1]
        cur_s = str_to_encode[index]
        
        if cur_s == next_s:
            rc += 1
        else:
            if rc > 1:
                _res += f"{cur_s}{rc}"
            else:
                if index != len(str_to_encode)-2:
                    _res += f"{cur_s}"
                else:
                    _res += f"{cur_s}{next_s}"
                #break
            rc = 1

    if rc > 1:
        _res += f"{cur_s}{rc}"
    else:
        _res += f"{next_s}"

    return _res

a = ['AAAABBBBBBBBBDDEEEEESSSSAAACCCFA', 'AAAAAAAAAAAAAAAAAAAAAAB', 'AAAAAAAAAAAAAAAA', 'AABABABABABABABBA']
print([rle_str(s) for s in a])

#>>> ['A4B9D2E5S4A3C3FAA', 'A22B', 'A16', 'A2BABABABABABAB2A']
