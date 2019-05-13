#!/bin/sh
#
# This file is part of REANA.
# Copyright (C) 2017, 2018, 2019 CERN.
#
# REANA is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

pydocstyle reana_workflow_controller && \
isort -rc -c -df **/*.py && \
FLASK_APP=reana_workflow_controller/app.py python ./scripts/generate_openapi_spec.py && \
diff -q -w temp_openapi.json docs/openapi.json && \
check-manifest --ignore ".travis-*" && \
sphinx-build -qnN docs docs/_build/html && \
python setup.py test && \
docker build -t reanahub/reana-workflow-controller .
