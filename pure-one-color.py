import itertools

# 鳴いている形を指定
calling = [[1,2,3],[2,3,4]]
# そのほかで使われている枚数をそれぞれ指定
one = 0
two = 0
three = 0
four = 0
five = 0
six = 0
seven = 0
eight = 0
nine = 0
#######################################################################

def get_unique_list(seq):
    seen = []
    return [x for x in seq if x not in seen and not seen.append(x)]
if __name__ == "__main__":
    # 何メンツ鳴いているか
    calling_num = len(calling)
    print("calling-num:{}".format(calling_num))
    # 鳴いている形をすべて合体
    calling = list(itertools.chain.from_iterable(calling))

    # それぞれの枚数で使える数を計算
    one_remain = 4 - calling.count(1) - one
    two_remain = 4 - calling.count(2) - two
    three_remain = 4 - calling.count(3) - three
    four_remain = 4 - calling.count(4) - four
    five_reamin = 4 - calling.count(5) - five
    six_remain = 4 - calling.count(6) - six
    seven_remain = 4 - calling.count(7) - seven
    eight_remain = 4 - calling.count(8) - eight
    nine_remain = 4 - calling.count(9) - nine
    print("1:{}枚, 2:{}枚, 3:{}枚, 4:{}枚, 5:{}枚, 6:{}枚, 7:{}枚, 8:{}枚, 9:{}枚".format(one_remain, two_remain, three_remain, four_remain, five_reamin, six_remain, seven_remain, eight_remain, nine_remain))

    runs_triples = [[1,2,3],[2,3,4],[3,4,5],[4,5,6],[5,6,7],[6,7,8],[7,8,9],[1,1,1],[2,2,2],[3,3,3],[4,4,4],[5,5,5],[6,6,6],[7,7,7],[8,8,8],[9,9,9]]
    heads = [[1,1],[2,2],[3,3],[4,4],[5,5],[6,6],[7,7],[8,8],[9,9]]
    all_pure_one_color = []
    # 面子手
    for head in heads:
        all = [1] * one_remain + [2] * two_remain + [3] * three_remain + [4] * four_remain + [5] * five_reamin + [6] * six_remain + [7] * seven_remain + [8] * eight_remain + [9] * nine_remain 
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
    # 七対子
    if calling_num == 0:
        seven_pairs = []
        for pair in itertools.combinations(heads, 7):
            pair = sum(list(pair),[])
            pair.sort()
            all_pure_one_color.append(pair)

    unique_list = get_unique_list(all_pure_one_color)
    print(unique_list)
    print("総数：{}".format(len(unique_list)))