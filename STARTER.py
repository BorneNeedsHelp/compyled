import TOKENS

class STARTER:
    @staticmethod
    def START(CODE, read_tokens, read_asm, read_binary):
        tokens = TOKENS.Tokenizer.tokenize(CODE)
        asm = TOKENS.TTATB.tokens_to_assembly(tokens)
        binary = TOKENS.TTATB.tokens_to_binary(tokens)

        if read_tokens:
            print(f'Tokens: {tokens}')

        else:
            return f'Tokens: {tokens}\nASM: {asm}\nBinary: {binary}'

        if read_asm:
            print(f'\nASM: {asm}')

        else:
            return f'Tokens: {tokens}\nASM: {asm}\nBinary: {binary}'

        if read_binary:
            print(f'\nBinary: {binary}')

        else:
            return f'Tokens: {tokens}\nASM: {asm}\nBinary: {binary}'

#PLEASE no one steal!
