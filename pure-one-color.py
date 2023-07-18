run = [[1,2,3],[2,3,4],[3,4,5],[4,5,6],[5,6,7],[6,7,8],[7,8,9]]
triples = [[1,1,1],[2,2,2],[3,3,3],[4,4,4],[5,5,5],[6,6,6],[7,7,7],[8,8,8],[9,9,9]]
heads = [[1,1],[2,2],[3,3],[4,4],[5,5],[6,6],[7,7],[8,8],[9,9]]
# all で二つ以上の数があればそれを雀頭として使う
for head in range(1,10):
    all = [1] * 4 + [2] * 4 + [3] * 4 + [4] * 4 + [5] * 4 + [6] * 4 + [7] * 4 + [8] * 4 + [9] * 4
    if all.count(head) >= 2:
        print("head:[{},{}]".format(head,head))
        all.remove(head)
        all.remove(head)
        # 雀頭を除いた部分
        # print(all)
        for triple_1 in range(1,10):
            answer = []
            if all.count(triple_1) >= 3:
                answer.append(triples[triple_1 - 1])
                all_1 = all.copy()
                all_1.remove(triple_1)
                all_1.remove(triple_1)
                all_1.remove(triple_1)
                for triple_2 in range(triple_1+1,10):
                    if all.count(triple_2) >= 3:
                        answer_2 = answer.copy()
                        all_2 = all_1.copy()
                        answer_2.append(triples[triple_2 -1])
                        all_2.remove(triple_2)
                        all_2.remove(triple_2)
                        all_2.remove(triple_2)
                        for triple_3 in range(triple_2+1,10):
                            if all.count(triple_3) >= 3:
                                answer_3 = answer_2.copy()
                                all_3 = all_2.copy()
                                answer_3.append(triples[triple_3 - 1])
                                all_3.remove(triple_3)
                                all_3.remove(triple_3)
                                all_3.remove(triple_3)
                                for triple_4 in range(triple_3+1,10):
                                    if all.count(triple_4) >= 3:
                                        answer_4 = answer_3.copy()
                                        all_4 = all_3.copy()
                                        answer_4.append(triples[triple_4 - 1])
                                        all_4.remove(triple_4)
                                        all_4.remove(triple_4)
                                        all_4.remove(triple_4)
                                        print(answer_4)
                                        
                           
        
