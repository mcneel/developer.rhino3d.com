+++
aliases = ["/en/5/guides/yak/yak-cli-reference/", "/en/6/guides/yak/yak-cli-reference/", "/en/7/guides/yak/yak-cli-reference/", "/en/wip/guides/yak/yak-cli-reference/"]
authors = [ "will" ]
categories = [ "Fundamentals" ]
description = "Un riferimento per lo strumento a linea di comando Yak."
keywords = [ "developer", "yak" ]
sdk = [ "Yak" ]
title = "Riferimento agli strumenti a linea di comando Yak"
type = "guides"
weight = 1

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

Lo strumento a linea di comando Yak è incluso in Rhino 7 WIP. In Windows, lo strumento si trova in `"C:\Program Files\Rhino {{< latest-rhino-version >}}System\yak.exe"`. Su macOS esiste un comodo script in `"/Applications/Rhino {{< latest-rhino-version >}}.app/Contents/Resources/bin/yak"`.

## Comandi

### Build

* _Since 0.2: Command added_
* _Since 0.4: Supports multiple .gha files, .rhp files or anything else for that matter_
* _Since 0.9: Appends distribution tag to filename and expands $version placeholder_
* _Since 0.10.1: Adds `--platform` argument_

Quando viene eseguito in una cartella contenente un file `manifest.yaml` valido, crea un pacchetto contenente tutti i file della cartella.

```commandline
Usage: yak build [options]

Options:
    --platform PLATFORM  The platform where the package will run ('win', 'mac' or 'any')
    -h, --help           Get help (equivalent to `yak help build`)
```

{{< call-out "note" "Nota" >}}
  Un <a class="alert-link" href="../the-anatomy-of-a-package#distributions">tag di distribuzione</a> (ad esempio<code>rh7-win</code>) viene aggiunto al nome del file del pacchetto creato. Il tag viene determinato ispezionando il contenuto del pacchetto durante la creazione. L'argomento <code>&#45;&#45;platform=any</code> può essere usato se l'autore vuole pubblicare una distribuzione multipiattaforma, ad esempio code>rh7-any</code>. Attualmente è possibile ispezionare solo i file .rhp e .gha. Se un pacchetto non contiene nessuno di questi elementi, avrà un tag di distribuzione <code>any-any</code>.
{{< /call-out >}}

<!-- Durante la compilazione, il GUID del componente viene estratto per facilitare la ricerca del pacchetto in seguito. -->

### Install

* _Since 0.1: Command added_
* _Since 0.13.0: Supports installing local .yak files_

Installa un pacchetto (facoltativamente con una versione specifica).

```commandline
Usage:
    yak install [--source=URL] <package> [<version>]
    yak install <package>
```

Dove`<package>` è il nome di un pacchetto o il percorso di un file .yak locale.

### List

_Since 0.2_

Elenca i pacchetti installati sulla macchina.

```commandline
yak list
```

### Login

* _Since 0.2: Command added_
* _Since 0.10: User registered during login_

Autentica con Rhino Accounts e memorizza un token di accesso OAuth2 limitato nel tempo, in modo che l'utente possa usare i comandi che richiedono l'autenticazione.

```commandline
Usage: yak login [options]

Options:
    --ci              Generate a non-expiring API key and display it
    -s, --source URL Posizione del repository del pacchetto [default: https://yak.rhino3d.com/].
    -h, --help        Get help (equivalent to `yak help login`)
```

Su Windows, il token è memorizzato in `%appdata%\McNeel\yak.yml`. Su macOS, è memorizzato in `~/.mcneel/yak.yml`.

Durante il primo accesso, l'utente viene registrato sul server.

{{< call-out "note" "Nota" >}}
  In un ambiente di compilazione automatizzato, ad esempio una macchina di compilazione, GitHub Actions, ecc. - lo strumento CLI `yak` può leggere il token di accesso dalla variabile d'ambiente `YAK_TOKEN`. Utilizzare il flag `--ci` per effettuare il login e creare un token a questo scopo.
{{< /call-out >}}

### Push

_Since 0.1_

Invia un pacchetto al server.

```commandline
yak push [--source=URL] <filename>
```

{{< call-out "note" "Nota" >}}
  Richiede <a class="alert-link" href="#login">autenticazione</a>.
{{< /call-out >}}

