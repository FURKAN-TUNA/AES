sbox = (  # Substitution Box
    0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
    0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
    0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
    0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
    0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
    0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
    0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
    0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
    0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
    0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
    0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
    0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
    0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
    0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
    0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
    0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16,
)

rsbox = (  # Reverse S-Box
    0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB,
    0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB,
    0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E,
    0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25,
    0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92,
    0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84,
    0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06,
    0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B,
    0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73,
    0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E,
    0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B,
    0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4,
    0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F,
    0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF,
    0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61,
    0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D,
)

rcon = (  # Round Constant
    0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1B, 0x36,
    0x6c, 0xd8, 0xab, 0x4d, 0x9a, 0x2f, 0x5e, 0xbc, 0x63, 0xc6,
    0x97, 0x35, 0x6a, 0xd4, 0xb3, 0x7d, 0xfa, 0xef
)


def _MUL02(n):
    return (((n << 1) & (0xFF)) ^ (0x1B if (n & 0x80) else 0x00))


def _MUL03(n):
    return _MUL02(n) ^ n


class aes:  # Advanced Encryption Standard - 128
    def __init__(self, master_key, keysize=128, operation_mode='ECB'):
        self.mk = self.__toarray(master_key)
        self.__key_expansion(self.mk)
        # will be supported
        if operation_mode != 'ECB' or keysize != 128:
            raise ValueError("Oops! It's not supported yet...")
        self.mode = operation_mode
        self.keysize = keysize

    def __toarray(self, ints):
        if type(ints) == list and len(ints) == 16:
            return ints
        arr = [((ints >> (8 * (15 - i))) & 0xFF) for i in range(16)]

        return arr

    def __tobyte(self, arr):
        ints = 0
        for i in range(len(arr)):
            ints += arr[15 - i] * (256 ** i)

        return ints

    def __key_expansion(self, mk):
        self.rk = mk
        for i in range(0, 10):
            self.rk.append(self.rk[(i << 4) + 0] ^ sbox[self.rk[(i << 4) + 13]] ^ rcon[i])
            self.rk.append(self.rk[(i << 4) + 1] ^ sbox[self.rk[(i << 4) + 14]])
            self.rk.append(self.rk[(i << 4) + 2] ^ sbox[self.rk[(i << 4) + 15]])
            self.rk.append(self.rk[(i << 4) + 3] ^ sbox[self.rk[(i << 4) + 12]])
            self.rk.append(self.rk[(i << 4) + 4] ^ self.rk[((i + 1) << 4) + 0])
            self.rk.append(self.rk[(i << 4) + 5] ^ self.rk[((i + 1) << 4) + 1])
            self.rk.append(self.rk[(i << 4) + 6] ^ self.rk[((i + 1) << 4) + 2])
            self.rk.append(self.rk[(i << 4) + 7] ^ self.rk[((i + 1) << 4) + 3])
            self.rk.append(self.rk[(i << 4) + 8] ^ self.rk[((i + 1) << 4) + 4])
            self.rk.append(self.rk[(i << 4) + 9] ^ self.rk[((i + 1) << 4) + 5])
            self.rk.append(self.rk[(i << 4) + 10] ^ self.rk[((i + 1) << 4) + 6])
            self.rk.append(self.rk[(i << 4) + 11] ^ self.rk[((i + 1) << 4) + 7])
            self.rk.append(self.rk[(i << 4) + 12] ^ self.rk[((i + 1) << 4) + 8])
            self.rk.append(self.rk[(i << 4) + 13] ^ self.rk[((i + 1) << 4) + 9])
            self.rk.append(self.rk[(i << 4) + 14] ^ self.rk[((i + 1) << 4) + 10])
            self.rk.append(self.rk[(i << 4) + 15] ^ self.rk[((i + 1) << 4) + 11])

        # return rk

    def encrypt(self, pt, byte=False):
        ct = pt

        self.__addroundkey(ct, self.rk[0:16])

        for i in range(1, 10):
            self.__subbytes(ct)
            self.__shiftrows(ct)
            self.__mixcolumns(ct)
            self.__addroundkey(ct, self.rk[i * 16:(i + 1) * 16])

        self.__subbytes(ct)
        self.__shiftrows(ct)
        self.__addroundkey(ct, self.rk[(i + 1) * 16:(i + 2) * 16])

        if byte:
            return self.__tobyte(ct)

        return ct

    def decrypt(self, ct, byte=False):
        pt = ct

        self.__addroundkey(pt, self.rk[10 * 16:(10 + 1) * 16])
        self.__inv_shiftrows(pt)
        self.__inv_subbytes(pt)

        for i in range(9, 0, -1):
            self.__addroundkey(pt, self.rk[i * 16:(i + 1) * 16])
            self.__inv_mixcolumns(pt)
            self.__inv_shiftrows(pt)
            self.__inv_subbytes(pt)

        self.__addroundkey(pt, self.rk[0:16])

        if byte:
            return self.__tobyte(pt)

        return pt

    def __subbytes(self, s):
        for i in range(16):
            s[i] = sbox[s[i]]

    def __shiftrows(self, s):
        s[1], s[5], s[9], s[13] = s[5], s[9], s[13], s[1]
        s[2], s[6], s[10], s[14] = s[10], s[14], s[2], s[6]
        s[3], s[7], s[11], s[15] = s[15], s[3], s[7], s[11]

    def __mixcolumns(self, s):
        for i in range(4):
            s0 = _MUL02(s[(i << 2) + 0]) ^ _MUL03(s[(i << 2) + 1]) ^ s[(i << 2) + 2] ^ s[(i << 2) + 3]
            s1 = _MUL02(s[(i << 2) + 1]) ^ _MUL03(s[(i << 2) + 2]) ^ s[(i << 2) + 3] ^ s[(i << 2) + 0]
            s2 = _MUL02(s[(i << 2) + 2]) ^ _MUL03(s[(i << 2) + 3]) ^ s[(i << 2) + 0] ^ s[(i << 2) + 1]
            s3 = _MUL02(s[(i << 2) + 3]) ^ _MUL03(s[(i << 2) + 0]) ^ s[(i << 2) + 1] ^ s[(i << 2) + 2]
            s[(i << 2) + 0], s[(i << 2) + 1], s[(i << 2) + 2], s[(i << 2) + 3] = s0, s1, s2, s3

    def __inv_subbytes(self, s):
        for i in range(16):
            s[i] = rsbox[s[i]]

    def __inv_shiftrows(self, s):
        s[1], s[5], s[9], s[13] = s[13], s[1], s[5], s[9]
        s[2], s[6], s[10], s[14] = s[10], s[14], s[2], s[6]
        s[3], s[7], s[11], s[15] = s[7], s[11], s[15], s[3]

    def __inv_mixcolumns(self, s):
        for i in range(4):
            tmp1 = _MUL02(_MUL02(s[(i << 2) + 0] ^ s[(i << 2) + 2]))
            tmp2 = _MUL02(_MUL02(s[(i << 2) + 1] ^ s[(i << 2) + 3]))
            s[(i << 2) + 0] ^= tmp1
            s[(i << 2) + 1] ^= tmp2
            s[(i << 2) + 2] ^= tmp1
            s[(i << 2) + 3] ^= tmp2
        self.__mixcolumns(s)

    def __addroundkey(self, s, k):
        for i in range(16):
            s[i] = s[i] ^ k[i]