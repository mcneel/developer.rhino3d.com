+++
aliases = ["/en/5/guides/compute/how-hops-works/", "/en/6/guides/compute/how-hops-works/", "/en/7/guides/compute/how-hops-works/", "/en/wip/guides/compute/how-hops-works/"]
authors = [ "andy.payne" ]
categories = [ "Hops" ]
keywords = [ "developer", "grasshopper", "components", "hops" ]
languages = [ "Grasshopper" ]
sdk = [ "Compute" ]
title = "So funktioniert Hops"
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

Der Kommunikationsprozess zwischen Hops und einem Hops-kompatiblen Server ist etwas komplizierter als das einfache Senden und Empfangen einer einzelnen http-Anfrage und -Antwort. Der erste Schritt des Prozesses besteht darin, dass Hops die referenzierte Grasshopper-Definition bündelt und eine http-Anfrage an einen Endpunkt des Servers sendet. 

Ein Endpunkt ist eine URL-Adresse, unter der der Server erreicht werden kann, um eine bestimmte Funktion auszuführen. In dieser Anfrage öffnet der Server die von Hops gesendete Grasshopper-Definition und bestimmt, welche Informationen benötigt werden, um die Ein- und Ausgänge für die Hops-Komponente zu füllen. Der Endpunkt wird also `/io` (kurz für Input Output) genannt.

{{< image url="/images/hops_io_request.png" alt="/images/hops_io_request.png" class="image_center" width="100%" >}}

Die Komponente Hops sollte nun über genügend Informationen verfügen, um die erforderlichen Ein- und Ausgangsknoten für sich selbst zu erstellen. 

{{< image url="/images/hops_get_inputs.png" alt="/images/hops_get_inputs.png" class="image_center" width="75%" >}}

Wenn alle Hops-Eingaben mit den Quellparametern verbunden wurden, wird eine weitere http-Anfrage an den Server gesendet - nur dieses Mal an den Endpunkt `/solve`. Die Grasshopper-Definition muss nicht erneut gesendet werden, da sie während des `/io`-Prozesses auf dem Server gespeichert wurde. Stattdessen enthalten die in der `/solve`-Anfrage gesendeten Daten nur eine Zeiger-ID, die dem Server mitteilt, wo er die richtige Datei und alle Eingabedaten finden kann. 

Die http-Antwort des Servers enthält alle Daten, die beim Ausführen der Grasshopper-Datei auf herkömmliche Weise zurückgegeben werden würden.

{{< image url="/images/hops_return_results.png" alt="/images/hops_return_results.png" class="image_center" width="70%" >}}

Um besser zu verstehen, wie jeder der obigen Schritte funktioniert, können Sie die letzte http-Anfrage und -Antwort für die Endpunkte `/io` und `/solve` direkt aus der Komponente Hops exportieren.

{{< image url="/images/hops_export_requests.png" alt="/images/hops_export_requests.png" class="image_center" width="100%" >}}

 ---
 
## Quick Links

 - [Was ist Hops?](../what-is-hops)
 - [Die Hops-Komponente](../hops-component)
 - [Einrichten einer Produktionsumgebung](../deploy-to-iis)