from fastapi import HTTPException

async def check_users(data, id=None):
    if not data:
        message = {"error": f'user not found'}
        if not id is None:
            message = {"error": f"user with id '{id}' not found"}
        raise HTTPException(
            404, 
            detail=message
            )