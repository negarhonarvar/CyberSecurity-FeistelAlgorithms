# Feistel-Based Cryptographic Algorithm

### Overview
This project implements a **Feistel-based encryption algorithm**, similar to DES, incorporating some novel ideas from the paper *"An innovative method for enhancing the AES algorithm based on a magic square of order 6"*. The encryption process includes an **initial permutation**, a **Feistel network**, and a **final inverse permutation** to secure data.

### Algorithm Structure
1. **Initial Permutation (IP)**:
   - A permutation is applied to the input block using a table similar to the initial DES permutation.

2. **Feistel Network**:
   - The main encryption is done using a Feistel network, with multiple rounds of XOR, S-box substitution, and a **magic square** transformation for added complexity and reduced execution time.
   - The right half of the block is transformed and combined with the left half through XOR. After each round, the left and right halves are swapped.
   - This process repeats for **16 rounds**, ensuring that the entire data block is thoroughly mixed and dependent on the key.

3. **Magic Square**:
   - The algorithm introduces a **magic square transformation** to replace the MixColumn function in AES, enhancing encryption security and reducing computation time.
   - A **6x6 magic square** is used for nonlinear transformations, further obfuscating the relationship between the plaintext and ciphertext.

4. **Final Permutation (IP-1)**:
   - After the Feistel rounds, a final permutation similar to DES is applied to the output.

### Key Generation
- A **64-bit key** is used, and **subkeys** are generated using **Linear Feedback Shift Registers (LFSR)**. The subkeys are used in each round of the Feistel network.

![image](https://github.com/user-attachments/assets/b2b58ca0-5b5b-45c1-818d-cd85d8a68018)

### Features

![image](https://github.com/user-attachments/assets/b23336a6-4d63-45c7-8265-ad466d89a6c4)

### Architecture

![image](https://github.com/user-attachments/assets/aa9531b1-a8f3-4140-b57c-13da80132f8a)

### Code Implementation
The algorithm's Python implementation can be found in the file **NegarFeistelCipher.py** in the repository. It includes:
- Functions for the initial and final permutation.
- Key generation using LFSR.
- Feistel round processing, including XOR and S-box transformations.
- Magic square processing for nonlinear encryption steps.

### Performance
The proposed algorithm increases security by making linear and differential cryptanalysis more difficult while reducing execution time compared to traditional AES.

This algorithm is particularly efficient for **image encryption**, providing high security while maintaining low execution time.

---






