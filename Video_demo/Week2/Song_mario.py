# -*- coding:UTF-8 -*-

from wave import open 
from struct import Struct
from math import floor

frame_rate = 11025
c_freq, e_freq, g_freq = 261.63, 329.63, 392.00

def encode(x):    
    """
    将x编码为-1和1
    """
    i = int(16384 * x)
    return Struct('h').pack(i)

def play(sampler, name='mario.wav', seconds=2):
    """
    将采样结果输出到wav文件
    """
    out = open(name, 'wb') 
    """
    二进制格式打开，只用于写入。
    如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
    """
    out.setnchannels(1)
    out.setsampwidth(2)
    out.setframerate(frame_rate)
    t = 0 
    while t < seconds * frame_rate :
        sample = sampler(t)
        out.writeframes(encode(sample))
        t = t + 1
    out.close()

def tri(frequency, amplitude=0.3):
    """ 生成连续三角波 """
    period = frame_rate // frequency  ##周期
    def sampler(t):
        saw_wave = t / period - floor(t / period + 0.5)
        tri_wave = 2 * abs(2 * saw_wave) - 1
        return amplitude * tri_wave
    return sampler

def both(f, g):
    """
    两个音节
    """
    return lambda t:f(t) + g(t)
##play(both(tri(c_freq),tri(e_freq)))

def note(f, start, end, fade=0.01 ):
    """
    存在时间
    """
    def sampler(t):
        seconds = t /frame_rate
        if seconds < start:
            return 0
        elif seconds > end:
            return 0
        elif seconds < start + fade:
            return (seconds - start) / fade * f(t)
        elif seconds > end - fade:
            return (end - seconds) /  fade * f(t)
        else:
            return f(t)
    return sampler

c, e = tri(c_freq), tri(e_freq)
g, low_g = tri(g_freq), tri(g_freq /  2)
# play(both(note(c, 0, 1/4 ), note(e, 1/2, 1)))
# play(both(tri(261.63),tri(329.63)))
z = 0
song = note(e, z ,z + 1/8)
z += 1/8
song = both(song, note(e, z, z + 1/8))
z += 1/4
song = both(song, note(e, z, z + 1/8))
z += 1/4
song = both(song, note(c, z, z + 1/8))
z += 1/8
song = both(song, note(e, z, z + 1/8))
z += 1/4
song = both(song, note(g, z, z + 1/4))
z += 1/2
song = both(song, note(low_g, z, z + 1/4))
z += 1/2

play(song)
