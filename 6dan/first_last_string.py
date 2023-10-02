def solution(string, ending):
    len_endig = len(ending)
    # would work too!
    # return string.endswith(ending)
    return True if ending == string[-len_endig:] or ending == '' else False

string = "Coool"
for i in string:
    print(i)

ending = ""

print(solution(string, ending))