 - running ``run.sh``
     - generates ``pynguin_report`` but ``pynguin`` is given as output dir
     - does not value max iterations option and default stop value is 60 iterations
     - runs perhaps forever, even if coverage doesn't change?!

 - could we have some project independent config file that is used for all runs? I would prefer to set ``PYNGUIN_DANGER_AWARE`` and maybe some other defaults once. Could be overwritten on a per-project basis