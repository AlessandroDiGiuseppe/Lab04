class Stand:
    def __init__(self,codice,superficie,padiglione,prezzo_base):
        self.codice = codice
        self.superficie = float(superficie)
        self.padiglione = int(padiglione)
        self.prezzo_base = float(prezzo_base)
        self.espositore_assegnato = None

    @property
    def disponibile(self):
         return self.espositore_assegnato is None

    def calcola_prezzo(self):
        return self.prezzo_base

    def __lt__(self, other):
        if not isinstance(other,Stand):
            return NotImplemented
        return self.calcola_prezzo()<other.calcola_prezzo()

    def __str__(self):
        stato = "Disponibile" if self.disponibile else f"Assegnato a {self.espositore_assegnato.codice}"
        return f"{self.codice}: Standard | {self.superficie} mq - padiglione: {self.padiglione} - Prezzo: {self.calcola_prezzo():.2f} euro - {stato}"



