from backend.repositories.tweets import TweetsRepository
from backend.schemas.tweets import CreateTweetSchema


class TweetsService:
    # def __init__(self, tweets_repo: TweetsRepository):
    def __init__(self, tweets_repo: TweetsRepository):
        self.tweets_repo = tweets_repo

    async def create_tweet(self, tweet: CreateTweetSchema):
        tweets_dict = tweet.model_dump()
        created_tweet = await self.tweets_repo.create_tweet(tweets_dict)
        return created_tweet
