# Token types
#
# EOF (end-of-file) token is used to indicate that
# there is no more in put left for lexical analysis
INTERGER, PLUS, MINUS, EOF = 'INTERGER', 'PLUS', 'MINUS', 'EOF'

class Token(object):
    # Object that has a type and a value
    def __init__(self, type, value):
        # token type right now : INTEGER, PLUS, or EOF
        self.type = type
        # token value value : 0, 1 ,2 ,3 ,4, 5, 6, 7, 8, 9, '+', or None
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
        self.current_char = self.text[self.pos]

    def error(self):
        raise  Exception('Error parsing input')

    def advance(self):
        """Advance the 'pos' pointer and set the 'current_char' variable."""
        self.pos +=1
        if self.pos > len(self.text) -1:
            self.current_char = None # Indicates end of input
        else:
            self.current_char = self.text[self.pos]

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def integer(self):
        sum = 0
        list_number = []
        while self.current_char is not None and self.current_char.isdigit():
            list_number.append(int(self.current_char))
            self.advance()

        for x ,y in enumerate(list_number):
            sum += y*10**(len(list_number)-1 -x)
        return sum

    def get_next_token(self):
        """Lexical analyzer(also known as scanner or tokenizer)

        This method is responsible for breaking a sentence apart into tokens.One token at a time.
        """

        while self.current_char is not None:

            if self.current_char.isspace():
                self.skip_whitespace()
                continue



            # if a character is a digit then convert it to integer, create an INTEGER token, increment self.pos
            # index to point to next character after the digit,
            # and return the INTEGER token
            if self.current_char.isdigit():
                return Token(INTERGER, self.integer())

            if self.current_char == '+':
                self.advance()
                return Token(PLUS, '+')

            if self.current_char == '-':
                self.advance()
                return Token(MINUS, self.current_char)

            self.error()
        return Token(EOF, None)

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
        """
        Methdd is responsible for finding and interpreting the expected structure
        expr -> INTEGER PLUS INTEGER"""

        # set current token to the first token taken from the input
        self.current_token = self.get_next_token()

        # we expect the cunrrent token to be a single-digit integer
        left = self.current_token
        self.eat(INTERGER)

        # we expect the current token to be a '+' token
        op = self.current_token
        if op.type == 'PLUS':
            self.eat(PLUS)
        else :
            self.eat(MINUS)

        # we expect the cunrrent token to be a single-digit integer
        right = self.current_token
        self.eat(INTERGER)
        # after the above call the self.current_token is set to
        # EOF token

        # at this point INTEGER PLUS INTEGER sequence of tokens
        # has been succesfully found and method can just
        # return the result of adding two integers, thus
        # effectively interpreting client input
        if op.type == 'PLUS':
            result = left.value + right.value
        else :
            result = left.value - right.value
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
