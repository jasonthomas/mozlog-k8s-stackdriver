import logging.config
import random
import _thread
import time

cfg = {
    'version': 1,
    'formatters': {
        'json': {
            '()': 'dockerflow.logging.JsonLogFormatter',
            'logger_name': 'myfancyproject'
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'json'
        },
    },
    'loggers': {
        'myfancyproject': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    }
}

logging.config.dictConfig(cfg)
logger = logging.getLogger('myfancyproject')


def load_words():
    with open('words.txt') as fp:
        words = fp.readlines()
    return [e.strip() for e in words]


def random_message(words, len=1):
    return ' '.join(random.sample(words, len))


def run(words):
    extra_fields = {}
    for n in range(6):
        extra_fields['field%s' % n] = random_message(words)
    logger.info(random_message(words, 10), extra=extra_fields)


while True:
    words = load_words()
    for n in range(5):
        _thread.start_new_thread(run, (words,))
    time.sleep(.1)
