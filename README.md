
# RUZZLE

## In questa documentazione:
  - Che cos' è Ruzzle
  - Regole del gioco
  - Cosa abbiamo studiato per progettarlo 
  - La collaborazione con i professori
  - Regole del calcolo combinatorio


### DESCRIZIONE DEL GIOCO
    Ruzzle è un gioco interattivo online, dove, l'utente, che ha la possibilità di salire di livello nel suo percorso di gioco, ha l’obiettivo di 
    trovare, nell'ambito di una partita contro un altro giocatore oppure contro il computer, il maggior numero di parole all'interno di una griglia in 
    un tempo prestabilito. 
    Per giocare a Ruzzle online, sarà necessario possedere oppure, creare, un account Google con cui registrarsi sul gioco per poter salvare tutti i 
    progressi(PUNTI ESPERIENZA CHE FANNO AVANZARE DI LIVELLO) in quanto abbiamo appena affermato che su Ruzzle è possibile avanzare di     
    livello per poter accedere a tornei esclusivi e 
    ottenere eccezionali ricompense.
    All'inizio di ogni partita e quindi di ogni round, appariranno delle lettere all’interno di una griglia che se utilizzate all’interno di una parola     andranno ad aumentare il punteggio di ogni singolo 
    giocatore   che, messo a confronto con quello dell’avversario (o del computer), andrà a determinare la vittoria o la sconfitta del giocatore in ogni     singolo round.
    Ci sara una "schermata home" ad accogliere l'utente, nella schermata home, quest'ultimo potrà scegliere se giocare online (se munito di WI-FI) 
    oppure contro il computer.
    Se sceglierà di giocare online, dovrà attendere un tempo che si aggira intorno ai 10 secondi nei quali avverrà la ricerca di un avversario avente il 
    suo stesso livello oppure un livello simile.
    Naturalmente, è possibile accedere ad un menù impostazioni(anche durante i round) dove si potrà modificare l'intensità del volume, quella degli         effetti sonori, la lingua(non modificabile durante la partita) e altre svariate caratteristiche che renderanno migliore l'esperienza all'interno del 
    gioco.
    
   **I PROGRESSI VENGONO SALVATI?** 
    Ricordiamo che i punti esperienza si ottengono alla fine di ogni partita (se si vince), vengono accumulati e permettono di salire di livello.
    Il livello sarà salvato in modo permanente all'interno del 
    gioco quindi, nel caso in cui il gioco venisse disinstallato, i progressi verrebbero salvati all'interno di esso e, per ripartire dallo stesso           punto, sarà       necessario effettuare nuovamente l'accesso con Google all'interno del gioco.
        
  **QUANTI ROUND CI SONO IN OGNI PARTITA?**
    I round sono 3 e chi alla fine avrà collezionato più punti si aggiudicherà la vittoria.
    
  **COME FUNZIONA IL CONTEGGIO DEI PUNTI?**
    I giocatori accumuleranno punti in base alla quantità di parole trovate e in base alla lunghezza di esse (una parola più lunga e ricercata conferirà 
    al giocatore un punteggio naturalmente più alto rispetto ad una parola semplice dalla breve lunghezza). 
    Ricordiamo inoltre che in RUZZLE, alcune delle lettere presenti nella tabella, avranno un colore del riquadro diverso in quanto potranno svolgere 
    diverse funzioni come quella di conferire più punti ad una parola contenente quella determinata lettera oppure dare un bonus di tempo da sfruttare       per trovare altre parole.
    Alla fine di ogni singolo round, al gocatore apparirà una schermata dove potrà vedere i punti accumulati.
    Ricordiamo che se per caso il giocatore con più punti, volesse abbandonare la partita senza aver effettuato tutti e tre i round, riceverà la metà         dei punti che gli spettano in quanto non è arrivato a conclusione della partita.
    
  **QUANTO TEMPO SI HA A DISPOSIZIONE PER OGNI ROUND?**
    Il giocatore, ha a disposzione 2 minuti e mezzo per ogni round senza considerare la possibile apparizione dei bonus di tempo.
    
  **COME FUNZIONA L'AVANZAMENTO DI LIVELLO?**
    L'utente ha la possibilità di avanzare di livello in quanto ogni partita vinta darà ad esso dei punti mentre ogni partita persa farà rimanere 
    invariato il suo quantitativo di punti.
    Con l'avanzare di livello, l'utente avrà la possibilità di accedere a toreni esclusivi contro altri giocatori che lo porteranno ad ottenere               molteplici ricompense sottoforma di diamanti, monete, ecc... che serviranno nel gioco ad acquistare delle abilità da utilizzare durante i round.
    
  **C'E' UNO SHOP ALL'INTERNO DEL GIOCO?**
    Certo, è presente uno shop all'interno del gioco dove, tramite soldi reali, è possibile acquistare le monete e i diamanti di cui parlavamo prima.

 ### SPIEGAZIONE DEI BLOCCHI DEL DIAGRAMMA DI FLUSSO 
     BLOCCO "INIZIALIZZAZIONE" : è il blocco che indica la creazione di interfaccia di gioco all'inizio di ognuno dei 3 round con conseguente avvio del        countdown del tempo (2.30 min).
     
     BLOCCHI "PUNTEGGIO" E "NESSUN PUNTEGGIO" : sono i blocchi che permettono di tornare all'inizio del ciclo con seguente verifica della disponibilità        di tempo.
     
     BLOCCO "SCHERMATA DI FINE PARTITA" : tramite questo blocco, si creerà un'interfaccia della schermata di fine round dove verrà chiesto ai giocatori        se      vogliono passare al round successivo, in base alla loro risposta, ci sarà o un aggiornamento dei punteggi oppure il calcolo dei punti per        decretare      il vincitore.
     
     BLOCCO "AGGIORNA PUNTEGGI": se i giocatori decidono di passare al prossimo round della partita, verrà effettuato il conteggio dei punti accumulati        durante il round che appariranno ad ogni singolo giocatore come risultato parziale.
     
     BLOCCO "VERIFICA VINCITORE" : se uno dei due giocatori decide di non voler proseguire al prossimo round, avverà il conteggio dei punti per                decretare il vincitore.

 ### CONTESTO
    Quest’anno sempre programmando in Python abbiamo deciso di utilizzare la compresenza in matematica per creare un gioco interattivo,
    abbiamo prima seguito un percorso in matematica con la professoressa Tripepi in cui abbiamo studiato il calcolo combinatorio, ovvero, 
    in quanti modi è possibile disporre una certa quantità di elementi su un determinato quantitativo di posti.
    Abbiamo poi pensato che Ruzzle fosse un ottimo gioco da creare per mettere in pratica lo studio che avevamo effettuato e quindi,
    il nostro obiettivo quest’ anno è quello di collaborare per arrivare al risultato finale:
    ognuno proverà a scrivere delle righe di codice e si prenderanno i migliori codici relativi ad ogni funzione necessaria,
    mettendo tutto insieme riusciremo poi a creare il nostro gioco interattivo.
    Con l’aiuto di GitHub riusciamo a comunicare molto facilmente e a provare a scrivere con l’aiuto del professore il codice in questione.
    Il professor Mazzone ci sta aiutando scrivendo ogni funzione (da modificare naturalmente)  in poche righe di codice in modo da avere tutto piu’           chiaro e poter gestire meglio il codice finale in quanto creato da più pezzi.
    
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
  
  **COME VIENE UTILIZZATO IL CALCOLO COMBINATORIO ALL'INTERNO DEL GIOCO?**
  All'interno del gioco, il calcolo combinatorio è fondamentale per far si che le combinazioni di lettere che si vanno a creare vadano a formare delle 
  parole di senso compiuto tramite la verifica della loro presenza all'interno del dizionario italiano (nel nostro caso).
  Ricordiamo che il dizionario di riferimento cambia in base alla lingua che si sceglie nel menù impostazioni.
  
  
