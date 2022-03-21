from antlr4 import *
from gen.JavaLexer import JavaLexer


def main():
    filename = input()
    input_stream = FileStream(filename + '.java')
    lexer = JavaLexer(input_stream)
    token = lexer.nextToken()
    Remove_Comments = open('New' + filename + '.java', 'w')

    while token.type != Token.EOF:
        if token.type == lexer.LINE_COMMENT:
            Remove_Comments.write(token.text[2:].replace('\n', ''))
        elif token.type == lexer.COMMENT:
            Remove_Comments.write(token.text[2:-2].replace('\n', ''))
        else:
            Remove_Comments.write(token.text.replace('\n', ''))

        token = lexer.nextToken()


if __name__ == '__main__':
    main()
