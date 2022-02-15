#!/usr/bin/env bash
PYNGUIN_DANGER_AWARE=1; pynguin -v --maximum_statement_executions 100 --maximum-iteration 10 --project-path ./ --output-path ./pynguin --module-name example.main