### Search

* _Since 0.1: Command added_
* _Since 0.5: Adds `--all` and `--prerelease` flags_

Cerca sul server i pacchetti che corrispondono a `query`.

```commandline
Usage: yak search [options] <query>

  Opzioni:
    --prerelease      Display prerelease package versions
    -a, --all         Display all package versions
    -s, --source URL  Package repository location
    -h, --help        Get help (equivalent to `yak help search`)
```

### Spec

* _Since 0.2: Command added_
* _Since 0.4: Adds support for inspecting .rhp files (RhinoCommon only)_

Crea un file `manifest.yml` strutturale, basato sul contenuto della cartella corrente.
Quando viene eseguito in una directory contenente un assieme Grasshopper (`.gha`) o un plug-in RhinoCommon, il file (`.rhp`) verrà ispezionato e utilizzato per pre-popolare il file `manifest.yml`.



```commandline
yak spec
```

### Uninstall

_Since 0.1_

Disinstalla un pacchetto.

```commandline
yak uninstall <package>
```
<!-- deactivation fallback removed in v0.6-->
<!-- {{< call-out "note" "Nota" >}}
  Dalla versione 0.3, Yak tenterà di rimuovere il pacchetto dalla macchina. Se questo non è possibile (probabilmente perché Rhino è in esecuzione), il pacchetto verrà invece disattivato.
{{< /call-out >}} -->

### Yank

_Since 0.6_

Rimuove una versione dall'indice del pacchetto.

```commandline
yak yank <package> <version>
```

{{< call-out "note" "Nota" >}}
  Richiede <a class="alert-link" href="#login">autenticazione</a>.
{{< /call-out >}}

Le versioni eliminate non appaiono nelle ricerche, ma possono essere installate se si conosce la versione esatta del pacchetto. Sono nascosti a tutti gli effetti.

Non è possibile inviare una versione del pacchetto che è stata eliminata. In questo caso, è sufficiente modificare il numero di versione del proprio pacchetto e ripetere l'operazione.

Se tutte le versioni di un pacchetto vengono rimosse, esso non apparirà più nell'indice dei pacchetti.

{{< call-out danger "Pericolo" >}}
  <p><strong>Eliminazione di un pacchetto dal server McNeel</strong></p>
  <p>Per cancellare un pacchetto dal server pubblico, inviare un'e-mail a <a href="mailto:support@mcneel.com">support@mcneel.com</a>. Una volta che il pacchetto è stato cancellato, il nome non può più essere utilizzato.</p>
{{< /call-out >}}

### Unyank

Funziona come il comando yank, ma al contrario!

### Owner

_Since 0.10_

Aggiunge, rimuove o elenca i proprietari di un pacchetto. I proprietari di un pacchetto possono inviare nuove versioni del pacchetto e eliminare o annullare l’eliminazione delle versioni esistenti.

```commandline
Usage:
    yak owner add [--source=URL] <package> <email>
    yak owner remove [--source=URL] <package> <email>
    yak owner list [--source=URL] <package>
    
Options:
    -h, --help
    -s, --source URL  Package repository location [default: https://yak.rhino3d.com/].
```

Tenere presente che i nuovi proprietari possono fare tutto ciò che può fare il proprietario originale. 

I nuovi proprietari devono essere registrati sul server prima di poter essere aggiunti a un pacchetto. Possono farlo eseguendo il comando [`login`](#login).

## Download

`yak` CLI è disponibile come eseguibile indipendente per l'uso in ambienti in cui Rhino non è installato, ad esempio su macchine di compilazione automatica.

* https://files.mcneel.com/yak/tools/0.13.0/yak.exe
* https://files.mcneel.com/yak/tools/0.13.0/win-arm64/yak.exe
* https://files.mcneel.com/yak/tools/0.13.0/mac/yak
* https://files.mcneel.com/yak/tools/0.13.0/linux-x64/yak
* https://files.mcneel.com/yak/tools/0.13.0/linux-arm64/yak


## Argomenti correlati

- [Guide e tutorial su Yak](/guides/yak/)
- [Anatomia di un pacchetto](/guides/yak/the-anatomy-of-a-package/)
- [Il manifesto del pacchetto](/guides/yak/the-package-manifest/)
