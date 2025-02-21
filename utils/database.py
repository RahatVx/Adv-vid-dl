from motor.motor_asyncio import AsyncIOMotorClient
from datetime import datetime

class Database:
    def __init__(self):
        self.client = AsyncIOMotorClient(Config.MONGO_URI)
        self.db = self.client.get_database()
        self.users = self.db.users

    async def add_user(self, user_id: int):
        await self.users.update_one(
            {"_id": user_id},
            {"$setOnInsert": {
                "downloads": 0,
                "last_download": None,
                "joined": datetime.now()
            }},
            upsert=True
        )

    async def update_user(self, user_id: int):
        await self.users.update_one(
            {"_id": user_id},
            {"$inc": {"downloads": 1}, "$set": {"last_download": datetime.now()}}
        )

    async def total_users(self):
        return await self.users.count_documents({})

    async def total_downloads(self):
        result = await self.users.aggregate([
            {"$group": {"_id": None, "total": {"$sum": "$downloads"}}}
        ]).to_list(length=1)
        return result[0]['total'] if result else 0

    async def get_all_users(self):
        return self.users.find({})
