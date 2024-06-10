from typing import List


def paginated_menu(offset: int, limit: int, menu_lenght: int) -> List[str]:
    if offset == 1:
        return ['⏩ next', '🏠 Home']
            
    elif offset+limit >= menu_lenght:
        return ['⏪ Previous', '🏠 Home']

    else:
        return ['⏪ Previous', '⏩ next', '🏠 Home']