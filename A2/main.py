import ntpath

from examples.utils import get_java_files
from gen.JavaLexer import JavaLexer, CommonTokenStream, ParseTreeWalker
from gen.JavaParserLabeled import JavaParserLabeled, FileStream
from gen.JavaParserLabeledListener import JavaParserLabeledListener


class MyListener(JavaParserLabeledListener):
    def enterClassDeclaration(self, ctx: JavaParserLabeled.ClassDeclarationContext):
        classes.append(ctx.IDENTIFIER().getText())

    def enterMethodDeclaration(self, ctx:JavaParserLabeled.MethodDeclarationContext):
        methods.append(f"{ctx.IDENTIFIER()}")

    def enterVariableDeclarators(self, ctx:JavaParserLabeled.VariableDeclaratorsContext):
        variables.append(ctx.getText().split('=')[0])


test_project_address = '.\\test_project'
for java_file in get_java_files(test_project_address):
    try:
        classes = []
        methods = []
        variables = []

        stream = FileStream(java_file)
        lexer = JavaLexer(stream)
        tokens = CommonTokenStream(lexer)
        parser = JavaParserLabeled(tokens)
        ParseTreeWalker().walk(listener=MyListener(), t=parser.compilationUnit())

        print(f"fileName : {ntpath.basename(java_file)}")
        print(f" - classNames : {classes}")
        print(f" - methodNames : {methods}")
        print(f" - variableNames : {variables}")

    except NameError:
        print(NameError)
