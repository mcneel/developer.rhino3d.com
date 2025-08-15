+++
aliases = ["/en/5/guides/compute/core-hour-billing/", "/en/6/guides/compute/core-hour-billing/", "/en/7/guides/compute/core-hour-billing/", "/en/wip/guides/compute/core-hour-billing/"]
authors = [ "brian" ]
categories = [ "Deployment" ]
keywords = [ "developer", "compute", "core-hour" ]
languages = []
sdk = [ "Compute" ]
title = "Licences et facturation"
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


## À propos de la facturation par cœur et par heure

Lorsque Rhino est connecté à un compte de service et qu’il est exécuté sur un système d’exploitation Windows Server, vous serez facturé **0,10 $ par cœur et par heure** de fonctionnement de Rhino (au prorata de la minute).

***Exemple 1 :** Rhino fonctionne sur un serveur 32 cœurs pendant une heure :*

  * 1 ordinateur * 32 cœurs * 1 heure * 0,10 $ /cœur/heure = 3,20 $

***Exemple 2 :** Rhino fonctionne sur 200 serveurs 4 cœurs pendant 6 minutes :*

  * 200 ordinateurs * 4 cœurs * 0,1 heure * 0,10 $ /cœur/heure = 8 $

***Exemple 3 :** 1 session de Rhino fonctionne sur un serveur à 2 cœurs, 8 heures par jour pendant 30 jours :*
  * 1 ordinateur * 2 cœurs * 8 heures/jour * 30 jours/mois * 0,10 $/cœur/heure = 48 $/mois

***Exemple 4 :** 10 sessions de Rhino fonctionnent sur un serveur à 2 cœurs, 8 heures par jour pendant 30 jours :*
  * 1 ordinateur * 2 cœurs * 8 heures/jour * 30 jours/mois * 0,10 $/cœur/heure = 48 $/mois
  * (Vous remarquez que le nombre de sessions de Rhino n’a pas d’incidence sur votre facture.)

**La facturation est basée sur le temps de disponibilité** et non pas sur le temps d’utilisation. Nous ne contrôlons pas l’activé de chaque cœur, mais simplement qu’un cœur exécute Rhino. Vous pouvez augmenter ou réduire votre volume de travail afin d’optimiser la performance et le coût final.

**Possibilité d’ouvrir plusieurs sessions de Rhino** -  Vous pouvez ouvrir autant de sessions de Rhino que vous voulez sur la même machine ; le coût sera le même que vous ayez une ou plusieurs sessions ouvertes.

## Mettre en place une facturation par cœur et par heure

La facturation par cœur et par heure doit être mise en place lorsque Rhino est utilisé sur un système d’exploitation Windows Server.

1. Accédez au [Portail des licences](https://www.rhino3d.com/licenses?_forceEmpty=true) (connectez-vous à votre compte Rhino si vous y êtes invité).
2. Cliquez sur _Créer une nouvelle équipe_ et créez une équipe que vous utiliserez pour votre projet Compute. {{< call-out "note" "Remarque" >}}
Il n’est pas absolument nécessaire de créer une nouvelle équipe ; toutefois, la facturation par cœur et par heure n’est *pas compatible* avec les licences existantes dans l’équipe. Par conséquent, si votre équipe est associée à une licence, vous ne pourrez pas mettre en place la facturation par cœur et par heure.
{{< /call-out >}}

3. Cliquez sur _Gérer une équipe_ -> _Gérer une facturation par cœur et par heure_.
4. Cochez la case devant les produits que vous souhaitez activer. \
**Remarque : si vous avez une équipe qui fonctionne depuis des années, il se peut que vous deviez activer une version plus récente de Rhino.**
5. Cliquez sur _Enregistrer_, et renseignez les informations de paiement lorsque vous y serez invité pour votre nouvelle équipe.

## Utiliser la facturation par cœur et par heure

1. Allez sur le [Portail des licences](https://www.rhino3d.com/licenses?_forceEmpty=true) et sélectionnez l’équipe pour laquelle vous venez de configurer la facturation par cœur et par heure.
1. Cliquez sur _Gérer une équipe_ -> _Gérer une facturation par cœur et par heure_.
2. Cliquez sur _Action_ -> _Obtenir un jeton d’autorisation_ pour obtenir un jeton.
3. Créez une nouvelle variable d’environnement que vous nommerez `RHINO_TOKEN` et utilisez le jeton comme valeur. Le jeton étant trop long pour la boîte de dialogue Variables d’environnement de Windows, il est plus facile de réaliser cette opération via une commande PowerShell.

    ```ps
    [System.Environment]::SetEnvironmentVariable('RHINO_TOKEN', 'votre jeton ici', 'Machine')
    ```

Dorénavant, lorsque vous démarrerez Rhino sur cette machine, il utilisera votre équipe de facturation par cœur et par heure.

{{< call-out "warning" "Avertissement" >}}
<strong>Attention !</strong> Ce jeton permet à toute personne qui le possède de facturer votre équipe à volonté. Ne le partagez <strong>EN AUCUN CAS</strong>.
{{< /call-out >}}

## Licence sur ordinateur unique non prise en charge

Lorsque Rhino fonctionne sur Windows Server, il n’est pas possible d’entrer une clé de licence rattachée uniquement à l’ordinateur étant donné que Rhino a besoin d’une licence par cœur.
