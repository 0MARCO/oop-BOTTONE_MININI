
# RUZZLE

## In questa documentazione:
  - Che cos' è Ruzzle
  - Regole del gioco
  - Cosa abbiamo studiato per progettarlo 
  - La collaborazione con i professori
  - Regole del calcolo combinatorio


### DESCRIZIONE DEL GIOCO
    Ruzzle è un gioco interattivo online, dove, l'utente, che ha la possibilità di salire di livello nel suo percorso di gioco, ha l’obiettivo di 
    trovare, nell'ambito di una partita contro un altro giocatopre oppure contro il computer, il maggior numero di parole all'interno di una griglia in 
    un 
    tempo      
    prestabilito, 
    appariranno delle lettere all’interno della griglia che se utilizzate all’interno di una parola andranno ad aumentare il punteggio di ogni singolo 
    giocatore   
    che, messo a confronto con quello dell’avversario (o del computer), andrà a determinare la vittoria o la sconfitta del giocatore in ogni singolo 
    round.
    
    Ci sara una "schermata home" ad accogliere l'utente, nella schermata home, quest'ultimo potrà scegliere se giocare online (se munito di WI-FI) oppure 
    contro il computer.
    Se sceglierà di giocare online, dovrà attendere un tempo che si aggira intorno ai 10 secondi nei quali avverrà la ricerca di un avversario avente il 
    suo stesso livello oppure un livello simile
    
  **QUANTI ROUND CI SONO IN OGNI PARTITA?**
    I round sono 3 e chi alla fine avrà collezionato più punti si aggiudicherà la vittoria.
    
  **COME FUNZIONA IL CONTEGGIO DEI PUNTI?**
    I giocatori accumuleranno punti in base alla quantita di parole trovate e in base alla lunghezza di esse (una parola più lunga e ricercata conferirà 
    al giocatore un punteggio naturalmente più alto rispetto ad una parola semplice dalla breve lunghezza). 
    Ricordiamo inoltre che in RUZZLE, alcune delle lettere presenti nella tabella, avranno un colore del riquadro diverso in quanto potranno svolgere 
    diverse funzioni come quella di conferire più punti ad una parola contenente quella determinata lettera oppure dare un bonus di tempo da sfruttare       per trovare altre parole.
    Alla fine di ogni singolo round, al gocatore apparirà una schermata dove potrà vedere i punti accumulati.
    
  **QUANTO TEMPO SI HA A DISPOSIZIONE PER OGNI ROUND?**
    Il giocatore, ha a disposzione 2 minuti e mezzo per ogni round senza considerare la possibile apparizione dei bonus di tempo.
    
  **COME FUNZIONA L'AVANZAMENTO DI LIVELLO?**
    L'utente ha la possibilità di 
    avanzare       
    di livello in quanto ogni partita vinta darà ad esso dei punti mentre ogni partita persa farà rimanere invariato il suo quantitativo di punti.
    Con l'avanzare di livello, l'utente avrà la possibilità di accedere a toreni esclusivi contro altri giocatori che lo porteranno ad ottenere               molteplici ricompense sottoforma di diamanti, monete, ecc... che serviranno nel gioco ad acquistare delle abilità da utilizzare durante i round.
    
  **C'E' UNO SHOP ALL'INTERNO DEL GIOCO?**
    Certo, e' presente uno shop all'interno del gioco dove, tramite soldi reali, è possibile acquistare le monete e i diamanti di cui parlavamo prima.

 ### SPIEGAZIONE DEI BLOCCHI DEL DIAGRAMMA DI FLUSSO 
     BLOCCO "INIZIALIZZAZIONE": è il blocco che indica la creazione di interfaccia di gioco all'inizio di ognuno dei 3 round con conseguente avvio del          countdown del tempo (2.30 min).
     BLOCCHI "PUNTEGGIO" E "NESSUN PUNTEGGIO": sono i blocchi che permettono di tornare all'inizio del ciclo con seguente verifica della disponibilità di 
     tempo.
     

 ### CONTESTO
    Quest’anno sempre programmando in Python abbiamo deciso di utilizzare la compresenza in matematica per creare un gioco interattivo,
    abbiamo prima seguito un percorso in matematica con la professoressa Tripepi in cui abbiamo studiato il calcolo combinatorio, ovvero, 
    in quanti modi è possibile disporre una certa quantità di elementi su un determinato quantitativo di posti.
    Abbiamo poi pensato che Ruzzle fosse un ottimo gioco da creare per mettere in pratica lo studio che avevamo effettuato e quindi,
    il nostro obiettivo quest’ anno è quello di collaborare per arrivare al risultato finale:
    ognuno proverà a scrivere delle righe di codice e si prenderanno i migliori codici relativi ad ogni funzione necessaria,
    mettendo tutto insieme riusciremo poi a creare il nostro gioco interattivo.
    Con l’aiuto di GitHub riusciamo a comunicare molto facilmente e a provare a scrivere con l’aiuto del professore il codice in questione.
    Il professor Mazzone ci sta aiutando scrivendo ogni funzione (da modificare naturalmente)  in poche righe di codice in modo da avere tutto piu’ chiaro e        
    poter gestire meglio il codice finale in quanto creato da più pezzi.
    
  ### REGOLE CALCOLO COMBINATORIO
  ![Image text](https://www.studenti.it/images/matematica/pictures/4131fo/images/FO.4.13.1_9817.png)
   
  Il **CALCOLO COMBINATORIO** è, in matematica, ciò che ci consente di determinare in quanti e in quali modi è possibile ordinare o raggruppare un determinato     numero di elementi su un determinato numero di posti.
  
  Il calcolo combinatorio è un tipo di calcolo che comprende vari metodi tra i quali:
  
  - **PERMUTAZIONI SEMPLICI E PERMUTAZIONI CON RIPETIZIONE**
  
     - Le PERMUTAZIONI SEMPLICI di "n" elementi distinti, sono tutti i gruppi formati dagli "n" elementi, che differiscono per il loro ORDINE.
     
     - Le PERMUTAZIONI CON RIPETIZIONE di "n" elementi distinti, sono tutti i gruppi formati dagli "n" elementi, ALCUNI RIPETUTI, che                                    differiscono per il loro ORDINE.
    
  - **DISPOSIZIONI SEMPLICI e DISPOSIZIONI CON RIPETIZIONE**
  
     - Le DISPOSIZIONI SEMPLICI di "n" elementi su "k" posti, sono  tutti i gruppi di "k" elementi scelti tra gli "n" che si differenziano per ALMENO un        elemento o per l'ordine con cui gli elementi sono disposti.
     
     - LE DISPOSIZIONI CON RIPETIZIONE di "n" elementi su "k" posti, sono tutti i gruppi di "k" elementi,ALCUNI RIPETUTI, scelti fra gli "n" che si        differenziano per ALMENO un elemento o per l'ordine con cui gli elementi sono disposti.
     
  - **COMBINAZIONI SEMPLICI E COMBINAZIONI CON RIPETIZIONE**
  
      - Le COMBINAZIONI SEMPLICI di "n" elementi su "k" posti, sono tutti i gruppi di "k" elementi scelti tra gli "n" che differiscono per almeno un         elemento E NON PER L'ORDINE.
     
     - Le COMBINAZIONI CON RIPETIZIONE di "n" elementi su "k" posti, sono tutti i gruppi di "k" elementi scelti tra gli "n", ALCUNI RIPETUTI, che              differiscono per almeno un elemento E NON PER L'ORDINE. 
  
