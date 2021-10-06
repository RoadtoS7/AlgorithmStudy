from collections import defaultdict
def solution(table, languages, preference):
    answer = ''
    score = dict()


    for r in table:
        ln = 6
        _r = r.split()
        value = dict()
        for i, t in  enumerate(_r[ln:0:-1]):
            value[t] = i + 1
        score[_r[0]] = value

    res = defaultdict(int)

    for l, p in zip(languages, preference):
        for job, value in score.items():
            if l in value:
                res[job] += value[l] * p

    answer = sorted(res.items(), key=lambda x: (-x[1], x[0]))[0][0]

    return answer

print(solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"],
               ["PYTHON", "C++", "SQL"],
               [7, 5, 5]
               ))

print(solution(
    ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"],
    ["JAVA", "JAVASCRIPT"],
    [7, 5]
))