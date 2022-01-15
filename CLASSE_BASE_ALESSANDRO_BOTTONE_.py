# classe calcolo combinatorio
import math
math.fattoriale(1000)
class calcComb():

    def __init__(self, stringa):

        self.__N = len(stringa)
        self.__stringa = stringa
        self.__listStringa = list(stringa)

    def get_stringa(self):
        return self.__stringa

    def get_listStringa(self):
        return self.__listStringa

    def setStringa(self):
        
        self.__stringa = str 
        
        return self.__stringa



    def cerca(str):
        str= self.__stringa = stringa  
        it = 'words.italian.txt' # è possibile aggiungere tante variabili quanti file di lingua si posseggono

        f = open(it, 'r')
        line = f.readline()

        for line in f:  # per ogni riga del file vengono eseguite le righe di codice che seguono
            print(str) 
            if str == line[:-1]:  #bisogna eliminare l'ultimo carattere dalla parola contenuta nella riga del file
                return("vero")
        '''
        verificare se la STRINGA attributo di istanza è presente
        nel file word.italian.txt 
        '''



    def charRipetuti(self):
        pass
        '''
        questo metodo deve creare un dictionary all'interno del quale la chiave deve essere
        il singolo carattere, il valore deve essere il numero di ripetizioni di quel carattere
        
        esempi di dictionary sono presenti nel file elementi_base/dictionary.py
        '''

    ############################CORREZIONE#####################################
    '''
    confUtil sta per configurazioni utili. Vuol dire che a partire  dalla stringa iniziale
    deve trovare tutte le configurazioni utili, cioè tra tutte le configurazioni quelle che 
    effettivamente hanno un senso compiuto. Dentro invece avete copiato solo il codice della funzione cerca.

    Prima invece bisogna creare la lista di tutte le possibili configurazioni, dopo cercarle una ad una
    dentro il file della lingua italiana.

    '''

    def confUtil(self):

        pass


    def fattoriale(n):
        if n < 2:
          return 1
      else:
          return n * fattoriale(n-1)
        '''
        implementare una qualunque versione della funzione fattoriale
        '''
        pass

    def coeffBinom(n, k):
       P = fattoriale(n)/fattoriale(K) * fattoriale(n-fattoriale(K)) #per richiamare il fattoriale non puoi procedere con l'esclamativo,
      # ma richiamare la funzione fattoriale che però non vedo implementata da nessuna parte
        return (P)
        pass

    # PERMUTAZIONI

    def nPermutSenzaRip(self):
        calcComb.fattoriale(self.n)
        return fattoriale(n)
        '''
        restituire il numero di permutazioni SENZA ripetizione
        '''
        return  fattoriale(n) 

    def nPermutConRip(self):
         calcComb.fattoriale(self.n)
        return fattoriale(n) / fattoriale(h) * fattoriale(k) * fattoriale(s)
        '''
        restituire il numero di permutazioni CON ripetizione
        '''
        #return n! / h! k! s! stesso errore di prima, tra l'altro se leggete
            #il commento che avevo fatto (sotto questo rigo) avevo anche indicato cosa bisognava
            #restituire
        # return fattoriale(n) / fattoriale(h) ....

 
    def permutConRip(self):
        '''
        generare e restituire la lista di permutazioni CON ripetizione
        '''
        return 0

    # DISPOSIZIONI

    def nDispSemplSenzaRip(self):
        calcComb.fattoriale(self.n)
        return P = fattoriale(n) / fattoriale(n-k)
        '''
        restituire il numero di disposizioni semplici SENZA ripetizione
        '''

        #return P = n! / (n-k)! 
        # non sa cosa sia il punto esclaamtivo. Devi dichiarare una funzione fattoriale
        # che prende in input n e restituisce il suo fattoriale.
        # se vai più sopra ho scritto anche la dichiarazione, devi implementarla. 


    def nDispSemplConRip(self):
        '''
        restituire il numero di disposizioni semplici CON ripetizione
        '''
        P = n**k
        return '='  # in return non puoi scrivere anche "=" 

    def dispSemplSenzaRip(self):
        '''
        generare e restituire la lista delle disposizioni semplici SENZA ripetizione
        '''
        return 0


    def dispSemplConRip(self):
        '''
        generare e restituire la lista delle disposizioni semplici CON ripetizione
        '''
        return 0

    # COMBINAZIONI

    def nCombSemplSenzaRip(self):
        calcComb.fattoriale(self.n)
        return fattoriale(n) / fattoriale(k) * fattoriale(n-k)
        '''
        restituire il numero delle combinazioni SENZA ripetizione
        '''
         # dopo aver implementato la funzione leva il pass
        # return P = n! / k! (n-k)!  # leggi sopra

    def nCombSemplConRip(self):
          calcComb.fattoriale(self.n)
        return fattoriale(n + k - 1) / fattoriale(k) * fattoriale(n-1)
        '''
        restituire il numero delle combinazioni CON ripetizione
        '''
        #return P = (n + k - 1)! / k! (n-1)!
        pass # dopo aver implementato la funzione leva il pass

    def combSenzaRip(self):
        '''
        generare e restituire la lista delle combinazioni SENZA ripetizione
        '''
        return 0


    def combConRip(self):
        '''
        generare e restituire la lista delle combinazioni CON ripetizione
        '''
        return 0


