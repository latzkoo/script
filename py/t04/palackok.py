class Palack(object):
    def __init__(self, ital, max_urtartalom, jelenlegi_urtartalom=1):
        self.ital = ital
        self.max_urtartalom = int(max_urtartalom)
        self._jelenlegi_urtartalom = int(jelenlegi_urtartalom)

    @property
    def jelenlegi_urtartalom(self):
        return self._jelenlegi_urtartalom

    @jelenlegi_urtartalom.setter
    def jelenlegi_urtartalom(self, jelenlegi_urtartalom):

        if jelenlegi_urtartalom > self.max_urtartalom:
            self._jelenlegi_urtartalom = self.max_urtartalom
        else:
            self._jelenlegi_urtartalom = jelenlegi_urtartalom

        if self._jelenlegi_urtartalom == 0:
            self.ital = None

    def suly(self):
        return float(self.max_urtartalom / 35) + float(self._jelenlegi_urtartalom)

    def __eq__(self, other):
        if not isinstance(self, Palack) or not isinstance(other, Palack):
            return False

        if type(self) != type(other):
            return False

        if self.ital == other.ital and self.max_urtartalom == other.max_urtartalom and self.jelenlegi_urtartalom == other.jelenlegi_urtartalom:
            return True
        else:
            return False

    def __iadd__(self, other):
        if type(self) == type(other) and isinstance(self, Palack) and isinstance(other, Palack):
            self.jelenlegi_urtartalom += other.jelenlegi_urtartalom

            if self.ital != other.ital:
                if self.ital is not None and other.ital is not None:
                    self.ital = "keverek"
                elif self.ital is None:
                    self.ital = other.ital

        return self

    def __str__(self):
        return "Palack, benne levo ital: " + str(self.ital) + ", jelenleg " + str(
            self.jelenlegi_urtartalom) + " ml van benne, maximum " + str(self.max_urtartalom) + " ml fer bele."


class VisszavalthatoPalack(Palack):
    def __init__(self, ital, max_urtartalom, jelenlegi_urtartalom=1, palackdij=25):
        super().__init__(ital, max_urtartalom, jelenlegi_urtartalom)
        self.palackdij = int(palackdij)

    def __str__(self):
        return str("Visszavalthato") + Palack.__str__(self)


class Rekesz(object):
    def __init__(self, max_teherbiras):
        self.max_teherbiras = int(max_teherbiras)
        self.palackok = []

    def suly(self):
        if len(self.palackok) == 0:
            return 0

        osszsuly = 0
        for palack in self.palackok:
            osszsuly += palack.suly()

        return osszsuly

    def uj_palack(self, palack):
        if self.suly() + palack.jelenlegi_urtartalom <= self.max_teherbiras:
            self.palackok.append(palack)

    def osszes_penz(self):
        if len(self.palackok) == 0:
            return 0

        penz = 0
        for palack in self.palackok:
            if isinstance(palack, VisszavalthatoPalack):
                penz += int(palack.palackdij)

        return penz