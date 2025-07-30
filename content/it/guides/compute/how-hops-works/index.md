+++
aliases = ["/en/5/guides/compute/how-hops-works/", "/en/6/guides/compute/how-hops-works/", "/en/7/guides/compute/how-hops-works/", "/en/wip/guides/compute/how-hops-works/"]
authors = [ "andy.payne" ]
categories = [ "Hops" ]
keywords = [ "developer", "grasshopper", "components", "hops" ]
languages = [ "Grasshopper" ]
sdk = [ "Compute" ]
title = "Come funziona Hops"
type = "guides"
weight = 2
override_last_modified = "2022-02-18T10:08:37Z"

[admin]
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows", "Mac" ]
since = 0

[page_options]
byline = true
toc = true
toc_type = "single"
+++

Il processo di comunicazione tra Hops e un server conforme a Hops è un po' più complesso del semplice invio e ricezione di una singola richiesta e risposta http. Il primo passo del processo avviene quando Hops raggruppa la definizione di Grasshopper di riferimento e invia una richiesta http a un endpoint del server. 

Un endpoint è un indirizzo URL che consente di raggiungere il server per eseguire una determinata funzione. In questa richiesta, il server apre la definizione di Grasshopper inviata da Hops e determina quali informazioni saranno necessarie per popolare gli input e gli output del componente Hops. Quindi, l'endpoint si chiamerà `/io` (abbreviazione di Input Output).

{{< image url="/images/hops_io_request.png" alt="/images/hops_io_request.png" class="image_center" width="100%" >}}

Il componente Hops dovrebbe ora disporre di informazioni sufficienti per creare i nodi di ingresso e di uscita necessari. 

{{< image url="/images/hops_get_inputs.png" alt="/images/hops_get_inputs.png" class="image_center" width="75%" >}}

Quando tutti gli input di Hops sono stati collegati ai parametri di origine, invierà un'altra richiesta http al server, solo che questa volta invierà la richiesta all'endpoint `/solve`. Non è necessario inviare nuovamente la definizione di Grasshopper, poiché è stata memorizzata sul server durante il processo `/io`. Invece, i dati inviati nella richiesta `/solve` contengono solo un ID puntatore che indica al server dove trovare il file corretto e tutti i dati di input. 

La risposta http del server contiene tutti i dati che verrebbero restituiti dall'esecuzione del file Grasshopper in modo tradizionale.

{{< image url="/images/hops_return_results.png" alt="/images/hops_return_results.png" class="image_center" width="70%" >}}

Per capire meglio come funzionano i passaggi precedenti, è possibile esportare l'ultima richiesta e risposta http per entrambi gli endpoint `/io` e `/solve` direttamente dal componente Hops.

{{< image url="/images/hops_export_requests.png" alt="/images/hops_export_requests.png" class="image_center" width="100%" >}}

 ---
 
## Collegamenti rapidi

 - [Che cos'è Hops](../what-is-hops)
 - [Il componente Hops](../hops-component)
 - [Impostazione di un ambiente di produzione](../deploy-to-iis)