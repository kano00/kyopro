# kano00
# https://adventofcode.com/2021/day/10

def calc1(chunk_list):
    left_brankets = ["(", "[", "{", "<"]
    right_brankets = [")", "]", "}", ">"]
    scores = [3,57,1197,25137]
    res = 0

    def calc_points(chunk):
        stack = []
        for c in chunk:
            for i in range(4):
                if c == left_brankets[i]:
                    stack.append(i)
                elif c== right_brankets[i]:
                    if len(stack) == 0:
                        print("error")
                        return 0
                    else:
                        # if corrupted
                        if right_brankets[stack.pop()] != c:
                            return scores[i]
        return 0

    for chunk in chunk_list:
        res += calc_points(chunk)
                    
    return res

def calc2(chunk_list):
    left_brankets = ["(", "[", "{", "<"]
    right_brankets = [")", "]", "}", ">"]
    scores = [1, 2, 3, 4]
    res_options = []

    def calc_remains(chunk):
        stack = []
        for c in chunk:
            for i in range(4):
                if c == left_brankets[i]:
                    stack.append(i)
                elif c== right_brankets[i]:
                    if len(stack) == 0:
                        print("error")
                        return []
                    else:
                        # if corrupted
                        if right_brankets[stack.pop()] != c:
                            return []
        return stack

    def calc_points(remains):
        points = 0
       
        while len(remains):
            p = remains.pop()
            points = points * 5 + scores[p]

        return points

    for chunk in chunk_list:
        remains = calc_remains(chunk)
        if remains:
            points = calc_points(remains)
            res_options.append(points)
        
    res_options.sort()
    res = res_options[len(res_options)//2]                
    return res


if __name__ == "__main__":
    chunk_list= []
    i = input()
    while i:
        chunk_list.append(i)
        i = input()
    
    res = calc2(chunk_list)
    print(res)