n = 30


class Grid:
    def __init__(self):
        self.cell = [[1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1],
                     [1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1],
                     [1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1],
                     [1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1],
                     [1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1],
                     [1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1],
                     [1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1],
                     [1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1],
                     [1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1],
                     [1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1],
                     [1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1],
                     [1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1],
                     [1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1],
                     [1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1],
                     [1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1],
                     [1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1],
                     [1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1],
                     [1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1],
                     [1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1],
                     [1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1],
                     [1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1],
                     [1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1],
                     [1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1],
                     [1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1],
                     [1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1],
                     [1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1],
                     [1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1],
                     [1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1],
                     [1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1],
                     [1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1]
                     ]
        self.dict = {}
        k = -1
        a = 'a'
        for i in range(n):
            for j in range(n):
                k += 1
                k = str(k)
                d = a + k
                k = int(k)
                self.dict[d] = [i, j]


    def rules(self, i, j, l):
        def adjacent(cell, i, j):
            count = 0
            if i - 1 >= 0 and cell[i - 1][j] == 1:
                count += 1
            if i + 1 < n and cell[i + 1][j] == 1:
                count += 1
            if j - 1 >= 0 and cell[i][j - 1] == 1:
                count += 1
            if j + 1 < n and cell[i][j + 1] == 1:
                count += 1
            if i - 1 >= 0 and j - 1 >= 0 and cell[i - 1][j - 1] == 1:
                count += 1
            if i - 1 >= 0 and j + 1 < n and cell[i - 1][j + 1] == 1:
                count += 1
            if i + 1 < n and j - 1 >= 0 and cell[i + 1][j - 1] == 1:
                count += 1
            if i + 1 < n and j + 1 < n and cell[i + 1][j + 1] == 1:
                count += 1
            return count

        count = adjacent(self.cell, i, j)
        s = []
        if self.cell[i][j] == 1:
            if count >= 2 and count <= 3:
                s = [i, j]
                pass
        else:
            if count == 3:
                s = [i, j]
        if len(s) > 0:
            l.append(s)

    def add(self, row, column, element, name):
        var = 0
        for i in range(row, n):
            for j in range(column, n):
                if var >= len(element):
                    break
                else:
                    self.cell[i][j] = element[var]
                    self.dict[name[var]] = [i, j]

                var += 1

    def update(self, l):
        for i in range(n):
            for j in range(n):
                self.cell[i][j] = 0
        for i in l:
            self.cell[i[0]][i[1]] = 1

    def search_input(self, search):
        x=-1
        for key in self.dict:
            if key == search:
                i = self.dict[key]
                x=self.cell[i[0]][i[1]]
                break
        return x

    def dict_key(self, l):
        for x in self.dict:
            if x == l:
                return True
        else:
            return False

    def display(self):
        for i in range(n):
            # time.sleep(0.5)
            print(self.cell[i])


g = Grid()
print("Initial Pattern")
g.display()

while True:

    r = int(input("Enter the ith position   "))
    c = int(input("Enter jth position for  input  "))
    size = int(input("Enter the number of element less than 100  "))
    element = []
    name = []
    var = 0
    while var < size:
        print("Enter the element then enter the name of cell")
        ele = int(input())
        nme = input()
        if g.dict_key(nme) == False:
            name.append(nme)
            element.append(ele)
            var += 1
        else:
            print("Cell value that you have requested is not avalible as it is being used in different cell")
            print("Retry")
    g.add(r,c,element,name)
    l = []
    for i in range(n):
        for j in range(n):
            g.rules(i, j, l)
    g.update(l)
    print("After the rules applied")
    g.display()

    while 1:
        print("Press 1 to search if an element is present or press any other key to skip")
        key = int(input())

        if key == 1:
            search = input("Please Enter the cell name:  ")
            search = g.search_input(search)
            if search == 1:
                print("live")
            elif search==-1:
                print("No cell present with given input")
            else:
                print("dead")
        else:
            break
