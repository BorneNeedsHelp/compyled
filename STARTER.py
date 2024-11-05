import TOKENS

class STARTER:
    @staticmethod
    def START(CODE):
        tokens = TOKENS.Tokenizer.tokenize(CODE)
        asm = TOKENS.TTATB.tokens_to_assembly(tokens)
        binary = TOKENS.TTATB.tokens_to_binary(tokens)

        return f'Tokens: {tokens}\nASM: {asm}\nBinary: {binary}'
