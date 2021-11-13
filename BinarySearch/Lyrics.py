from bisect import bisect_left, bisect_right


def count_range(words, left_word, right_word):
    left_index = bisect_left(words, left_word)
    right_index = bisect_right(words, right_word)
    return right_index - left_index


def solution(words, queries):
    max_len = len(max(words, key=len))
    word_list = [[] for _ in range(max_len + 1)]
    rev_word_list = [[] for _ in range(max_len + 1)]
    for word in words:
        word_list[len(word)].append(word)
        rev_word_list[len(word)].append(word[::-1])
    for i in range(max_len + 1):
        word_list[i].sort()
        rev_word_list[i].sort()
    result = []
    for query in queries:
        if query[0] != '?':
            res = count_range(word_list[len(query)], query.replace('?', 'a'),
                              query.replace('?', 'z'))
        else:
            res = count_range(rev_word_list[len(query)],
                              query[::-1].replace('?', 'a'),
                              query[::-1].replace('?', 'z'))
        result.append(res)
    return result


words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(words, queries))
