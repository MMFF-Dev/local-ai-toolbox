"""
Local AI Toolbox - 一键启动本地 AI 工具箱
启动后浏览器自动打开 http://127.0.0.1:7860
"""
from __future__ import annotations
import gradio as gr

from modules.transcribe import transcribe_audio
from modules.remove_bg import remove_background
from modules.tts import text_to_speech, CHINESE_VOICES


CUSTOM_CSS = """
#header { text-align: center; margin-bottom: 10px; }
#header h1 { font-size: 1.8rem; margin-bottom: 4px; }
#header p { color: #666; }
"""


def build_ui() -> gr.Blocks:
    with gr.Blocks(css=CUSTOM_CSS, title="Local AI Toolbox", theme=gr.themes.Soft()) as demo:
        gr.HTML(
            """
            <div id="header">
                <h1>🧰 Local AI Toolbox</h1>
                <p>本地运行 · 无需 API Key · 一键启动的 AI 工具箱</p>
            </div>
            """
        )

        with gr.Tab("🎙️ 音频转文字"):
            gr.Markdown("上传音频文件，自动转写为文字，并生成 SRT 字幕。首次使用会自动下载模型（约 460MB）。")
            with gr.Row():
                with gr.Column():
                    audio_in = gr.Audio(label="上传音频", type="filepath")
                    model_size = gr.Dropdown(
                        choices=["tiny", "base", "small", "medium"],
                        value="small",
                        label="模型大小（越大越准越慢）",
                    )
                    lang = gr.Dropdown(
                        choices=["auto", "zh", "en", "ja", "ko"],
                        value="auto",
                        label="语言",
                    )
                    btn1 = gr.Button("开始转写", variant="primary")
                with gr.Column():
                    text_out = gr.Textbox(label="转写结果", lines=12)
                    srt_out = gr.Textbox(label="SRT 字幕", lines=8)
            btn1.click(
                fn=transcribe_audio,
                inputs=[audio_in, model_size, lang],
                outputs=[text_out, srt_out],
            )

        with gr.Tab("🖼️ 图片去背景"):
            gr.Markdown("上传图片，自动去除背景，输出透明底 PNG。首次使用会自动下载模型（约 170MB）。")
            with gr.Row():
                with gr.Column():
                    img_in = gr.Image(label="上传图片", type="filepath")
                    btn2 = gr.Button("去除背景", variant="primary")
                with gr.Column():
                    img_out = gr.Image(label="透明底结果", type="pil")
            btn2.click(fn=remove_background, inputs=img_in, outputs=img_out)

        with gr.Tab("🔊 文字转语音"):
            gr.Markdown("输入文字，选择语音，生成 MP3。使用微软 Edge 神经语音，免费且音质好（需联网）。")
            with gr.Row():
                with gr.Column():
                    tts_text = gr.Textbox(
                        label="输入文字",
                        lines=6,
                        placeholder="在这里输入要朗读的文字...",
                    )
                    voice = gr.Dropdown(
                        choices=list(CHINESE_VOICES.keys()),
                        value=list(CHINESE_VOICES.keys())[0],
                        label="选择语音",
                    )
                    btn3 = gr.Button("生成语音", variant="primary")
                with gr.Column():
                    audio_out = gr.Audio(label="生成的 MP3", type="filepath")
            btn3.click(fn=text_to_speech, inputs=[tts_text, voice], outputs=audio_out)

        gr.HTML(
            """
            <div style="text-align:center;color:#999;font-size:0.85rem;margin-top:20px;">
                ⭐ 如果这个项目帮到你，欢迎在 GitHub 上点个 Star<br>
                本地运行 · 隐私安全 · 免费开源
            </div>
            """
        )

    return demo


if __name__ == "__main__":
    demo = build_ui()
    demo.launch(server_name="127.0.0.1", server_port=7860, inbrowser=True)
