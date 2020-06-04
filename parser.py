import re

DEFAULT = {
    'query': '',
    'num_answers': 1,
    'pos': 1,
    'all': False,
    'link': False,
    'clear_cache': True,
    'version': False,
    'color': False
}

MAPPINGS = {
    'glink': 'link',
    'gall':'all'
}

def _set_params(query):
    if(DEFAULT['clear_cache']):
        print("CACHE SHOULD BE CLEARED")
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

    print(DEFAULT)
    return DEFAULT 