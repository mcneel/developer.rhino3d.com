+++
aliases = ["/en/5/guides/compute/how-hops-works/", "/en/6/guides/compute/how-hops-works/", "/en/7/guides/compute/how-hops-works/", "/en/wip/guides/compute/how-hops-works/"]
authors = [ "andy.payne" ]
categories = [ "Hops" ]
keywords = [ "developer", "grasshopper", "components", "hops" ]
languages = [ "Grasshopper" ]
sdk = [ "Compute" ]
title = "Comment fonctionne Hops ?"
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

Le processus de communication entre Hops et un serveur compatible avec Hops ne se limite pas à l’envoi et à la réception d’une requête et d’une réponse http. Pour commencer, Hops empaquette la définition de Grasshopper référencée et envoie une requête http à un point de terminaison sur le serveur. 

Un point de terminaison est une adresse URL à laquelle le serveur peut être joint pour exécuter une certaine fonction. Lorsqu’il reçoit cette requête, le serveur ouvre la définition de Grasshopper envoyée par Hops et détermine quelles informations seront nécessaires pour renseigner les entrées et les sorties du composant Hops. Le point de terminaison sera donc appelé `/io` (pour « Input Output »).

{{< image url="/images/hops_io_request.png" alt="/images/hops_io_request.png" class="image_center" width="100%" >}}

Le composant Hops doit alors disposer des informations nécessaires pour créer les nœuds d’entrée et de sortie dont il a besoin. 

{{< image url="/images/hops_get_inputs.png" alt="/images/hops_get_inputs.png" class="image_center" width="75%" >}}

Lorsque toutes les entrées de Hops ont été connectées aux paramètres source, il envoie une autre requête http au serveur ; mais cette fois-ci, il envoie la requête au point de terminaison `/solve`. La définition de Grasshopper n’a pas besoin d’être renvoyée puisqu’elle a été enregistrée sur le serveur pendant le processus `/io`. Au lieu de cela, les données envoyées dans la requête `/solve` ne contiennent qu’un pointeur ID qui indique au serveur où trouver le bon fichier et toutes les données d’entrée. 

La réponse http du serveur contient toutes les données qui seraient renvoyées si le fichier Grasshopper était exécuté de manière traditionnelle.

{{< image url="/images/hops_return_results.png" alt="/images/hops_return_results.png" class="image_center" width="70%" >}}

Pour mieux comprendre le fonctionnement de chacune des étapes précédentes, vous pouvez exporter la dernière requête http et la dernière réponse http pour les points de terminaison `/io` et `/solve` directement à partir du composant Hops.

{{< image url="/images/hops_export_requests.png" alt="/images/hops_export_requests.png" class="image_center" width="100%" >}}

 ---
 
## Liens rapides

 - [Qu’est-ce que Hops ?](../what-is-hops)
 - [Le composant Hops](../hops-component)
 - [Mettre en place un environnement de production](../deploy-to-iis)