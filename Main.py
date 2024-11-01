from ArithmeticSequence import ASequence
from GeometricSequence import GSequence
from OtherImporters import preloader, input_math

class SC:
    def __init__(self):
        print("Hello, welcome to Sequence calculator!")
        self.starter()

    def starter(self):
        print("\nWhat is the type of sequence you want?", end=" ")
        print("(Arithmetic Sequence) or (Geometric Sequence)")
        type_the_sequence = input("If you choose the desired sequence type, type A or G: ").lower()
        if type_the_sequence == "a":
            self.arithmetic_sequence()
        elif type_the_sequence == "g":
            self.geometric_sequence()
        else:
            print("Error! Please try again.")
            self.starter()

    def sum_of_terms(self):
        print("\nDo you have the sum of the terms in the sequence (minimum sn)? Yes or No")
        sum_of_the_sentences = input("type y or n: ").lower()
        if sum_of_the_sentences == "y":
            return True
        elif sum_of_the_sentences == "n":
            return False
        else:
            print("Error! Please try again.")
            self.sum_of_terms()
    
    def arithmetic_sequence(self):
        s_o_s = self.sum_of_terms()
        if s_o_s:
            self.input_type_sn("a")
        elif not s_o_s:
            print("\nWhich of the following methods would you choose to input the sequence?", end=" ")
            print("(2, 4, 6, ...) or (a1: 2, a2: 4, d: 2, ...)")
            input_the_sequence = input("If you choose the desired method, type 1 or 2: ")
            if input_the_sequence == "1":
                self.input_type_1("a")
            elif input_the_sequence == "2":
                self.input_type_2("a")
            else:
                print("Error! Please try again.")
                self.arithmetic_sequence()

    def geometric_sequence(self):
        s_o_s = self.sum_of_terms()
        if s_o_s:
            self.input_type_sn("g")
        elif not s_o_s:
            print("\nWhich of the following methods would you choose to enter the sequence?", end=" ")
            print("(2, 4, 8, ...) or (a1: 2, a2: 4, q: 2, ...)")
            input_the_sequence = input("If you choose the desired method, type 1 or 2: ")
            if input_the_sequence == "1":
                self.input_type_1("g")
            elif input_the_sequence == "2":
                self.input_type_2("g")
            else:
                print("Error! Please try again.")
                self.geometric_sequence()

    def input_type_1(self, types):
        print("\nRuning the machine:")
        if types == "a":
            sequence_sentences = input(
                "An example of a geometric sequence: 2, 4, 6, ...\n> ").replace(",", " ").split()
            n = input_math("n (number of terms): ", "b")
            index = 0
            for i in sequence_sentences:
                if i.count(".") == 0:
                    sequence_sentences[index] = int(i)
                index += 1
            try:
                a1, a2, *other = sequence_sentences
            except ValueError:
                print("The sequence has a problem!\n")
                self.input_type_1("a")
            an = None
            index = [None, None]
            for x in range(len(other)):
                if type(other[x]) != int:
                    index[0] = x
                elif type(other[x]) == int and len(other) == 1:
                    index[1] = True
                    index[0] = 0
            if index[0] != None:
                if (index[0]) > 0 or index[1] == True:
                    if a2 - a1 != other[0] - a2:
                        print("a2 or a3 has a problem!\n")
                        self.input_type_1("a")
                if len(other) - (index[0]+1) > 0:
                    an = other[-1]
            sequence = ASequence(a1, a2, None, an, n)
            preloader(".", 0.2)
            print(sequence.show())
            print("a1=", sequence["a1"], ", a2=", sequence["a2"], ", d=", sequence["d"],
                  ", an=", sequence["an"], ", n=", sequence["n"], ", sn=", sequence["sn"])
        elif types == "g":
            sequence_sentences = input(
                "An example of a arithmetric sequence: 2, 4, 8, ...\n> ").replace(",", " ").split()
            n = input_math("n (number of terms): ", "b")
            index = 0
            for i in sequence_sentences:
                if i.count(".") == 0:
                    sequence_sentences[index] = int(i)
                index += 1
            try:
                a1, a2, *other = sequence_sentences
            except ValueError:
                print("The sequence has a problem!\n")
                self.input_type_1("g")
            an = None
            index = [None, None]
            for x in range(len(other)):
                if type(other[x]) != int:
                    index[0] = x
                elif type(other[x]) == int and len(other) == 1:
                    index[1] = True
                    index[0] = 0
            if index[0] != None:
                if (index[0]) > 0 or index[1] == True:
                    if a2 / a1 != other[0] / a2:
                        print("a2 or a3 has a problem!\n")
                        self.input_type_1("g")
                if len(other) - (index[0]+1) > 0:
                    an = other[-1]
            sequence = GSequence(a1, a2, None, an, n)
            preloader(".", 0.2)
            print(sequence.show())
            print("a1=", sequence["a1"], ", a2=", sequence["a2"], ", q=", sequence["q"],
                  ", an=", sequence["an"], ", n=", sequence["n"], ", sn=", sequence["sn"])

    def input_type_2(self, types):
        print("\nRuning the machine:")
        if types == "a":
            sequence_dict = {}
            for x in ("a1", "a2", "d", "an", "n"):
                sequence_dict[x] = input_math(f"{x}: ", "b")
                while x == "n" and sequence_dict[x] == 0:
                    print("Error! n cannot be equal to 0. Please change it.")
                    sequence_dict[x] = input_math("n: ", "b")

            sequence = ASequence(sequence_dict["a1"], sequence_dict["a2"],
                                 sequence_dict["d"], sequence_dict["an"], sequence_dict["n"])
            preloader(".", 0.2)
            print(sequence.show())
            print("a1=", sequence["a1"], ", a2=", sequence["a2"], ", d=", sequence["d"],
                  ", an=", sequence["an"], ", n=", sequence["n"], ", sn=", sequence["sn"])
        elif types == "g":
            sequence_dict = {}
            for x in ("a1", "a2", "q", "an", "n"):
                sequence_dict[x] = input_math(f"{x}: ", "b")
                while sequence_dict[x] == 0:
                    print(
                        f"Error! {x} cannot be equal to 0. Please change it.")
                    sequence_dict[x] = input_math(f"{x}: ", "b")

            try:
                sequence = GSequence(sequence_dict["a1"], sequence_dict["a2"],
                                     sequence_dict["q"], sequence_dict["an"], sequence_dict["n"])
            except ValueError:
                print(
                    "Error! n is more than the allowed limit (4506).\nIf q is less than 10, then n is unbounded.")
                self.input_type_2("g")
            preloader(".", 0.2)
            print(sequence.show())
            print("a1=", sequence["a1"], ", a2=", sequence["a2"], ", q=", sequence["q"],
                  ", an=", sequence["an"], ", n=", sequence["n"], ", sn=", sequence["sn"])

    def input_type_sn(self, types):
        print("\nRuning the machine:")
        if types == "a":
            sequence_dict = {}
            for x in ("a1", "a2", "d", "min_sn", "</<=/="):
                if x == "min_sn":
                    sequence_dict[x] = input_math("minimum sn: ")
                elif x == "</<=/=":
                    sequence_dict[x] = input_math(f"{sequence_dict['min_sn']} (< or <= or =) Sn: ", x)
                else:
                    sequence_dict[x] = input_math(f"{x}: ", "b")

            sequence = ASequence(sequence_dict["a1"], sequence_dict["a2"],
                                 sequence_dict["d"], None, None, (sequence_dict["min_sn"], sequence_dict["</<=/="]))
            preloader(".", 0.2)
            print(sequence.show())
            print("a1=", sequence["a1"], ", a2=", sequence["a2"], ", d=", sequence["d"],
                  ", an=", sequence["an"], ", n=", sequence["n"], ", sn=", sequence["sn"])

        elif types == "g":
            sequence_dict = {}
            for x in ("a1", "a2", "q", "min_sn", "</<=/="):
                if x == "min_sn":
                    sequence_dict[x] = input_math("minimum sn: ")
                elif x == "</<=/=":
                    sequence_dict[x] = input_math(f"{sequence_dict['min_sn']} (< or <= or =) Sn: ", x)
                else:
                    sequence_dict[x] = input_math(f"{x}: ", "b")
                    while sequence_dict[x] == 0:
                        print(f"Error! {x} cannot be equal to 0. Please change it.")
                        sequence_dict[x] = input_math(f"{x}: ", "b")

            try:
                sequence = GSequence(sequence_dict["a1"], sequence_dict["a2"],
                                     sequence_dict["q"], None, None, (sequence_dict["min_sn"], sequence_dict["</<=/="]))
            except ValueError:
                print(
                    "Error! n is more than the allowed limit (4506).\nIf q is less than 10, then n is unbounded.")
                self.input_type_2("g")
            preloader(".", 0.2)
            print(sequence.show())
            print("a1=", sequence["a1"], ", a2=", sequence["a2"], ", q=", sequence["q"],
                  ", an=", sequence["an"], ", n=", sequence["n"], ", sn=", sequence["sn"])

while True:
    SC()
    print("\nWould you like to try again? Yes or No")
    if input("type y or n: ").lower() != "y":
        break
