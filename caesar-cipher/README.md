# Caesar Cipher

The **Caesar Cipher** is one of the simplest and most well-known encryption techniques.  
It is a type of substitution cipher where each letter in the plaintext is shifted a certain number of places down (or up) the alphabet.

For example, with a shift of `3`:
- `A` becomes `D`
- `B` becomes `E`
- `C` becomes `F`

So, the word `HELLO` becomes `KHOOR`.

## How It Works

1. Choose a **shift key** (an integer, like `3`).
2. For each letter in the plaintext:
   - Shift it forward in the alphabet by the key value.
   - Wrap around if needed (e.g., `Z` shifted by 1 becomes `A`).
3. Non-letter characters (like spaces or punctuation) are usually left unchanged.

To **decrypt**, shift letters backward by the same key.

## Example

| Plaintext  | Shift (3) | Ciphertext |
|------------|-----------|------------|
| HELLO      | +3        | KHOOR      |
| WORLD      | +3        | ZRUOG      |

## Notes

- It only works on alphabetic characters.
- It’s considered **weak encryption** by modern standards.
- Good for learning about basic cryptography.


