from fastapi import HTTPException

async def check_users(data, your_id=None):
    if not data:
        message = {"error": f'user not found'}
        if not your_id is None:
            message = {"error": f"user with id '{your_id}' not found"}
        raise HTTPException(
            404, 
            detail=message
            )