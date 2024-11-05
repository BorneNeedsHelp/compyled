class Tokenizer:
    KEYWORDS = {
        'def', 'class', 'if', 'else', 'elif', 'while', 'for', 'return',
        'try', 'except', 'finally', 'print', 'with', 'break', 'continue',
        'pass', 'and', 'or', 'not', 'is', 'in', 'as',
        'True', 'False', 'None'
    }
    OPERATORS = {'+', '-', '*', '/', '%', '**', '//', '=', '+=', '-=', '*=', '/=', '%=', '**=', '//='}
    COMPARISONS = {'==', '!=', '<', '>', '<=', '>='}
    PUNCTUATIONS = {'(', ')', '{', '}', '[', ']', ',', ':', '.', '_', '`'}
    SPECIAL_CHARACTERS = {'~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=',
                          '{', '}', '[', ']', '|', ':', ';', '/', '?', '.', ',', '<', '>', '`'}

    @staticmethod
    def tokenize(input_string):
        tokens = []
        pos = 0
        length = len(input_string)

        while pos < length:
            current_char = input_string[pos]

            if current_char.isspace():
                pos += 1
                continue

            if current_char.isdigit():
                start = pos

                while pos < length and input_string[pos].isdigit():
                    pos += 1
                tokens.append(('NUMBER', input_string[start:pos]))
                continue

            if current_char.isalpha() or current_char == '_' or current_char == '.' or current_char == '`':
                start = pos

                while pos < length and (input_string[pos].isalnum() or input_string[pos] in ['_', '.', '`']):
                    pos += 1
                identifier = input_string[start:pos]

                if identifier in Tokenizer.KEYWORDS:
                    tokens.append(('KEYWORD', identifier))
                else:
                    tokens.append(('IDENTIFIER', identifier))
                continue

            if pos + 1 < length:
                two_char_operator = input_string[pos:pos + 2]
                if two_char_operator in Tokenizer.OPERATORS:
                    tokens.append(('OPERATOR', two_char_operator))
                    pos += 2
                    continue

            if current_char in Tokenizer.OPERATORS:
                tokens.append(('OPERATOR', current_char))
                pos += 1
                continue

            if current_char in Tokenizer.PUNCTUATIONS:
                tokens.append(('PUNCTUATION', current_char))
                pos += 1
                continue

            if current_char in ["'", '"']:
                quote_char = current_char
                start = pos
                pos += 1
                while pos < length and input_string[pos] != quote_char:
                    if input_string[pos] == '\\' and pos + 1 < length and input_string[pos + 1] == quote_char:
                        pos += 2
                    else:
                        pos += 1
                if pos < length:
                    pos += 1
                tokens.append(('STRING', input_string[start:pos]))
                continue

            raise ValueError(f"Unexpected character: {current_char}")

        return tokens


class TTATB:
    @staticmethod
    def tokens_to_assembly(tokens):
        assembly_instructions = []
        register_counter = 0
        current_register = f"R{register_counter}"

        for token in tokens:
            if token[0] == 'NUMBER':
                assembly_instructions.append(f"LOAD {current_register}, {token[1]}")
                register_counter += 1
                current_register = f"R{register_counter}"
            elif token[0] == 'IDENTIFIER':
                assembly_instructions.append(f"LOAD {current_register}, {token[1]}")
                register_counter += 1
                current_register = f"R{register_counter}"
            elif token[0] == 'OPERATOR':
                if token[1] == '+':
                    assembly_instructions.append(f"ADD {current_register}, R{register_counter - 1}")
                elif token[1] == '-':
                    assembly_instructions.append(f"SUB {current_register}, R{register_counter - 1}")
                elif token[1] == '=':
                    assembly_instructions.append(f"MOV R{register_counter - 1}, {current_register}")
            elif token[0] == 'KEYWORD':
                if token[1] == 'print':
                    assembly_instructions.append(f"PRINT {current_register}")

        return assembly_instructions

    @staticmethod
    def assembly_to_binary(assembly_instructions):
        binary_instructions = []

        for instruction in assembly_instructions:
            parts = instruction.split()

            if parts[0] == "LOAD":
                binary_instructions.append("0001 " + ' '.join(parts[1:]))
            elif parts[0] == "ADD":
                binary_instructions.append("0010 " + ' '.join(parts[1:]))
            elif parts[0] == "SUB":
                binary_instructions.append("0011 " + ' '.join(parts[1:]))
            elif parts[0] == "MOV":
                binary_instructions.append("0100 " + ' '.join(parts[1:]))
            elif parts[0] == "PRINT":
                binary_instructions.append("0101 " + ' '.join(parts[1:]))
            else:
                binary_instructions.append("UNKNOWN " + ' '.join(parts[1:]))

        return binary_instructions

    @staticmethod
    def tokens_to_binary(tokens):
        assembly_instructions = TTATB.tokens_to_assembly(tokens)
        binary_instructions = TTATB.assembly_to_binary(assembly_instructions)
        return binary_instructions

#PLEASE no one steal!
