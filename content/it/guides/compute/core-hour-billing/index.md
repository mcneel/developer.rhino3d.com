+++
aliases = ["/en/5/guides/compute/core-hour-billing/", "/en/6/guides/compute/core-hour-billing/", "/en/7/guides/compute/core-hour-billing/", "/en/wip/guides/compute/core-hour-billing/"]
authors = [ "brian" ]
categories = [ "Deployment" ]
keywords = [ "developer", "compute", "core-hour" ]
languages = []
sdk = [ "Compute" ]
title = "Licenze e fatturazione"
type = "guides"
weight = 1

[admin]
TODO = ""
origin = "http://www.grasshopper3d.com/forum/topics/how-do-i-install-a-custom-ghx"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

[page_options]
byline = true
toc = true
toc_type = "single"
+++


## Informazioni sulla fatturazione nucleo per ora.

Quando Rhino è collegato a un account di servizio e viene eseguito su un sistema operativo basato su server di Windows, verranno fatturati **0,10$ per nucleo all'ora** su cui Rhino è in esecuzione (distribuiti proporzionalmente per minuto).

***Esempio 1:** Rhino in esecuzione su un server a 32 nuclei per un'ora:*

  * * 1 computer * 32 nuclei * 1 ora * 0,10$/nucleo-ora = 3,20$.

***Esempio 2:** Rhino in esecuzione su 200 server a 4 nuclei per 6 minuti:*

  * * 200 computer * 4 nuclei * 0,1 ora * 0,10$/nucleo-ora = 8,00$.

***Esempio 3:** 1 istanza di Rhino in esecuzione su un server a 2 nuclei 8 ore al giorno per 30 giorni:*
  * 1 computer * 2 nuclei * 8 ore/giorno * 30 giorni/mese * $0,10/core-ora = $48/mese.

***Esempio 4:** 10 istanze di Rhino in esecuzione su un server a 2 nuclei 8 ore al giorno per 30 giorni:*
  * 1 computer * 2 nuclei * 8 ore/giorno * 30 giorni/mese * $0,10/core-ora = $48/mese.
  * Nota: il numero di istanze di Rhino non influisce sulla fattura.

**La fatturazione si basa sul tempo di esecuzione**, non sull'utilizzo; non monitoriamo l'attività di ciascun nucleo, ma solamente del nucleo su cui Rhino è in esecuzione. È possibile scalare in eccesso o difetto i carichi di lavoro per ottimizzare le prestazioni e i costi.

**Sono ammesse più istanze** - è possibile eseguire sullo stesso computer tutte le istanze di Rhino desiderate e il costo sarà equivalente a quello di una sola istanza.

## Impostazione della fatturazione nucleo per ora

La fatturazione nucleo per ora è necessaria quando si utilizza Rhino su un sistema operativo basato su Windows Server.

1. Accedere al [Portale licenze ](https://www.rhino3d.com/licenses?_forceEmpty=true) (accedere al proprio account Rhino se richiesto).
2. Fare clic su _Create New Team_ e creare un team da utilizzare per il progetto di calcolo. {{< call-out "note" "Nota" >}}
La creazione di un nuovo team non è strettamente necessaria, ma la fatturazione nucleo per ora *non è compatibile* con le licenze esistenti nel team. Pertanto, se il team dispone di licenze, la fatturazione nucleo per ora non sarà consentita.
{{< /call-out >}}

3. Fare clic su _Manage Team_ -> _Manage Core-Hour Billing_.
4. Selezionare l’opzione accanto ai prodotti che si desidera abilitare. \
**Nota: se il team è in funzione da anni, potrebbe essere necessario abilitare le versioni più recenti di Rhino.**
5. Fare clic su _Save_ e inserire le informazioni di pagamento quando richiesto per il nuovo team.

## Utilizzare la fatturazione nucleo per ora

1. Accedere al [Portale Licenze](https://www.rhino3d.com/licenses?_forceEmpty=true) e selezionare il team che è stato impostato con la fatturazione nucleo per ora.
1. Fare clic su _Manage Team_ -> _Manage Core-Hour Billing_.
2. Fare clic su _Action_ -> _Get Auth Token_ per ottenere un token.
3. Creare una nuova variabile d'ambiente con il nome `RHINO_TOKEN` e utilizzare il token come valore. Poiché il token è troppo lungo per la finestra di dialogo delle variabili d'ambiente di Windows, è più facile farlo tramite un comando PowerShell.

    ```ps
    [System.Environment]::SetEnvironmentVariable('RHINO_TOKEN', 'your token here', 'Machine')
    ```

D'ora in poi, quando si avvia Rhino su questo computer, si utilizzerà il team di fatturazione nucleo per ora.

{{< call-out "warning" "Avviso" >}}
<strong>Avviso</strong> Questo token consente a chiunque ne sia in possesso di addebitare spese al team. <strong>NON</strong> condividere questo token con nessuno.
{{< /call-out >}}

## Licenza a singolo computer non supportata

Se viene utilizzato Windows Server, non è possibile inserire un codice di licenza per eseguire una licenza a singolo computer perché Rhino richiede una licenza per nucleo.
