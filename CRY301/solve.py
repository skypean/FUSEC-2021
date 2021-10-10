import gmpy2
import random

def easyone(x):
    assert(x < 2 ** 128)
    x ^= x >> (64 + 19)
    x *= 0xd3856e824d9c8a26aef65c0fe1cc96db
    x &= 0xffffffffffffffffffffffffffffffff #x mod 2**128
    x ^= x >> (64 + 3)
    x *= 0xe44035c8f8387dc11dd3dd67097007cb
    x &= 0xffffffffffffffffffffffffffffffff
    x ^= x >> (64 + 20)
    x *= 0xc9f54782b4f17cb68ecf11d7b378e445
    x &= 0xffffffffffffffffffffffffffffffff
    x ^= x >> (64 + 2)
    return x

def solveeasyone(x):
    x ^= x >> (64 + 2)
    x *= gmpy2.invert(268448390289851351177030176676964262981, 2**128)
    x &= 0xffffffffffffffffffffffffffffffff
    x ^= x >> (64 + 20)
    x *= gmpy2.invert(303397380928069120521467215513016862667, 2**128)
    x &= 0xffffffffffffffffffffffffffffffff
    x ^= x >> (64 + 3)
    x *= gmpy2.invert(281159923981539500379670095774511568603, 2**128)
    x &= 0xffffffffffffffffffffffffffffffff
    x ^= x >> (64 + 19)
    return int(x)


def alittlebitharderone(x):
    assert(x < 2 ** 128)
    x ^= x >> 19
    x *= 0xd3856e824d9c8a26aef65c0fe1cc96db
    x &= 0xffffffffffffffffffffffffffffffff
    x ^= x >> 3
    x *= 0xe44035c8f8387dc11dd3dd67097007cb
    x &= 0xffffffffffffffffffffffffffffffff
    x ^= x >> 20
    x *= 0xc9f54782b4f17cb68ecf11d7b378e445
    x &= 0xffffffffffffffffffffffffffffffff
    x ^= x >> 2
    return x

def xor(a, b):
    return ''.join(str(int(_a) ^ int(_b)) for _a, _b in zip(a, b))

def shiftsolong(x, bitshift):
    x = '{0:b}'.format(x)
    for i in range(0, len(x) - bitshift):
        x = x[:bitshift*(i+1)] + xor(x[bitshift*i:bitshift*(i+1)], x[bitshift*(i+1):bitshift*(i+2)]) + x[bitshift*(i+2):]
    return int(x, 2)

def solvehardone(x):
    x = shiftsolong(x, 2)
    x *= gmpy2.invert(268448390289851351177030176676964262981, 2**128)
    x &= 0xffffffffffffffffffffffffffffffff
    x = shiftsolong(x, 20)
    x *= gmpy2.invert(303397380928069120521467215513016862667, 2**128)
    x &= 0xffffffffffffffffffffffffffffffff
    x = shiftsolong(x, 3)
    x *= gmpy2.invert(281159923981539500379670095774511568603, 2**128)
    x &= 0xffffffffffffffffffffffffffffffff
    x = shiftsolong(x, 19)
    return int(x)

if __name__ == "__main__":
    print(solveeasyone(202661756339499127044586996938357369448))
    print(solvehardone(318509305307585403332815431912214934281))

