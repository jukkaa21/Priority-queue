class Element:
    def __init__(self, dane, priorytet):

        self.__dane = dane
        self.__priorytet = priorytet

    def __lt__(self, other):
        return self.__priorytet < other

    def __gt__(self, other):
        return self.__priorytet > other

    def __eq__(self, other):
        return self.__priorytet == other

    def __repr__(self):
        wynik = f"{self.__priorytet} : {self.__dane}"
        return wynik


class Heap:
    def __init__(self):
        self.tab = []
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.tab[0]

    def left(self, idx):
        return 2*idx+1

    def right(self, idx):
        return 2*idx+2

    def parent(self, idx):
        return (idx-1)//2

    def fix_deq(self, idx):
        child_l_idx = self.left(idx)
        child_r_idx = self.right(idx)

        if child_l_idx > self.size-2 and child_r_idx > self.size-2:
            return

        child_l = self.tab[child_l_idx]
        child_r = self.tab[child_r_idx]

        if child_l_idx > self.size-2:
            if child_r > self.tab[idx]:
                self.tab[idx], self.tab[child_r_idx] = self.tab[child_r_idx], self.tab[idx]
            return
        elif child_r_idx > self.size-2:
            if child_l > self.tab[idx]:
                self.tab[idx], self.tab[child_l_idx] = self.tab[child_l_idx], self.tab[idx]
            return

        if (self.tab[idx] > child_l or self.tab[idx] == child_l) and (self.tab[idx] > child_r or self.tab[idx] == child_r):
            return
        else:
            if child_l > child_r:
                self.tab[idx], self.tab[child_l_idx] = self.tab[child_l_idx], self.tab[idx]
                self.fix_deq(child_l_idx)
            else:
                self.tab[idx], self.tab[child_r_idx] = self.tab[child_r_idx], self.tab[idx]
                self.fix_deq(child_r_idx)
                return

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            el = self.tab[0]
            self.tab[0], self.tab[self.size-1] = self.tab[self.size-1], self.tab[0]
            if self.size > 1:

                self.fix_deq(0)
            self.size -= 1

            return el

    def fix_enq(self, idx):
        parent_idx = self.parent(idx)
        if self.tab[parent_idx] > self.tab[idx] or self.tab[parent_idx] == self.tab[idx] or parent_idx<0:
            return
        else:
            self.tab[idx], self.tab[parent_idx] = self.tab[parent_idx], self.tab[idx]
            self.fix_enq(parent_idx)
            return

    def enqueue(self, element):
        if len(self.tab) == self.size:
            self.tab.append(element)
        elif len(self.tab) >= self.size:
            self.tab[self.size] = element

        el_id = self.size
        if self.size > 0:
            self.fix_enq(el_id)
        self.size += 1

    def print_tab(self):
        print('{', end=' ')
        print(*self.tab[:self.size], sep=', ', end=' ')
        print('}')

    def print_tree(self, idx, lvl):
        if idx<self.size:
            self.print_tree(self.right(idx), lvl+1)
            print(2*lvl*'  ', self.tab[idx] if self.tab[idx] else None)
            self.print_tree(self.left(idx), lvl+1)


#utworzenie pustej kolejki
kol = Heap()

# using enqueue in a loop to insert elements of priority from the list: [7, 5, 1, 2, 5, 3, 4, 8, 9] 
# with values corresponding to the being subsequent letters from the word "GRYMOTYLA"
lst = [7, 5, 1, 2, 5, 3, 4, 8, 9]
string = "GRYMOTYLA"
for i in range(9):
    el = Element(string[i], lst[i])
    kol.enqueue(el)

# current queue status as a heap 
kol.print_tree(0, 0)

# current queue status as a list
kol.print_tab()

d = kol.dequeue()

kol.print_tab()

print(d)

#opróżnienie kolejki z wypisaniem usuwanych danych
while kol.is_empty() is False:
    print(kol.dequeue())

kol.print_tab()
