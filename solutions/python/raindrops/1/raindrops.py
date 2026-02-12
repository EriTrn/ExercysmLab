def convert(number):
    sounds = [(3, "Pling"), (5, "Plang"), (7, "Plong")]
    res = "".join(sound for factor, sound in sounds if number % factor == 0)
    return res or str(number)