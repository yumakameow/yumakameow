from hikkatl.types import Message
from .. import loader


@loader.tds
class FullInfo(loader.Module):
    """Full Info"""
    strings = {"name": "Full Information", "fullinfo": "<code>raspberry@ymkxyumaka</code>\n🌒 <b><u>Hikka Userbot</u></b>\n\n🤵 <b>Owner:</b> <a href="https://t.me/YumakaLukasz">yumaka</a>\n🧠 <b>Branch:</b> <code>master</code>\n⌨️ <b>Prefix:</b> «<code>.</code>»\n🐻 <b>Actual Version</b>\n\n🐍 <b>Python:</b> <code>Actual Version</code>\n💿 <b>CPU Usage:</b> <i>~0.2%</i>\n🌥 <b>RAM Usage:</b> <i>~398.5 MB</i>\n\n🍎 <b>FFMPEG:</b> <code>True</code>\n🍾 <b>Telethon-Mod</b>: <code>True</code>\n<code>💜 Raspberry | Raspberry Pi4 B Plus Rev 12GB</code>",parse_mode='html'}
    
    async def fullinfo(self, message: Message):
        """Info your server"""
        await utils.answer(message, self.strings("fullinfo"))
