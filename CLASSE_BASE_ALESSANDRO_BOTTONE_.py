# classe calcolo combinatorio

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

    def charRipetuti(self):
        '''
        questo metodo deve creare un dictionary all'interno del quale la chiave deve essere
        il singolo carattere, il valore deve essere il numero di ripetizioni di quel carattere
        
        esempi di dictionary sono presenti nel file elementi_base/dictionary.py
        '''

    def confUtil(self):
        #qui andiamo a verificare (percorrendo la stringa dalla fine all'inizio eliminando l'ultimo carattere della parola contenuta nella riga del file) se la stringa che prendiamo in considerazione è presente nel file contenente tutte le parole della lingua italiana in quanto ruzzle richiede che le parole abbiano un senso compiuto
        str= "pop"  # nel caso di ruzzle, str deve contenere l'attributo di istanza
        it = 'words.italian.txt' # è possibile aggiungere tante variabili quanti file di lingua si posseggono

        f = open(it, 'r')
        line = f.readline()

        for line in f:  # per ogni riga del file vengono eseguite le righe di codice che seguono
        #    print(str) 
            if str == line[:-1]:  #bisogna eliminare l'ultimo carattere dalla parola contenuta nella riga del file
                print("vero")
        '''
        verificare se la STRINGA attributo di istanza è presente
        nel file word.italian.txt 
        '''
        pass

    def fattoriale(n):
        '''
        implementare una qualunque versione della funzione fattoriale
        '''

    def coeffBinom(n, k):
      P = n!/K!(n-K!)!
        pass

    # PERMUTAZIONI

    def nPermutSenzaRip(self):
        '''
        restituire il numero di permutazioni SENZA ripetizione
        '''
        return  fattoriale(n) 

    def nPermutConRip(self):
        '''
        restituire il numero di permutazioni CON ripetizione
        '''
        return n! / h! k! s!
        # return fattoriale(n) / fattoriale(h) ....

 
    def permutConRip(self):
        '''
        generare e restituire la lista di permutazioni CON ripetizione
        '''
        return 0

    # DISPOSIZIONI

    def nDispSemplSenzaRip(self):
        '''
        restituire il numero di disposizioni semplici SENZA ripetizione
        '''

        return P = n! / (n-k)! 
        # non sa cosa sia il punto esclaamtivo. Devi dichiarare una funzione fattoriale
        # che prende in input n e restituisce il suo fattoriale.
        # se vai più sopra ho scritto anche la dichiarazione, devi implementarla. 


    def nDispSemplConRip(self):
        '''
        restituire il numero di disposizioni semplici CON ripetizione
        '''
        return P = n**k

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
        '''
        restituire il numero delle combinazioni SENZA ripetizione
        '''
        return P = n! / k! (n-k)!

    def nCombSemplConRip(self):
        '''
        restituire il numero delle combinazioni CON ripetizione
        '''
        return P = (n + k - 1)! / k! (n-1)!

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
