from backend.api.tweets import router as router_tweets
from backend.api.users import router as router_users
from backend.api.medias import router as router_medias

all_routers = [
    router_tweets,
    router_users,
    router_medias
]