"""
图片去背景模块 - 基于 rembg (U2-Net)
首次运行自动下载模型（约 170MB），之后本地运行。
"""
from __future__ import annotations
import io
import os
from PIL import Image

_session = None


def _get_session():
    global _session
    if _session is None:
        from rembg import new_session
        _session = new_session("u2net")
    return _session


def remove_background(image_path: str) -> Image.Image:
    """
    去除图片背景，返回带透明通道的 PNG。

    Args:
        image_path: 输入图片路径（jpg/png/webp 等）

    Returns:
        PIL Image (RGBA)
    """
    if not image_path or not os.path.exists(image_path):
        # 返回一张 1x1 透明图，避免 Gradio 报错
        return Image.new("RGBA", (1, 1), (0, 0, 0, 0))

    from rembg import remove
    session = _get_session()

    with open(image_path, "rb") as f:
        input_bytes = f.read()

    output_bytes = remove(input_bytes, session=session)
    img = Image.open(io.BytesIO(output_bytes)).convert("RGBA")
    return img
