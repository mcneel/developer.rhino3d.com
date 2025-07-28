+++
aliases = ["/en/5/guides/yak/pushing-a-package-to-the-server/", "/en/6/guides/yak/pushing-a-package-to-the-server/", "/en/7/guides/yak/pushing-a-package-to-the-server/", "/en/wip/guides/yak/pushing-a-package-to-the-server/"]
authors = [ "will" ]
categories = [ "Getting Started" ]
description = "Questa è una guida passo passo per inviare un pacchetto al server dei pacchetti."
keywords = [ "developer", "yak" ]
sdk = [ "Yak" ]
title = "Inviare un pacchetto al server"
type = "guides"
weight = 20
override_last_modified = "2020-11-12T12:17:36Z"

[admin]
TODO = ""
origin = ""
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

Consultare la guida [Il server dei pacchetti](/guides/yak/the-package-server/) per ulteriori dettagli sui formati dei numeri di versione consentiti.

{{< call-out "note" "Nota" >}}
Yak è multipiattaforma. Gli esempi che seguono sono per Windows.
Per Mac, sostituire il percorso dello strumento Yak CLI con<code>"/Applications/Rhino {{< latest-rhino-version >}}.app/Contents/Resources/bin/yak"</code>.

{{< /call-out >}}



## Autenticazione

Prima di poter inviare un pacchetto al server, è necessario autorizzare lo strumento Yak CLI usando l’account Rhino.


```commandline
> "C:\Program Files\Rhino {{< latest-rhino-version >}}\System\Yak.exe" login
```

Si aprirà una scheda del browser che vi chiederà di accedere a Rhino Accounts (sempre che non sia stato già effettuato l'accesso).
 La finestra successiva chiederà di fornire a "Yak" l'accesso all’account.


- **Visualizzare le informazioni personali** Questo ambito viene utilizzato per recuperare il nome, la località e l'immagine del profilo.
   Queste informazioni saranno utilizzate in futuro, quando il database dei pacchetti avrà un'interfaccia grafica.
  
- **Verificare l’identità** Utilizzato per l'autenticazione quando si interroga la proprietà di un pacchetto.
  
- **Visualizzare l'indirizzo e-mail** L'indirizzo e-mail principale viene memorizzato in modo da poter essere [aggiunto come proprietario](../yak-cli-reference/#owner) di pacchetti pubblicati da altri.

Una volta accettata, la finestra del browser si chiuderà da sola. Yak ha recuperato un token OAuth da Rhino Accounts e lo ha memorizzato sul computer.


- Mac - `~/.mcneel/yak.yml`
- Windows - `%APPDATA%\McNeel\yak.yml`

{{< call-out "note" "Nota" >}}
Per sicurezza, il token OAuth è valido solo per un periodo di tempo limitato.
 Lo strumento Yak CLI richiede un nuovo accesso dopo circa 30 giorni.

{{< /call-out >}}

## Invio

Ora che si è effettuato l'accesso, è possibile inviare un pacchetto al server. Useremo il pacchetto creato nel file

[guida precedente](../creating-a-grasshopper-plugin-package) come esempio.

```commandline
> "C:\Program Files\Rhino {{< latest-rhino-version >}}\System\Yak.exe" push marmoset-1.0.0-rh6_18-any.yak
```

Questo comando non restituisce nessun output anche se si esegue correttamente..

Possiamo controllare che il pacchetto sia stato inviato correttamente eseguendo una ricerca.
 Dovrebbe apparire il nome e il numero di versione del pacchetto appena inviato. 🤞


```commandline
> "C:\Program Files\Rhino {{< latest-rhino-version >}}\System\Yak.exe" search --all --prerelease marmoset

marmoset (1.0.0)
```

{{< call-out "note" "Nota" >}}
Se è la prima volta, perché non provare a inviare il file al server di prova?
```cmd
"C:\Program Files\Rhino {{< latest-rhino-version >}}\System\Yak.exe" push --source https://test.yak.rhino3d.com marmoset-1.0.0-rh6_18-any.yak

"C:\Program Files\Rhino {{< latest-rhino-version >}}\System\Yak.exe" search --source https://test.yak.rhino3d.com --all --prerelease marmoset

marmoset (1.0.0)
```
Questo server viene ripulito ogni sera.
{{< /call-out >}}

## Risoluzione dei problemi

Ci sono alcuni motivi per cui l’invio di un pacchetto potrebbe non funzionare.

- Invalid `manifest.yml`

  Il messaggio di errore dovrebbe essere autoesplicativo. Correggiamo e riproviamo! Si può anche provare a convalidare la sintassi YAML stessa con un'opzione
  
  [linter](http://www.yamllint.com)._

- Il nome del pacchetto esiste già, ma non siamo un **proprietario**.

  Solo i **proprietari** dei pacchetti sono autorizzati a inviare nuove versioni dei loro pacchetti.
  Quando un utente invia la prima versione di un pacchetto, ne diventa **proprietario**. È possibile aggiungere altri proprietari con il comando [`_owner`](../yak-cli-reference/#owner).

- La versione del pacchetto esiste già.

  Per evitare di disturbare gli altri che stanno usando uno dei pacchetti, non è possibile cancellare o sovrascrivere le versioni.
   Date il numero di versione e informare gli utenti che c'è qualcosa di nuovo da provare!
  

- Invio erroneo di contenuti.

  _Usare il [comando `yank`](../yak-cli-reference/#yank) per escludere dall’elenco una versione specifica._

## Argomenti correlati

- [Il server dei pacchetti](/guides/yak/the-package-server/)
- [Creazione di un pacchetto di plug-in per Grasshopper](/guides/yak/creating-a-grasshopper-plugin-package/)
- [Creazione di un pacchetto di plug-in per Rhino](/guides/yak/creating-a-rhino-plugin-package/)
