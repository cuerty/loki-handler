# -*- coding: utf-8 -*-

import logging
import warnings

from loki_handler import const
from loki_handler import emitter


class LokiHandler(logging.Handler):
    """
    Log handler that sends log records to Loki.
    `Loki API <https://github.com/grafana/loki/blob/master/docs/api.md>`_
    """

    emitters = {
        "0": emitter.LokiEmitterV0,
        "1": emitter.LokiEmitterV1,
    }

    def __init__(self, url, tags=None, auth=None, version=None):
        """
        Create new Loki logging handler.
        Arguments:
            url: Endpoint used to send log entries to Loki (e.g. `https://my-loki-instance/loki/api/v1/push`).
            tags: Default tags added to every log record.
            auth: Optional tuple with username and password for basic HTTP authentication.
            version: Version of Loki emitter to use.
        """
        super(LokiHandler, self).__init__()

        if version is None and const.emitter_ver == "0":
            msg = (
                "Loki /api/prom/push endpoint is in the depreciation process starting from version 0.4.0.",
                "Explicitly set the emitter version to '0' if you want to use the old endpoint.",
                "Or specify '1' if you have Loki version> = 0.4.0.",
                "When the old API is removed from Loki, the handler will use the new version by default.",
            )
            warnings.warn(" ".join(msg), DeprecationWarning)

        version = version or const.emitter_ver
        if version not in self.emitters:
            raise ValueError("Unknown emitter version: {0}".format(version))
        self.emitter = self.emitters[version](url, tags, auth)

    def handleError(self, record):  # noqa: N802
        """Close emitter and let default handler take actions on error."""
        self.emitter.close()
        super().handleError(record)

    def emit(self, record):
        """Send log record to Loki."""
        # noinspection PyBroadException
        try:
            self.emitter(record, self.format(record))
        except Exception:
            self.handleError(record)
