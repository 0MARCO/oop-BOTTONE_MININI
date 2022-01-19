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
        


    def confUtil(self):

        pass


    def fattoriale(n):
        if n < 2:
          return 1
      else:
          return n * fattoriale(n-1)
      
    def coeffBinom(n, k):
       P = fattoriale(n)/fattoriale(K) * fattoriale(n-fattoriale(K))    
       return (P)
     

    # PERMUTAZIONI

    def nPermutSenzaRip(self):
        calcComb.fattoriale(self.n)
        return fattoriale(n)
     

    def nPermutConRip(self):
         calcComb.fattoriale(self.n)
        return fattoriale(n) / fattoriale(h) * fattoriale(k) * fattoriale(s)
     
 
    def permutConRip(self):
        
        pass
     
    # DISPOSIZIONI

    def nDispSemplSenzaRip(self):
        calcComb.fattoriale(self.n)
        return fattoriale(n) / fattoriale(n-k)
        

    def nDispSemplConRip(self):
        P = n**k
        return P         
    
    def dispSemplSenzaRip(self):
        
        pass


    def dispSemplConRip(self):
        
       pass

    # COMBINAZIONI

    def nCombSemplSenzaRip(self):
        calcComb.fattoriale(self.n)
        return fattoriale(n) / fattoriale(k) * fattoriale(n-k)
       

    def nCombSemplConRip(self):
          calcComb.fattoriale(self.n)
        return fattoriale(n + k - 1) / fattoriale(k) * fattoriale(n-1)
       
    def combSenzaRip(self):
        
        pass
    
    def combConRip(self):
        
        pass
     
  


