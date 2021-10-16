def solution(s):
    result = []

    if len(s) == 1:
        return 1

    for i in range(1, len(s) // 2 + 1):
        count = 1
        index = 0
        char_sum = 0
        total = []
        while index <= len(s) - 2 * i:
            if s[index : index + i] == s[index + i: index + 2 * i]:
                count += 1
                index += i
            else:
                if count == 1:
                    char_sum += i
                else:
                    total.append(count)
                    count = 1
                index += i
        if count != 1:        
          total.append(count)
        else:
          char_sum += i

        char_sum += len(total) * i
        char_sum += len(s) - index - i
        num_sum = 0
        for num in total:
            num_sum += len(str(num))
        result.append(char_sum + num_sum)
    return min(result)

a = [
    "aabbaccc",
    "ababcdcdababcdcd",
    "abcabcdede",
    "abcabcabcabcdededededede",
    "xababcdcdababcdcd",

    'aaaaaa',
]

for x in a:
    print(solution(x))