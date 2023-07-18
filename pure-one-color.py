
def get_unique_list(seq):
    seen = []
    return [x for x in seq if x not in seen and not seen.append(x)]
if __name__ == "__main__":
    runs = [[1,2,3],[2,3,4],[3,4,5],[4,5,6],[5,6,7],[6,7,8],[7,8,9]]
    triples = [[1,1,1],[2,2,2],[3,3,3],[4,4,4],[5,5,5],[6,6,6],[7,7,7],[8,8,8],[9,9,9]]
    runs_triples = [[1,2,3],[2,3,4],[3,4,5],[4,5,6],[5,6,7],[6,7,8],[7,8,9],[1,1,1],[2,2,2],[3,3,3],[4,4,4],[5,5,5],[6,6,6],[7,7,7],[8,8,8],[9,9,9]]
    heads = [[1,1],[2,2],[3,3],[4,4],[5,5],[6,6],[7,7],[8,8],[9,9]]
    all_pure_one_color = []
    # all で二つ以上の数があればそれを雀頭として使う
    for head in heads:
        all = [1] * 4 + [2] * 4 + [3] * 4 + [4] * 4 + [5] * 4 + [6] * 4 + [7] * 4 + [8] * 4 + [9] * 4
        if all.count(head[0]) >= 2:
            print("head:{}".format(head))
            all.remove(head[0])
            all.remove(head[0])
            # 雀頭を除いた部分
            for element in runs_triples:
                answer = []
                if (element[0] != element[1] and all.count(element[0]) >= 1 and all.count(element[1]) >= 1 and all.count(element[2]) >= 1 ) \
                or (element[0] == element[1] and all.count(element[0]) >= 3):
                    answer.append(element)
                    all_1 = all.copy()
                    all_1.remove(element[0])
                    all_1.remove(element[1])
                    all_1.remove(element[2])
                    for element_2 in runs_triples:
                        answer_2 = answer.copy()
                        if (element_2[0] != element_2[1] and all_1.count(element_2[0]) >= 1 and all_1.count(element_2[1]) >= 1 and all_1.count(element_2[2]) >= 1 ) \
                        or (element_2[0] == element_2[1] and all_1.count(element_2[0]) >= 3):
                            answer_2.append(element_2)
                            all_2 = all_1.copy()
                            all_2.remove(element_2[0])
                            all_2.remove(element_2[1])
                            all_2.remove(element_2[2])
                            for element_3 in runs_triples:
                                answer_3 = answer_2.copy()
                                if (element_3[0] != element_3[1] and all_2.count(element_3[0]) >= 1 and all_2.count(element_3[1]) >= 1 and all_2.count(element_3[2]) >= 1 ) \
                                or (element_3[0] == element_3[1] and all_2.count(element_3[0]) >= 3):
                                    answer_3.append(element_3)
                                    all_3 = all_2.copy()
                                    all_3.remove(element_3[0])
                                    all_3.remove(element_3[1])
                                    all_3.remove(element_3[2])
                                    for element_4 in runs_triples:
                                        answer_4 = answer_3.copy()
                                        if (element_4[0] != element_4[1] and all_3.count(element_4[0]) >= 1 and all_3.count(element_4[1]) >= 1 and all_3.count(element_4[2]) >= 1 ) \
                                        or (element_4[0] == element_4[1] and all_3.count(element_4[0]) >= 3):
                                            answer_4.append(element_4)
                                            all_4 = all_3.copy()
                                            all_4.remove(element_4[0])
                                            all_4.remove(element_4[1])
                                            all_4.remove(element_4[2])
                                            answer_4.append(head)
                                            answer_4 = sum(answer_4,[])
                                            answer_4.sort()
                                            all_pure_one_color.append(answer_4)
    # # 七対子
    import itertools
    seven_pairs = []
    for pair in itertools.combinations(heads, 7):
        pair = sum(list(pair),[])
        pair.sort()
        all_pure_one_color.append(pair)
    unique_list = get_unique_list(all_pure_one_color)
    print(unique_list)
    print("総数：{}".format(len(unique_list)))