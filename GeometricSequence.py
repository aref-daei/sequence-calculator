from OtherImporters import infinite_power, infinite_log, infinite_division, input_math


class GSequence:
    def __init__(self, a1, a2, q, an, n, min_sn=None):
        self.a1 = a1
        self.a2 = a2
        self.q = q
        self.an = an
        self.n = n
        self.min_sn = min_sn
        self.sq_sn()

    def sq_sn(self):
        if self.a1 == None:
            print("Error! a1 cannot be blank. Please change it.")
            self.a1 = input_math("a1: ")
        self.sq_q()
        if self.min_sn != None:
            self.sq_min_sn()
        self.sq_n()
        if self.q != 1:
            self.sn = infinite_division(self.a1*(infinite_power(self.q, self.n)-1), (self.q-1))[0]
        else:
            self.sn = self.a1*self.n
        if self.a2 == None:
            self.a2 = self.a1*self.q
        self.sequence_info = {"a1": self.a1, "a2": self.a2,
                              "q": self.q, "an": self.an, "n": self.n, "sn": self.sn}

    def sq_q(self):
        while True:
            if self.q != None:
                if self.a2 != None:  # Troubleshooting
                    if self.a2 != self.a1 * self.q:
                        print(
                            "The product of a1 and q is not equal to a2! Please change one of them.")
                        a12_q = input("a1 or a2 or q: ")
                        if a12_q == "a1":
                            self.a1 = input_math("a1: ")
                        elif a12_q == "a2":
                            self.a2 = input_math("a2: ")
                        elif a12_q == "q":
                            self.q = input_math("q: ")
                        else:
                            print("Error! Please try again.")
                    else:
                        break
                else:
                    break
            elif self.q == None and self.a2 != None:
                self.q = infinite_division(self.a2, self.a1)
                if self.q[1] == 0:
                    self.q = self.q[0]
                    break
                else:
                    self.q = None
                    print(
                        "a1 or a2 has a problem! Please change one of them.")
                    a12_q = input("a1 or a2: ")
                    if a12_q == "a1":
                        self.a1 == input_math("a1: ")
                    elif a12_q == "a2":
                        self.a2 = input_math("a2: ")
                    else:
                        print("Error! Please try again.")
            elif self.q == None and self.a2 == None:
                print("Both a2 and q cannot be unknown! Please change one of them.")
                a2_q = input("a2 or q: ")
                if a2_q == "a2":
                    self.a2 = input_math("a2: ")
                elif a2_q == "q":
                    self.q = input_math("q: ")
                else:
                    print("Error! Please try again.")

    def sq_n(self):
        while True:
            if self.n != None:  # Troubleshooting
                if self.an != None and self.q != 1:
                    if self.n != infinite_log(self.an/self.a1, self.q)+1:
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
                elif self.an != None and self.q == 1:
                    if self.an != self.a1:
                        print("an has a problem! Please change it.")
                        self.an = input_math("an: ")
                    else:
                        break
                else:
                    self.an = self.a1 * self.q**(self.n-1)
                    break
            elif self.n == None and self.an != None:
                if self.q != 1:
                    self.n = infinite_log(self.an/self.a1, self.q)+1
                    if self.n == int(self.n):
                        self.n = int(self.n)
                        break
                    else:
                        self.n = None
                        print("an has a problem! Please change it.")
                        self.an = input_math("an: ")
                else:
                    print("n has a problem! Please change it.")
                    self.n = input_math("n: ")
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
            if (self.a1*(infinite_power(self.q, index)-1))/(self.q-1) > self.min_sn[0]:
                self.n = index
                break
            index += 1
        while self.min_sn[1] == "<=":
            if (self.a1*(infinite_power(self.q, index)-1))/(self.q-1) >= self.min_sn[0]:
                self.n = index
                break
            index += 1
        while self.min_sn[1] == "=":
            if (self.a1*(infinite_power(self.q, index)-1))/(self.q-1) == self.min_sn[0]:
                self.n = index
                break
            index += 1

    def show(self):
        if self.n == 1:
            return f"Sequence: {self.a1}"
        elif self.n == 2:
            return f"Sequence: {self.a1}, {self.an}"
        elif self.n == 3:
            return f"Sequence: {self.a1}, {self.a1*self.q}, {self.an}"
        elif self.n == 4:
            return f"Sequence: {self.a1}, {self.a1*self.q}, {self.a1*(self.q**2)}, {self.an}"
        elif self.n == 5:
            return f"Sequence: {self.a1}, {self.a1*self.q}, {self.a1*(self.q**2)}, {self.a1*(self.q**3)}, {self.an}"
        elif self.n > 5:
            return f"Sequence: {self.a1}, {self.a1*self.q}, {self.a1*(self.q**2)}, ..., {self.an}"

    def __getitem__(self, word):
        return self.sequence_info.get(word)
