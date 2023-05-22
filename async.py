import asyncio
import pyautogui as p
import threading

def move_mouse():
    p.moveTo(500, 500, duration=3)

async def function_1():
    for i in range(10):
        print('function_1 =>', i)
        await asyncio.sleep(0.3)

async def main():
    await asyncio.sleep(0)  # 이벤트 루프를 활성화하기 위해 잠시 대기
    t = threading.Thread(target=move_mouse)
    t.start()

    await function_1()

    t.join()

asyncio.run(main())
