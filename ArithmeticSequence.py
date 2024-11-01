from OtherImporters import infinite_division, input_math


class ASequence:
    def __init__(self, a1, a2, d, an, n, min_sn=None):
        self.a1 = a1
        self.a2 = a2
        self.d = d
        self.an = an
        self.n = n
        self.min_sn = min_sn
        self.sq_sn()

    def sq_sn(self):
        if self.a1 == None:
            print("Error! a1 cannot be blank. Please change it.")
            self.a1 = input_math("a1: ")
        self.sq_d()
        if self.min_sn != None:
            self.sq_min_sn()
        self.sq_n()
        if self.d != 0:
            self.sn = infinite_division(self.n*(self.a1+self.an), 2)[0]
        else:
            self.sn = self.a1*self.n
        if self.a2 == None:
            self.a2 = self.a1+self.d
        self.sequence_info = {"a1": self.a1, "a2": self.a2,
                              "d": self.d, "an": self.an, "n": self.n, "sn": self.sn}

    def sq_d(self):
        while True:
            if self.d != None:
                if self.a2 != None:  # Troubleshooting
                    if self.a2 != self.a1 + self.d:
                        print(
                            "The sum of a1 and d is not equal to a2! Please change one of them.")
                        a12_d = input("a1 or a2 or d: ")
                        if a12_d == "a1":
                            self.a1 = input_math("a1: ")
                        elif a12_d == "a2":
                            self.a2 = input_math("a2: ")
                        elif a12_d == "d":
                            self.d = input_math("d: ")
                        else:
                            print("Error! Please try again.")
                    else:
                        break
                else:
                    break
            elif self.d == None and self.a2 != None:
                self.d = int(self.a2 - self.a1)
                break
            elif self.d == None and self.a2 == None:
                print("Both a2 and d cannot be unknown! Please change one of them.")
                a2_d = input("a2 or d: ")
                if a2_d == "a2":
                    self.a2 = input_math("a2: ")
                elif a2_d == "d":
                    self.d = input_math("d: ")
                else:
                    print("Error! Please try again.")

    def sq_n(self):
        while True:
            if self.n != None:  # Troubleshooting
                if self.an != None and self.d != 0:
                    if self.n != (self.an - self.a1)/self.d + 1:
                        print("an or n has a problem! Please change one of them.")
                        an_n = input("an or n: ")
                        if an_n == "an":
                            self.an = input_math("an: ")
                        elif an_n == "n":
                            self.n = input_math("n: ")
                        else:
                            print("Error! Please try again.")
                    else:
                        break
                elif self.an != None and self.d == 0:
                    if self.an != self.a1:
                        print("an has a problem! Please change it.")
                        self.an = input_math("an: ")
                    else:
                        break
                else:
                    self.an = self.a1 + (self.n-1)*self.d
                    break
            elif self.n == None and self.an != None:
                self.n = (self.an - self.a1)/self.d + 1
                if self.n == int(self.n):
                    self.n = int(self.n)
                    break
                else:
                    self.n = None
                    print("an has a problem! Please change it.")
                    self.an = input_math("an: ")
            elif self.n == None and self.an == None:
                print("Both an and n cannot be unknown! Please change one of them.")
                n_an = input("an or n: ")
                if n_an == "an":
                    self.an = input_math("an: ")
                elif n_an == "n":
                    self.n = input_math("n: ")
                else:
                    print("Error! Please try again.")

    def sq_min_sn(self):
        index = 1
        while self.min_sn[1] == "<":
            if (index*(2*self.a1+(index-1)*self.d))/2 > self.min_sn[0]:
                self.n = index
                break
            index += 1
        while self.min_sn[1] == "<=":
            if (index*(2*self.a1+(index-1)*self.d))/2 >= self.min_sn[0]:
                self.n = index
                break
            index += 1
        while self.min_sn[1] == "=":
            if (index*(2*self.a1+(index-1)*self.d))/2 == self.min_sn[0]:
                self.n = index
                break
            index += 1

    def show(self):
        if self.n == 1:
            return f"Sequence: {self.a1}"
        elif self.n == 2:
            return f"Sequence: {self.a1}, {self.an}"
        elif self.n == 3:
            return f"Sequence: {self.a1}, {self.a1+self.d}, {self.an}"
        elif self.n == 4:
            return f"Sequence: {self.a1}, {self.a1+self.d}, {self.a1+(self.d*2)}, {self.an}"
        elif self.n == 5:
            return f"Sequence: {self.a1}, {self.a1+self.d}, {self.a1+(self.d*2)}, {self.a1+(self.d*3)}, {self.an}"
        elif self.n > 5:
            return f"Sequence: {self.a1}, {self.a1+self.d}, {self.a1+(self.d*2)}, ..., {self.an}"

    def __getitem__(self, word):
        return self.sequence_info.get(word)
