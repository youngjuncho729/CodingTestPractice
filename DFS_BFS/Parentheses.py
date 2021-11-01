def check_balanced(p):
    stack = list()
    for c in p:
        if c == '(':
            stack.append(c)
        else:
            if len(stack) == 0:
                return False
            stack.pop()
    if len(stack) != 0:
        return False
    return True


def solution(p):
    if check_balanced(p) or len(p) == 0:
        return p
    count_1 = 0
    count_2 = 0
    u, v = '', ''
    for index in range(len(p)):
        if p[index] == '(':
            count_1 += 1
        else:
            count_2 += 1
        if count_1 == count_2:
            u = p[:index + 1]
            v = p[index + 1:]
            print("u:", u , " v:", v)
            break
    if check_balanced(u):
        return u + solution(v)
    else:
        result = '('
        result += solution(v)
        result += ')'
        if len(u) >= 4:
          for i in range(1, len(u) - 1):
              if u[i] == '(':
                  result += ')'
              else:
                  result += '('
        return result


p1 = "(()())()"
p2 = ")("
p3 = "()))((()"
p4 = "(()))("
p5 = ''
print(solution(p3))
