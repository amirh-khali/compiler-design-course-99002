from CPP14Lexer import *
from CPP14Parser import *
from CPP14Visitor import *
from antlr4.tree.Trees import Trees

if __name__ == '__main__':
    input_stream = FileStream(sys.argv[1])
    cpplex = CPP14Lexer(input_stream)
    commtokstream = CommonTokenStream(cpplex)
    cpparser = CPP14Parser(commtokstream)

    tree = cpparser.translationunit()
    print(tree.getText())
    print()
    print(Trees.toStringTree(tree, None, cpparser))
