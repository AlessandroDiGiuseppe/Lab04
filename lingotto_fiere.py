from stand import Stand
from stand_prese_extra import StandPreseExtra
from stand_premium import StandPremium
from espositore import Espositore

class LingottoFiere:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        # TODO
        self._nome = nome
        self.stand = {}
        self.espositori = {}

    """Aggiungere setter e getter se necessari"""
    # TODO
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self,nome):
        self._nome = nome

    def carica_file_dati(self, file_path):
        """Carica i dati (stand ed espositori) dal file"""
        # TODO
        try:
            with open(file_path,"r", encoding = 'utf-8') as f:
                righe = f.readlines()
        except FileNotFoundError as e:
            print(e)

        for riga in righe:
            riga = riga.strip()
            if riga == "":
                continue

            campi = riga.strip().split(",")
            codice = campi[0].upper()

            if codice[0] == "S":
                if len(campi) == 4:
                    self.stand[codice] = Stand(codice,campi[1],campi[2],campi[3])

                elif len(campi)==5:
                    valore_aggiuntivo = campi[4]
                    if valore_aggiuntivo.isdigit():
                        self.stand[codice] = StandPreseExtra(codice,campi[1],campi[2],campi[3],campi[4])
                    else:
                        self.stand[codice] = StandPremium(codice, campi[1], campi[2], campi[3], campi[4])

            if codice[0] == "E":
                self.espositori[codice]=Espositore(codice,campi[1],campi[2])

    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""
        # TODO
        if codice_stand not in self.stand:
            raise ValueError(f"Il codice dello stand non esiste")

        if codice_espositore not in self.espositori:
            raise ValueError(f"Espositore non presente")

        stand = self.stand[codice_stand]
        espositore = self.espositori[codice_espositore]
        if not stand.disponibile:
            raise ValueError(f"Lo stand {codice_stand} è già occupato")

        for s in self.stand.values():
            if s.espositore_assegnato == espositore:
                raise ValueError(f"L'espositore {codice_espositore} ha già uno stand ({s.codice})")

        stand.espositore_assegnato = espositore

    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        # TODO
        if not self.espositori:
            print("Nessun espositore presente nel sistema")
            return

        for esp in self.espositori.values():
            stand_associato = None
            for s in self.stand.values():
                if s.espositore_assegnato == esp:
                    stand_associato = s.codice
                    break

            info_stand = f"-Stand associato: {stand_associato}" if stand_associato else "Nessuno stand associato"
            print(f"{esp}{info_stand}")

    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        # TODO
        return sorted(self.stand.values())