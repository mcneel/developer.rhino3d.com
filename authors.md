---
layout: fullwidth-page
title: Authors
description: Author credits and contributions
permalink: /authors/
order: 1
---

# Authors

Thanks to all who have [contributed to this site](https://github.com/mcneel/developer-rhino3d-com/graphs/contributors).  Contributions, both large and small, are welcome and appreciated.  If you would like to help improve this site, please see the [Contributing]({{ site.baseurl }}/guides/general/contributing/#this-website) guide.

The following people have authored [guides]({{ site.baseurl }}/guides), [samples]({{ site.baseurl }}/samples), or other content:

<div class="trigger">
<ul>
  {% for author in site.data.authors %}
    <li>
      <a class="page-link" href="{{ site.baseurl }}/authors/{{ author.name }}/">{{ author.display_name }}</a>
    </li>
  {% endfor %}
</ul>
</div>
