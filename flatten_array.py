import sys
import logging
import json

import constants as c

log = logging.getLogger()

def setup_log():
    log.setLevel(c.LOG_LEVEL)
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s]: %(message)s"))
    log.addHandler(handler)

def convert_string_array(s):
    array_input = json.loads(s)
    log.info('Array to flatten inserted as parameter: ' + str(array_input))
    return array_input

def get_array_to_flatten():
    try:
        return convert_string_array(sys.argv[1])
    except IndexError:
        log.info('Array to flatten not inserted as parameters. I use the default: ' + str(c.DEFAULT_ARRAY))
        return c.DEFAULT_ARRAY
    except ValueError:
        log.error('Error during parsing the input array. Please check it.')
        log.error('Possible causes: param not string; bad formatted array.')
        return ''
#       exit(-1)

def modify_array(array_to_flatten, array_flattened):
    for element in array_to_flatten:
        if isinstance(element, list):
            log.info('Element ' + str(element) + ' is an array so I go deeper inside.')
            modify_array(element, array_flattened)
        else:
            log.info('Element ' + str(element) + ' is a primitive so I add it to the final array.')
            array_flattened.append(element)

def main():
    array_final = []
    array_to_flatten = get_array_to_flatten()
    if array_to_flatten:
        modify_array(array_to_flatten, array_final)
        log.info('Array flattened: ' + str(array_final))
    return array_final #for unit tests

if __name__ == "__main__":
    setup_log()
    main()
