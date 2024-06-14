# Constants
BLOCK_SIZE = 64  # Block size in bits
KEY_SIZE = 64    # Key size in bits
NUM_ROUNDS = 16   # Number of rounds
HALF_BLOCK_SIZE = BLOCK_SIZE // 2  # Size of half the block

INITIAL_PERMUTATION = [i - 1 for i in [
    57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4,
    63, 55, 47, 39, 31, 23, 15, 7, 58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8
]]

FINAL_PERMUTATION = [i - 1 for i in [
    40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25
]]


S_BOX =  [
        [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
         [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
         [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
         [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],

        [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
         [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
         [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
         [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],

        [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
         [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
         [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
         [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],

        [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
         [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
         [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
         [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],

        [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
         [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
         [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
         [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],

        [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
         [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
         [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
         [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],

        [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
         [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
         [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
         [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],

        [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
         [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
         [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
         [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]
    ]


PC1 = [56, 48, 40, 32, 24, 16, 8, 0, 57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26,
       18, 10, 2, 59, 51, 43, 35, 62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37, 29,
       21, 13, 5, 60, 52, 44, 36, 28, 20, 12, 4, 27, 19, 11, 3]


PC2 = [13, 16, 10, 23, 0, 4, 2, 27, 14, 5, 20, 9, 22, 18, 11, 3, 25, 7, 15, 6, 26, 19, 12, 1,
       40, 51, 30, 36, 46, 54, 29, 39, 50, 44, 32, 47, 43, 48, 38, 55, 33, 52, 45, 41, 49, 35, 28, 31]

MAGIC_SQUARE = [[(i + j) % 32 for j in range(6)] for i in range(6)]
EXPANSION_FUNCTION = list(range(HALF_BLOCK_SIZE))


def apply_permutation(block, permutation):

    return ''.join(block[i] for i in permutation)


def expand(block):

    expanded_block = "".join(block[i // 2] for i in range(48))
    #print("Expanded block size:", len(expanded_block))
    return expanded_block


def s_box_transform(block):
    output = []
    for i in range(0, len(block), 6):
        bits = block[i:i+6]
        row = int(bits[0] + bits[5], 2)
        column = int(bits[1:5], 2)
        s_box_index = (i // 6) % len(S_BOX)
        s_box_value = S_BOX[s_box_index][row][column]
        output.append(format(s_box_value, '04b'))
    result = ''.join(output)
    #print("S-Box output size:", len(result))  # Debug: Check size
    return result


def magic_square_transform(block):

    transformed = []
    MAGIC_SQUARE = [i % 32 for i in range(32)]

    for i in MAGIC_SQUARE:
        transformed.append(block[i])
    result = ''.join(transformed)
    #print("Magic Square output size:", len(result))
    return result


def xor(a, b):
    assert len(a) == len(b), f"Length mismatch: {len(a)} vs {len(b)}"
    return ''.join('1' if x != y else '0' for x, y in zip(a, b))


def round_function(right, subkey):
    expanded_right = expand(right)
    xored = xor(expanded_right, subkey)
    substituted = s_box_transform(xored)
    result = magic_square_transform(substituted)
    print("Round function output :", result)
    return result


def generate_subkeys(key):
    key = apply_permutation(key, PC1)
    C, D = key[:28], key[28:]
    subkeys = []
    shifts = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
    for shift in shifts:
        C = C[shift:] + C[:shift]
        D = D[shift:] + D[:shift]
        combined = C + D
        subkeys.append(apply_permutation(combined, PC2))
    return subkeys


def feistel_cipher(plaintext, subkeys):
    left, right = plaintext[:HALF_BLOCK_SIZE], plaintext[HALF_BLOCK_SIZE:]
    for subkey in subkeys:
        new_left = right
        right = xor(left, round_function(right, subkey))
        left = new_left
    return left + right


def encrypt(plaintext, key):

    plaintext = apply_permutation(plaintext, INITIAL_PERMUTATION)
    subkeys = generate_subkeys(key)
    ciphertext = feistel_cipher(plaintext, subkeys)
    ciphertext = apply_permutation(ciphertext, FINAL_PERMUTATION)
    return ciphertext

# Example usage

key = "0110001001100101011010000110010101110011011010000111010001101001"
plaintext = "0110100001101111011011100110000101110010011101100110000101110010"

encrypted_text = encrypt(plaintext, key)
print("Encrypted output:", encrypted_text)
