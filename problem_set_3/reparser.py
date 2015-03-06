REGRAMMAR = grammar("""
RE => alt | seq | null
alt => seq [|] RE | null [|] RE
seq => item seq | item
item => repeat | simple
repeat => simple [*?+]
simple => group | oneof | eol | dot | lit
group => [(] RE [)]
oneof => [[]] [^]]* ] | [[] [^]]+ ]
eol => [$]
dot => [.]
lit => [^|()[]
null => ()
""", whitespace='')

def parse_re(pattern):
    tree, remainder = parse('RE', pattern, REGRAMMAR)
    return (convert(tree) if tree is not None else None), remainder

def convert(tree):
    atom, args = tree[0], tree[1:]
    if atom == 'alt':  return alt(convert(args[0]), convert(args[2]))
    elif atom == 'seq':  return seq(*(convert(x) for x in args))
    elif atom == 'repeat':  return convert_repeat(*args)
    elif atom == 'group':  return convert(args[1])
    elif atom == 'oneof':  return convert_oneof(*args)
    elif atom == 'eol':  return eol
    elif atom == 'dot':  return dot
    elif atom == 'lit':  return lit(args[0])
    elif atom == 'null':  return lit('')
    else:  return convert(args[0])

def convert_repeat(x, op):
    return {'*': star, '?': opt, '+': plus}[op](convert(x))

def convert_oneof(left, chars, right):
    return oneof(']' + chars) if left == '[]' else oneof(chars)