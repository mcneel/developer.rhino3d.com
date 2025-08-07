+++
title = "Initialisation des langages de script"
description = "Ce guide explique le processus d’initialisation de différents runtimes de langage"
authors = ["ehsan"]

[included_in]
platforms = [ "Windows", "Mac" ]
since = 8

[page_options]
byline = true
toc = true
toc_type = "single"
block_webcrawlers = false
+++

<style>
    code {
        background-color: #efefef;
        padding-left: 5px;
        padding-right: 5px;
        border-radius: 3px;
    }
</style>

## Répertoire racine de script

Tous les langages initialisent leur runtime dans le répertoire racine de script. Il se trouve en général dans :

- `%USERPROFILE%\N-.rhinocode` sous Window
- `~/.rhinocode` sous macOS (et autres de type Unix)

Par exemple, dans Rhino 8, les runtimes et les modules de Python 3 (CPython) et Python 2 (IronPython) sont déployés dans les répertoires suivants :

- `~/.rhinocode/py39-rh8/` pour Python 3 
- `~/.rhinocode/py27-rh8/` pour Python 2

Outre les runtimes de langage, le répertoire racine contient également :

- `logs/` pour les fichiers journaux des applications
- `stage/` pour les scripts temporaires
- `libs/` pour le cache des bibliothèques de scripts
- `component.json` pour les configurations des composants de script
- `editor.json` pour les configurations de l’éditeur de scripts

### Modifier le répertoire racine

Il est parfois nécessaire de modifier l’emplacement de ce répertoire. Comme indiqué ci-dessus, Python 3 déploie son runtime dans le répertoire racine de script et doit lancer l’exécutable binaire de Python (`python.exe` sous Windows) pour démarrer le serveur de langage et installer les paquets de PyPI.org.

Si, pour des raisons de sécurité, vous devez bloquer cette opération, vous pouvez changer le répertoire racine de script par un autre emplacement avec des privilèges d’exécution.

Pour modifier le répertoire racine de script :

- Ouvrez Rhino.
- N’utilisez pas les outils de script ; en d’autres termes, n’ouvrez pas ScriptEditor ou Grasshopper, et n’exécutez pas RunPythonCommand.
- Allez dans **Rhino -> Outils -> Options -> Options avancées** et remplacez la valeur vide par défaut de `RhinoCodePlugin.RootPath` par le chemin du répertoire racine de votre choix. Il doit s’agir d’un chemin absolu et le répertoire doit être accessible en écriture avec des privilèges d’exécution pour l’utilisateur de Rhino.
- Fermez et redémarrez Rhino.
- Ouvrez l’éditeur de scripts et laissez-le initialiser les langages dans ce nouveau répertoire racine.
- Ouvrez Grasshopper et placez un composant Script sur la toile afin que le fichier `component.json` soit également créé dans le répertoire racine.

![](01.png)

### Réinitialiser le répertoire racine

Pour rétablir le répertoire racine de script par défaut, supprimez le chemin que vous aviez indiqué pour `RhinoCodePlugin.RootPath` dans les **Options avancées** comme indiqué ci-dessus.