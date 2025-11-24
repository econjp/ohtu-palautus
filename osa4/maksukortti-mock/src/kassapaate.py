HINTA = 5


class Kassapaate:
    def __init__(self):
        self.myytyja_lounaita = 0

    def lataa(self, kortti, summa):
        # ladataan vain jos summa on positiivinen
        if summa > 0:
            kortti.lataa(summa)

    def osta_lounas(self, kortti):
        # veloitetaan vain jos kortilla on tarpeeksi rahaa
        if kortti.saldo >= HINTA:
            kortti.osta(HINTA)
            self.myytyja_lounaita = self.myytyja_lounaita + 1
