from fastapi import Header, HTTPException, Depends, status


def get_api_key(api_key: str = Header(...)):
    # Поменять эту заглушку, когда сделаю бд
    valid_api_keys = ["test", "user", "admin"]
    if api_key not in valid_api_keys:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API Key"
        )
    return api_key
