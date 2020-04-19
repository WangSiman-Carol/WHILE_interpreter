
###############################################################################
#                                                                             #
#  INTERPRETER                                                                #
#                                                                             #
###############################################################################

from collections import OrderedDict

class Interpreter():
    def __init__(self, parser):
        self.parser = parser
        self.state = {}

    def interp(self, tree):
        op = tree.data

        # Binary operations
        if op in {"add", "mul", "sub", "div", "power"}:
            lhs = self.interp(tree.children[0])
            rhs = self.interp(tree.children[1])
            if op == 'add':
                return lhs + rhs
            elif op == 'sub':
                return lhs - rhs
            elif op == 'mul':
                return lhs * rhs
            elif op == 'div':
                return lhs / rhs
            elif op == "power":
                return lhs ** rhs
        # visit number
        elif op == "number":
            return int(tree.children[0])
        # visit variable
        elif op == "var":
            return self.lookup(tree.children[0])
        # var assignment
        elif op == "assign":
            variable = tree.children[0].children[0]
            value = self.interp(tree.children[1])
            self.state[variable] = value
                # comparison
        elif op == "comparison":
            lhs = self.interp(tree.children[0])
            relation = tree.children[1]
            rhs = self.interp(tree.children[2])
            return self.compare(lhs, relation, rhs)
        # while statement
        elif op == "while_stmt":
            cond = self.interp(tree.children[0])
            if cond:
                self.interp(tree.children[1])
                self.interp(tree)
            else:
                return
        # if statement
        elif op == "if_stmt":
            children_num = len(tree.children)
            cond = self.interp(tree.children[0])
            if cond:
                self.interp(tree.children[1])
            elif not cond and children_num == 3:
                self.interp(tree.children[2])
            return 
        # skip statement
        elif op == "skip_stmt":
            return 
        # simple statement
        elif op == "simple_stmt":
            self.interp(tree.children[0])
            self.interp(tree.children[1])
            return
        # not
        elif op == "not":
            return -1 * self.interp(tree.children[0])
        # const_false
        elif op == "const_false":
            return 0
        elif op == "const_true":
            return 1
        elif op == "or_test":
            lhs = self.interp(tree.children[0])
            rhs = self.interp(tree.children[1])
            return lhs or rhs
        elif op == "and_test":
            lhs = self.interp(tree.children[0])
            rhs = self.interp(tree.children[1])
            return lhs and rhs


    def compare(self, left, relation, right):
        if relation == "=":
            return left == right
        elif relation == "<":
            return left < right
        elif relation == ">":
            return left > right

    def lookup(self, v):
        if v in self.state:
            return self.state[v]
        else:
            return 0
    
    def print_Result(self):
        od = OrderedDict(sorted(self.state.items()))
        ans = ",".join(str(var) + " → " + str(value) for var, value in od.items())
        return "{" + ans + "}"

    def interpret(self, text):
        tree = self.parser.parse(text)
        self.interp(tree)
        return self.print_Result()


