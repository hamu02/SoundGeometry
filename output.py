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
def _generate_svg(daijesuto:bytes,size:int) -> str:
    rng = HashRandom(daijesuto)
    hue = rng.integer(0,359)
    dark =  rng.number()<0.65
    background = f"hsl({hue},25%,{9 if dark else 96}%)"
    palette = [
        f"hsl({(hue + offset) % 360},{rng.integer(55,90)}%,"
        f"{rng.integer(48,76) if dark else rng.integer(25,55)}%)"
        for offset in (0,rng.integer(25,80),rng.integer(130,200),240)
    ]
    svg = [
        '<?xml version="1.0" encoding="utf-8"?>',
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox = "0 0 1000 1000">',
        '<title> Hash_Geometric </title>',
        f'<desc> sha-256:{daijesuto.hex()} </desc>',
        f'<rect width="{size}" height="{size}" fill="{background}"/>',
    ]
    def polygon(cx,cy,radius,sides,angle,color,filled=False):
        points = " ".join(
            f"{cx+radius*math.cos(angle+i*math.tau/sides):.3f},"
            f"{cy+radius*math.sin(angle+i*math.tau/sides):.3f}"
            for i in range(sides)
        )
        svg.append(f'<polygon points="{points}" fill="{color if filled else "none"}" stroke="{color}" stroke-width="{rng.uniform(1,4):.3f}" opacity="{rng.uniform(0.4,0.9):.3f}"/>')
    def circle(cx,cy,radius,color,filled=False):
        svg.append(f'<circle cx="{cx:.3f}" cy="{cy:.3f}" r="{radius:.3f}" fill="{color if filled else "none"}" stroke="{color}" stroke-width="{rng.uniform(1, 4):.3f}" opacity="{rng.uniform(0.4, 0.9):.3f}"/>')
    def line(cx1,cy1,cx2,cy2,color):
        svg.append(f'<line x1="{cx1:.3f}" y1="{cy1:.3f}" x2="{cx2:.3f}" y2="{cy2:.3f}" stroke="{color}" stroke-width="{rng.uniform(1, 4):.3f}" opacity="{rng.uniform(0.4, 0.9):.3f}"/>')
