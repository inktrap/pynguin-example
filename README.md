# Example

This seems like a strange issue?! pynguin provides many options … am I doing something wrong?

 - running ``run.sh``
     - generates ``pynguin_report`` but ``pynguin`` is given as output dir
     - does not value max iteration option and default stop value is 60 iterations
     - runs perhaps forever, even if coverage doesn't change?!
 - btw. I just want to start with some simple unittest-skeletons (c.f. auger, pythoscope)
 - could we have some project independent config file that is used for all runs? I would prefer to set ``PYNGUIN_DANGER_AWARE`` and maybe some other defaults once. Could be overwritten on a per-project basis. I could also delete my hard-drive with a terminal or a file manager and I guess most users are creating unittests for their own code.

