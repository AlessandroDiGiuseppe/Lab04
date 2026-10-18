from stand import Stand
class StandPreseExtra(Stand):
    def __init__(self,codice,superficie,padiglione,prezzo_base,numero_prese):
        super().__init__(codice, superficie, padiglione, prezzo_base)
        self.numero_prese = int(numero_prese)

    def calcola_prezzo(self):
        return self.prezzo_base*(1 + 0.07 * self.numero_prese)

    def __str__(self):
        stato = "Disponibile" if self.disponibile else f"Assegnato a {self.espositore_assegnato.codice}"
        return f"{self.codice}: Prese extra | {self.superficie} mq - padiglione: {self.padiglione} - Prezzo: {self.calcola_prezzo():.2f} euro -Numero prese extra: {self.numero_prese}- {stato}"

