grammar Q2;

start:
    Str EOF;
    Str:
        (('c'?)'bbb')
        | ('bbb'('c'?))
        |('bbbb')
        ;