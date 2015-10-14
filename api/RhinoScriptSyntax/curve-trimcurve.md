---
layout: bootstrap
---

# TrimCurve

Trims a curve by removing portions of the curve outside a specified interval
        Paramters:
          curve_id = the curve to trim
          interval = two numbers indentifying the interval to keep. Portions of
            the curve before domain[0] and after domain[1] will be removed. If the
            input curve is open, the interval must be increasing. If the input
            curve is closed and the interval is decreasing, then the portion of
            the curve across the start and end of the curve is returned
          delete_input[opt] = delete the input curve
        Reutrns:
          identifier of the new curve on success
          None on failure
        


