import token

__version__ = '1.0.1'


def plugin(tree, file_tokens):
    try:
        first = file_tokens[0]
    except IndexError:
        return
    if first.type == token.NL:
        yield (
            first.start[0],
            first.start[1],
            'LBL001: Blank line at start of file',
            None
        )


plugin.name = 'flake8-leading-blank-lines'
plugin.version = __version__
