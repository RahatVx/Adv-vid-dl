import time
from pyrogram.types import Message

class Progress:
    def __init__(self, message: Message):
        self.message = message
        self.start_time = time.time()
        
    async def update(self, current, total):
        try:
            speed = current / (time.time() - self.start_time)
            percent = current * 100 / total
            eta = (total - current) / speed
            
            progress_bar = "⬢" * int(percent//5) + "⬡" * (20 - int(percent//5))
            
            text = (
                f"**📥 Downloading...**\n\n"
                f"**Progress:** {percent:.1f}%\n"
                f"**Speed:** {self.sizeof_fmt(speed)}/s\n"
                f"**ETA:** {self.timefmt(eta)}\n"
                f"{progress_bar}"
            )
            
            await self.message.edit_text(text)
        except Exception as e:
            print(f"Progress error: {e}")

    @staticmethod
    def sizeof_fmt(num):
        for unit in ['B', 'KB', 'MB', 'GB']:
            if abs(num) < 1024.0:
                return f"{num:.1f} {unit}"
            num /= 1024.0
        return f"{num:.1f} TB"

    @staticmethod
    def timefmt(seconds):
        minutes, seconds = divmod(int(seconds), 60)
        hours, minutes = divmod(minutes, 60)
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
