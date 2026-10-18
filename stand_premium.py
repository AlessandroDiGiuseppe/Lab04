from stand import Stand
class StandPremium(Stand):
    def __init__(self,codice,superficie,padiglione,prezzo_base,posizione):
        super().__init__(codice,superficie, padiglione, prezzo_base)
        self.posizione = posizione

    def calcola_prezzo(self):
        return self.prezzo_base*1.30

    def __str__(self):
        stato = "Disponibile" if self.disponibile else f"Assegnato a {self.espositore_assegnato.codice}"
        return f"{self.codice}: Stand Premium | {self.superficie} mq -padiglione: {self.padiglione} -prezzo {self.calcola_prezzo():.2f}€ -posizione: {self.posizione} -{stato}"