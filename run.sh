#!/usr/bin/env bash
export PYNGUIN_DANGER_AWARE=1; pynguin -v --project-path ./ --output-path ./pynguin --module-name example.main --stopping-condition MAX_ITERATIONS --maximum-iteration 100
