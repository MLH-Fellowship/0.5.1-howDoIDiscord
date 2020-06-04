import re

def _set_params(query):

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
        'gall': 'all'
    }

    aliases = list(filter(lambda x: x in query['query'], MAPPINGS))
    params = list(map(MAPPINGS.get, aliases))
    if not params: 
        query['query'] = query['query'].strip().split(' ')
        DEFAULT.update(query)
    else: 
        regex= r'|'.join(map(r'{}'.format, aliases))
        query['query'] = re.sub(regex, '', query['query']).strip().split(' ')
        updated_params = { **query, **dict(zip(params, [True] * len(params)))}
        DEFAULT.update(updated_params)

    return DEFAULT 