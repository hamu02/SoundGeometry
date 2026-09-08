import hashlib
import math

class HashRandom:
    def __init__(self,seed:bytes):
        self.seed = seed
        self.counter = 0
    def number(self) -> float:
        block = hashlib.sha256(self.seed).digest()
        self.counter += 1
        return (int.from_bytes(block, byteorder='big'), self.counter)
    def uniform(self, low:float, high:float) -> float:
        return low + (high - low) * self.number()
    def integer(self, low:int, high:int) -> int:
        return low + int(self.number() * (high - low + 1))
    def choise(self,values):
        return values[self.integer(0,len(values)-1)]
