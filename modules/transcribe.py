"""
音频转文字模块 - 基于 faster-whisper
首次运行会自动下载模型（small 约 460MB），之后完全本地运行。
"""
from __future__ import annotations
import os
import tempfile
from typing import Tuple

# 模型懒加载：第一次调用才初始化，避免启动慢
_model = None


def _get_model(model_size: str = "small"):
    global _model
    if _model is None or _model_size != model_size:
        from faster_whisper import WhisperModel
        # int8 量化：CPU 也能跑得动，显存/内存占用最小
        _model = WhisperModel(model_size, device="cpu", compute_type="int8")
        _model_size = model_size
    return _model


_model_size = "small"


def transcribe_audio(
    audio_path: str,
    model_size: str = "small",
    language: str = "auto",
) -> Tuple[str, str]:
    """
    把音频文件转成文字。

    Args:
        audio_path: 音频文件路径（wav/mp3/m4a/flac 等）
        model_size: tiny/base/small/medium/large-v1/v2，越大越准越慢
        language: 语言代码，"auto" 为自动检测

    Returns:
        (转录文本, 带时间戳的 SRT 字幕文本)
    """
    if not audio_path or not os.path.exists(audio_path):
        return "⚠️ 请先上传音频文件", ""

    model = _get_model(model_size)

    lang = None if language in ("auto", "自动检测", "") else language

    segments, info = model.transcribe(
        audio_path,
        language=lang,
        beam_size=5,
        vad_filter=True,  # 自动跳过静音段，提速
    )

    lines = []
    srt_lines = []
    for i, seg in enumerate(segments, start=1):
        text = seg.text.strip()
        lines.append(text)
        # 生成 SRT
        start = _format_timestamp(seg.start)
        end = _format_timestamp(seg.end)
        srt_lines.append(f"{i}\n{start} --> {end}\n{text}\n")

    full_text = "\n".join(lines)
    srt_text = "\n".join(srt_lines)

    detected = f"[检测到语言: {info.language}, 概率 {info.language_probability:.2f}]\n\n"
    return detected + full_text, srt_text


def _format_timestamp(seconds: float) -> str:
    """秒数转 SRT 时间戳 HH:MM:SS,mmm"""
    ms = int((seconds - int(seconds)) * 1000)
    s = int(seconds)
    h, rem = divmod(s, 3600)
    m, sec = divmod(rem, 60)
    return f"{h:02d}:{m:02d}:{sec:02d},{ms:03d}"
