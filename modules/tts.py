"""
文字转语音模块 - 基于 edge-tts
使用微软 Edge 在线神经语音，免费、音质好，无需 API Key。
注意：此模块需要联网（调用微软接口），但不需要任何密钥。
"""
from __future__ import annotations
import asyncio
import os
import tempfile

# 常用中文语音，可在界面下拉选择
CHINESE_VOICES = {
    "晓晓 (女, 温柔)": "zh-CN-XiaoxiaoNeural",
    "云希 (男, 沉稳)": "zh-CN-YunxiNeural",
    "云扬 (男, 新闻)": "zh-CN-YunyangNeural",
    "晓伊 (女, 活泼)": "zh-CN-XiaoyiNeural",
    "晓秋 (女, 成熟)": "zh-CN-XiaoqiuNeural",
    "云龙 (男, 解说)": "zh-CN-YunlongNeural",
}


async def _tts_async(text: str, voice: str, output_path: str):
    import edge_tts
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(output_path)


def text_to_speech(text: str, voice_label: str = "晓晓 (女, 温柔)") -> str:
    """
    把文字转成语音 MP3。

    Args:
        text: 要朗读的文字
        voice_label: 语音显示名（见 CHINESE_VOICES）

    Returns:
        生成的 MP3 文件路径
    """
    if not text or not text.strip():
        return ""

    voice = CHINESE_VOICES.get(voice_label, "zh-CN-XiaoxiaoNeural")

    output_path = os.path.join(
        tempfile.gettempdir(),
        f"aitts_{abs(hash(text + voice)) % 10**8}.mp3",
    )

    asyncio.run(_tts_async(text, voice, output_path))
    return output_path
