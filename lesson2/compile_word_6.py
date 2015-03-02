# --------------
# User Instructions
#
# Write a function, compile_word(word), that compiles a word
# of UPPERCASE letters as numeric digits. For example:
# compile_word('YOU') => '(1*U + 10*O +100*Y)' 
# Non-uppercase words should remain unchaged.

def compile_word(word):
    if word.isupper():
        terminos = [('%s*%s' % (10**i,d))
               for (i,d) in enumerate(word[::-1])]
        return '('+ '+'.join(terminos)+')'
    else:
        return word
    # Your code here.
    
print compile_word('HOLA == HELL**O')