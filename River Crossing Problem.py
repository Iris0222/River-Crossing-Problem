
class State:
    def __init__(self, s, w, b):
        self.s = s  #sheep
        self.w = w  #wolf
        self.b = b  # 1左 0右
        self.node = [s, w, b]
        self.father = None


open_list = []
closed_list = []
goal = State(0, 0, 0)

def exist(new, list):
    for ll in list:
        if new.node == ll.node:
            return True
    return False

# 安全的狀態 (m, n, P), 則 m ≤ n（除非 n = 0），且 M – m ≤ N – n（除非 N – n = 0）
def notSafe(s, SHEEP, WOLF):
    if (s.s != 0 and s.s < s.w) or (s.s != SHEEP and SHEEP - s.s < WOLF - s.w) or s.s > SHEEP or s.s < 0 or s.w > WOLF or s.w < 0 :
        return True
    else:
        return False

def invaildStep(new, s):
    if s.father == None:
        return False
    elif new.node == s.father.node:
        return True
    else:
        return False

def BFS(s, SHEEP, WOLF):
    open_list = [s]
    #print(goal.node)
    while open_list:
        get = open_list[0]
        #print(get.node)
        if get.node == goal.node:  # 結束
            return get
        open_list.remove(get)

        closed_list.append(get)
        for i in range(SHEEP+1): # 1-SHEEP
            for j in range(WOLF+1):
                if i + j == 0 or i + j > 2 or (i != 0 and i < j): # 不安全
                    continue
                #print("i: ", end="")
                #print(i, end="")
                #print(", j: ", end="")
                #print(j)

                if get.b == 0 :
                    new = State(get.s + i, get.w + j, 1)
                    #print("0:",end = "")
                    #print(new.node)
                else:
                    new = State(get.s - i, get.w - j, 0)
                    #print("1: " ,end = "")
                    #print(new.node)

                if notSafe(new,SHEEP,WOLF) or invaildStep(new, get):
                    pass
                else:
                    new.father = get
                    if exist(new,open_list):
                        pass
                    elif exist(new, closed_list):
                        pass
                    else:
                        open_list.append(new)

                #os.system("pause")


def printList(list):
    temp = []
    if list is None:
        return
    printList(list.father)
    temp.append(list.w)
    temp.append(list.s)
    if list.b == 1:
        temp.append("W")
    else:
        temp.append("E")
    print(temp)
    temp.clear()


if __name__ == '__main__':
    SHEEP = 0
    WOLF = 0
    while True:
        while True:
            print("每列代表輸入初始狼與羊的數目 M、N（均為正整數，且 M ≤ N），0 0 表示結束")
            WOLF, SHEEP = input("Input the number of wolf and sheep : ").split()

            try:
                if int(SHEEP) < int(WOLF):
                    print("sheep must be larger than wolf!")
                else:
                    break
            except:
                print("Error Input!")

        # ==================================
        sheep = int(SHEEP)
        wolf = int(WOLF)
        goal = State(0, 0, 0)
        init = State(sheep, wolf, 1)
        list = BFS(init, sheep, wolf)

        # ===================================
        if list:
            print("Solution: ")
            printList(list)
        else:
            print("NO Solution!")

        print("=======================================")

        open_list.clear()
        closed_list.clear()

