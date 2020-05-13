import sys
import logging


_logger = logging.getLogger(__name__)


def paramArgsSimple():
    if len(sys.argv) > 1:
        _logger.info("Parse arguments: " +str(sys.argv))

        if str(sys.argv[1]) in ('INFO', 'info'):
            return 20
        if str(sys.argv[1]) in ('debug', 'DEBUG'):
            return 10
    return 20

def paramArgsAdvanced():
    pass