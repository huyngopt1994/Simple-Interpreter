# Token types
#
# EOF (end-of-file) token is used to indicate that
# there is no more in put left for lexical analysis
INTERGER, PLUS, EOF = 'INTERGER', 'PLUS', 'EOF'

class Token(object):
    def __init__(self, type, value):
        # token type: INTEGER, PLUS, or EOF
        self.type = type
        # token value : 0, 1 ,2 ,3 ,4, 5, 6, 7, 8, 9, '+', or None
        self.value = value

    def __str__(self):
        """String representation of class instance

        Examples:
            Token(Integer, 3)
            Token(Plus '+')
        """

        return 'Token({type}, {value})'.format(
            type=self.type,
            value=repr(self.value)
        )
    def __repr__(self):
        return self.__str__()


class Interpreter(object):
    def __init__(self, text):
        # client string input, e.g "3+5"
        self.text = text
        # self.pos is an index into self.text

        self.pos = 0
        self.current_token = None

    def error(self):
        raise  Exception('Error parsing input')

    def get_next_token(self):
        """Lexical analyzer(also known as scanner or tokenizer

        This method is responsible for breaking a sentence apart into tokens.One token at a time.
        """
        text = self.text
        while True:
            # is self.pos index past in the end of self.text ?
            # if so, please return EOF token because there is no more input left to convert into tokens
            if self.pos > len(text) -1 :
                return Token(EOF, None)

            # get a character at the position self.pos and decide
            # what token to create based on single character

            current_char = text[self.pos]

            # if a character is a digit then convert it to integer, create an INTEGER token, increment self.pos
            # index to point to next character after the digit,
            # and return the INTEGER token
            if current_char.isspace():
                self.pos +=1
            else:
                if current_char.isdigit():
                    token = Token(INTERGER, int(current_char))
                    self.pos +=1
                    return token

                if current_char == '+':
                    token = Token(PLUS, current_char)
                    self.pos += 1
                    return token

                self.error()

    def eat(self, token_type):
        # compare the current token_type with the passed token
        # type and if they match then "eat" the current token
        # and assign the next token to the self.current_token,
        # otherwise raise an exception.

        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()

    def expr(self):
        """expr -> INTEGER PLUS INTEGER"""
        # set current token to the first token taken from the input
        self.current_token = self.get_next_token()

        # we expect the cunrrent token to be a single-digit integer
        left = self.current_token
        self.eat(INTERGER)

        # we expect the current token to be a '+' token
        op = self.current_token
        self.eat(PLUS)

        # we expect the cunrrent token to be a single-digit integer
        right = self.current_token
        self.eat(INTERGER)
        # after the above call the self.current_token is set to
        # EOF token

        # at this point INTEGER PLUS INTEGER sequence of tokens
        # has been succesfully found and method can just
        # return the result of adding two integers, thus
        # effectively interpreting client input
        result = left.value + right.value
        return result

def main():
    while True:
        try:
            # Using input in python 3.
            text = input("huy's calc>")
        except EOFError:
            break
        if not text:
            continue
        interpreter = Interpreter(text)
        result = interpreter.expr()
        print (result)

if __name__ == '__main__':
    main()
