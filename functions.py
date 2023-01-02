import asyncio
from prisma import Prisma



async def data_transfer(currentGender, currentWeather, tops , outherwear, bottoms, shoes) -> None:
    db = Prisma()
    await db.connect()


    outfit = await db.outfit.create({
            'published': True,
            'gender': currentGender,
            'weather' : currentWeather,
            'tops' : tops,
            'outherwear' : outherwear,
            'bottoms' : bottoms,
            'shoes' : shoes,
        })

    print(f'created outfit: {outfit.json(indent=2, sort_keys=True)}')

    found = await db.outfit.find_unique(where={'id': outfit.id})
    assert found is not None
    print(f'found post: {found.json(indent=2, sort_keys=True)}')

    await db.disconnect()


if __name__ == '__main__':
    asyncio.run(data_transfer())