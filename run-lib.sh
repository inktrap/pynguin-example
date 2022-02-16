#!/usr/bin/env bash
export PYNGUIN_DANGER_AWARE=1; pynguin -v --create-coverage-report True --project-path ./ --output-path ./pynguin --module-name example.lib.ops # --stopping-condition MAX_ITERATIONS --maximum-iteration 100
