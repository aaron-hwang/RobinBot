from random import choice, random

def get_response(input: str) -> str:
    lowered: str = input.lower()

    if lowered == '':
        return 'Fuck you'
    elif "robifly" in lowered:
        return 'Did someone say robifly?'   
    else:
        return 'Test'