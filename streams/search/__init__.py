import providers

def do(term):
    """Gets movies matching term from all providers
    
    Args:
        term (string): the search term to submit to providers
    
    Returns: 
        A list of Movie objects fetched from all providers
    """
    results = []

    for provider in providers.provider_list():

        provider_results = []

        try:
            provider_results = provider.do_search(term)
        except Exception as exc:
            print 'Cannot get results from {0}: {1}'.format(provider.name, exc)
            continue

        results += provider_results

    return results