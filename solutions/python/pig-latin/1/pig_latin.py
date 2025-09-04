vowels = ("a", "e", "i", "o", "u")

def translate(text):
    words = text.split()
    result = []

    for word in words:
        # Rule 1
        if word.startswith(("xr", "yt")) or word[0] in vowels:
            result.append(word+"ay")
            continue
        else:
            idx = 0
            while idx < len(word):
                if word[idx] in vowels or (idx != 0 and word[idx] == "y"): # Rule 2 + 4
                    break
                if word[idx:idx+2] == "qu": # Rule 3
                    idx+=2
                    break
                else:
                     idx+=1
            result.append(word[idx:] + word[:idx] + "ay")
    return " ".join(result)