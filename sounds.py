import winsound

def a2():
    playsound(110)  # hz

def b2():
    playsound(123)  # hz

def c3():
    playsound(131)  # hz

def d3():
    playsound(147)  # hz

def e3():
    playsound(165)  # hz

def f3():
    playsound(175)  # hz

def g3():
    playsound(196)  # hz

def playsound(frequency):
    duration = 250  # hz
    freq = frequency
    winsound.Beep(freq, duration)