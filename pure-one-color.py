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
                answer.append(triple_1)
                answer.append(triple_1)
                answer.append(triple_1)
                for triple_2 in range(triple_1+1,10):
                    if all.count(triple_2) >= 3:
                        answer.append(triple_2)
                        answer.append(triple_2)
                        answer.append(triple_2)
                        for triple_3 in range(triple_2+1,10):
                            if all.count(triple_3) >= 3:
                                answer.append(triple_3)
                                answer.append(triple_3)
                                answer.append(triple_3)
                                for triple_4 in range(triple_3+1,10):
                                    if all.count(triple_4) >= 3:
                                        answer.append(triple_4)
                                        answer.append(triple_4)
                                        answer.append(triple_4)
                                        print(answer)
                                        break
                                        
                           
        
