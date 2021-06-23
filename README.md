loki-handler
===================

[![PyPI version](https://img.shields.io/pypi/v/loki-handler.svg)](https://pypi.org/project/loki-handler/)
[![License](https://img.shields.io/pypi/l/loki-handler.svg)](https://opensource.org/licenses/MIT)
[![CircleCI](https://circleci.com/gh/cuerty/loki-handler/tree/master.svg?style=svg)](https://circleci.com/gh/cuerty/loki-handler/?branch=master)

Python logging handler for Loki.  
https://grafana.com/loki

Backport of [Andrey Maslov](https://github.com/GreyZmeem)'s [python-logging-loki](https://github.com/GreyZmeem/python-logging-loki) for Python 2.X.

Installation
============
```bash
pip install loki-handler
```

Usage
=====

```python
import logging
import loki_handler


handler = loki_handler.LokiHandler(
    url="https://my-loki-instance/loki/api/v1/push", 
    tags={"application": "my-app"},
    auth=("username", "password"),
    version="1",
)

logger = logging.getLogger("my-logger")
logger.addHandler(handler)
logger.error(
    "Something happened", 
    extra={"tags": {"service": "my-service"}},
)
```

Example above will send `Something happened` message along with these labels:
- Default labels from handler
- Message level as `serverity`
- Logger's name as `logger` 
- Labels from `tags` item of `extra` dict

The given example is blocking (i.e. each call will wait for the message to be sent).
