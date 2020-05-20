from sys import platform
import logging
import os


def configure_logging(mode):

    if platform == "win32":
        logpath = "TechDraw3D/logs/debug.log"
    
    if platform == "linux":
        logpath = "logs/debug.log"

    try:
        logging.basicConfig(level=mode,
            format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
            datefmt='%m-%d %H:%M',
            filename=logpath,
            filemode='a')

    except FileNotFoundError as e:
        if not os.path.isdir(logpath[:-10]):
            os.mkdir(logpath[:-10])

        open(logpath, 'a').close()

        logging.basicConfig(level=mode,
            format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
            datefmt='%m-%d %H:%M',
            filename=logpath,
            filemode='a')

    # define a Handler which writes INFO messages or higher to the sys.stderr
    console = logging.StreamHandler()
    console.setLevel(mode)
    # set a format which is simpler for console use
    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    # tell the handler to use this format
    console.setFormatter(formatter)
    # add the handler to the root logger
    logging.getLogger('').addHandler(console)


