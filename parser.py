import re

def _set_params(query):

    curr = query['query'].strip().split(' ')

    DEFAULT = {
    'query': '',
    'num_answers': 1,
    'pos': 1,
    'all': False,
    'link': False,
    'clear_cache': False,
    'version': False,
    'color': False
    }

    MAPPINGS = {
        'glink': 'link',
        'gall': 'all',
        'gnum': 'num_answers'
    }

    if ('gnum' in curr):

        try:
            num = curr[curr.index('gnum') + 1]
        except:
            print("Ignoring parameter... End of sentence")
            curr.remove('gnum')
        else:
            if(num.isdigit()):
                DEFAULT.update({'num_answers': int(num)})
                curr.remove(num)
            print("Ignoring parameter... No value given")
            curr.remove('gnum')

    aliases = list(filter(lambda x: x in curr, MAPPINGS))
    params = list(map(MAPPINGS.get, aliases))

    if not params: 
        DEFAULT.update({'query':curr})
    else: 
        query['query'] = [word for word in curr if not word in aliases]
        updated_params = { **query, **dict(zip(params, [True] * len(params)))}
        DEFAULT.update(updated_params)

    return DEFAULT 