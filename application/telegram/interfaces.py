from aiogram import types


class SubscriberIogramInterface:

    async def handler(self, _event: types.Message)-> None:
        raise NotImplementedError
    
    def command(self)-> str:
        raise NotImplementedError
