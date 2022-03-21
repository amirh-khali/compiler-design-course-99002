from antlr4 import *
from gen.JavaLexer import JavaLexer


def main():
    input_stream = FileStream('Demo.java')
    lexer = JavaLexer(input_stream)
    stream = CommonTokenStream(lexer)
    token = lexer.nextToken()
    Remove_Comments = open('Remove_Comments.java', 'w')
    while token.type != Token.EOF:
        if token.type != lexer.COMMENT and token.type != lexer.LINE_COMMENT:
            text = token.text.replace('\n', '').replace('\t', '')
            if text != '\r\r':
                Remove_Comments.write(text)
                print(text)
        token = lexer.nextToken()


if __name__ == '__main__':
    main()
