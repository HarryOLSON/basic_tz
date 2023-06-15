from app import App
import asyncio


if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    app = App()

    loop.run_until_complete(app.load_files())

    loop.close()
