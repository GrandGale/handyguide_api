from app.config.database import DBBase


def paginate(qs: DBBase, page: int, size: int):
    """This function is used to paginate a query.

    Args:
        qs (Query): The query to paginate
        page (int): The current page
        size (int): The number of items per page

    Returns:
        dict: A dictionary containing the paginated response

    Sample:
        {
            "page": 1,
            "size": 10,
            "count": 10,
            "items": []
        }
    """
    items = qs.limit(size).offset(size * (page - 1)).all()
    response = {
        "page": page,
        "size": size,
        "count": len(items),
        "items": items,
    }
    return response
