+++
aliases = ["/en/5/guides/yak/pushing-a-package-to-the-server/", "/en/6/guides/yak/pushing-a-package-to-the-server/", "/en/7/guides/yak/pushing-a-package-to-the-server/", "/en/wip/guides/yak/pushing-a-package-to-the-server/"]
authors = [ "will" ]
categories = [ "Getting Started" ]
description = "Ce guide explique étape par étape comment envoyer un paquet sur le serveur de paquets."
keywords = [ "developer", "yak" ]
sdk = [ "Yak" ]
title = "Envoyer un paquet sur le serveur"
type = "guides"
weight = 20

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

Reportez-vous au guide sur le [serveur de paquets](/guides/yak/the-package-server/) pour en savoir plus sur le serveur de paquets public de McNeel.

{{< call-out "note" "Remarque" >}}
Yak est multiplateforme. Les exemples ci-dessous concernent Windows.
Pour Mac, remplacez le chemin d’accès à l’outil CLI de Yak par <code>"/Applications/Rhino {{< latest-rhino-version >}}.app/Contents/Resources/bin/yak"</code>.

{{< /call-out >}}



## Authentification

Avant de pouvoir envoyer un paquet sur le serveur, vous devez autoriser l’outil CLI de Yak à partir de votre compte Rhino.


```commandline
> "C:\Program Files\Rhino {{< latest-rhino-version >}}\System\Yak.exe" login
```

Une fenêtre du navigateur s’ouvrira et vous devrez vous connecter à Rhino Accounts (si vous n’êtes pas déjà connecté).
 La fenêtre suivante vous demande d’autoriser « Yak » à accéder à votre compte.


- **Voir des informations de base sur vous** : cela permet de récupérer votre nom, votre situation géographique et votre photo de profil.
   Ces informations seront utilisées ultérieurement, si la base de données du paquet a une interface graphique.
  
- **Vérifier votre identité** : ces données sont utilisées pour l’authentification lors de l’interrogation sur la propriété du paquet.
  
- **Voir votre adresse e-mail** : votre adresse e-mail principale est stockée afin que vous puissiez être [ajouté en tant que propriétaire](../yak-cli-reference/#owner) de paquets publiés par d’autres personnes.

Une fois que vous avez accepté, la fenêtre du navigateur se ferme toute seule. Yak récupère un jeton OAuth auprès de Rhino Accounts et l’enregistre sur votre ordinateur.


- Mac - `~/.mcneel/yak.yml`
- Windows - `%APPDATA%\McNeel\yak.yml`

{{< call-out "note" "Remarque" >}}
Pour des raisons de sécurité, le jeton OAuth n’est valable que pour une durée limitée.
 Ne soyez pas surpris si l’outil CLI de Yak vous redemande de vous connecter après environ 30 jours.

{{< /call-out >}}

## Envoyez !

Maintenant que vous êtes connecté, vous pouvez envoyer un paquet sur le serveur. À titre d’exemple, je vais utiliser le paquet que nous avons créé dans le [guide sur la création d’un paquet pour un module de Grasshopper](../creating-a-grasshopper-plugin-package).



```commandline
> "C:\Program Files\Rhino {{< latest-rhino-version >}}\System\Yak.exe" push marmoset-1.0.0-rh6_18-any.yak
```

Si tout est correct, cette commande ne renvoie aucun résultat.

Pour vérifier que votre paquet a été envoyé avec succès, recherchez-le.
 Vous devriez voir le nom et le numéro de version du paquet que vous venez d’envoyer. 🤞


```commandline
> "C:\Program Files\Rhino {{< latest-rhino-version >}}\System\Yak.exe" search --all --prerelease marmoset

marmoset (1.0.0)
```

{{< call-out "note" "Remarque" >}}
Si c’est la première fois que vous le faites, pourquoi ne pas essayer d’abord d’envoyer votre paquet sur le serveur de test ?
```cmd
"C:\Program Files\Rhino {{< latest-rhino-version >}}\System\Yak.exe" push --source https://test.yak.rhino3d.com marmoset-1.0.0-rh6_18-any.yak

"C:\Program Files\Rhino {{< latest-rhino-version >}}\System\Yak.exe" search --source https://test.yak.rhino3d.com --all --prerelease marmoset

marmoset (1.0.0)
```
Ce serveur est nettoyé chaque nuit.
{{< /call-out >}}

## Résolution des problèmes

Différentes raisons peuvent expliquer un échec lors de l’envoi d’un paquet sur le serveur.

- Fichier manifeste invalide

  _Le message d’erreur (« Invalid `manifest.yml` ») est assez évident. Réparez votre fichier manifeste et réessayez ! Vous pouvez également vérifier la syntaxe YAML au moyen d’un [linter](http://www.yamllint.com)._
  
  

- Le nom du paquet existe déjà, mais vous n’êtes pas **propriétaire**

  _Seuls les **propriétaires** de paquets sont autorisés à publier de nouvelles versions de leurs paquets.
  Quand un utilisateur envoie la première version d’un paquet, il en devient le **propriétaire**. Des propriétaires supplémentaires peuvent être ajoutés au moyen de la commande [`owner`](../yak-cli-reference/#owner)._

- La version du paquet existe déjà

  _Afin de ne pas perturber les personnes qui utilisent l’un de vos paquets, il n’est pas possible de supprimer ou d’écraser les versions.
   Indiquez le numéro de version et faites savoir à vos utilisateurs qu’il y a du nouveau !_
  

- Vous avez envoyé un paquet sans le vouloir ?

  _Utilisez la commande [`yank`](../yak-cli-reference/#yank) pour supprimer une certaine version de la liste._

## Voir aussi

- [Le serveur de paquets](/guides/yak/the-package-server/)
- [Créer un paquet pour un module de Grasshopper](/guides/yak/creating-a-grasshopper-plugin-package/)
- [Créer un paquet pour un module de Rhino](/guides/yak/creating-a-rhino-plugin-package/)
