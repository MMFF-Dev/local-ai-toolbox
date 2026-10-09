<div align="center">

# 🧰 Local AI Toolbox

**一键启动的本地 AI 工具箱 · 无需 API Key · 隐私安全 · 免费开源**

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)](https://www.python.org/)
[![Gradio](https://img.shields.io/badge/Gradio-4.x-orange?logo=gradio)](https://www.gradio.app/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Stars](https://img.shields.io/github/stars/MMFF-Dev/local-ai-toolbox?style=social)](https://github.com/MMFF-Dev/local-ai-toolbox/stargazers)

</div>

---

## ✨ 这是什么？

一个**双击就能跑**的本地 AI 工具箱，把常用的 AI 能力打包成一个网页界面：

- 🎙️ **音频转文字** — 录音/视频一键转写，自动生成 SRT 字幕
- 🖼️ **图片去背景** — 上传图片，秒出透明底 PNG
- 🔊 **文字转语音** — 输入文字，生成自然的中文语音 MP3

**不需要 OpenAI API Key，不需要配置环境变量，不需要 GPU。** 模型首次运行自动下载，之后完全本地运行。

## 🎯 为什么做这个？

现在 AI 工具五花八门，但大多要么要注册账号、要么要充钱买 API、要么配置环境让人头大。
这个项目把最常用的 3 个能力打包成一个 `run.bat`，**双击就能用**。

## 🚀 快速开始

### Windows
```bat
:: 1. 确保已安装 Python 3.9+（https://www.python.org/downloads/）
:: 2. 双击 run.bat
run.bat
```

### macOS / Linux
```bash
chmod +x run.sh
./run.sh
```

启动后浏览器会自动打开 `http://127.0.0.1:7860`，开始使用。

> 💡 首次运行会自动下载依赖和模型（约 600MB），请耐心等待。之后启动会很快。

## 📸 界面预览

<!-- 截图占位：实际发布后替换为真实截图 -->
<!-- ![界面截图](docs/screenshot.png) -->

> 截图即将上线。运行后你会看到三个 Tab：音频转文字 / 图片去背景 / 文字转语音。

## 🧱 技术栈

| 功能 | 技术 | 说明 |
|---|---|---|
| Web UI | [Gradio 4](https://www.gradio.app/) | 一行代码启动网页界面 |
| 音频转文字 | [faster-whisper](https://github.com/SYSTRAN/faster-whisper) | 比 openai-whisper 快 4 倍，CPU 可跑 |
| 图片去背景 | [rembg](https://github.com/danielgatis/rembg) | 基于 U2-Net 模型 |
| 文字转语音 | [edge-tts](https://github.com/rany2/edge-tts) | 微软 Edge 神经语音，免费 |

## 📁 项目结构

```
local-ai-toolbox/
├── app.py              # Gradio Web UI 入口
├── requirements.txt    # Python 依赖
├── run.bat             # Windows 一键启动
├── run.sh              # Mac/Linux 一键启动
├── modules/
│   ├── transcribe.py   # 音频转文字
│   ├── remove_bg.py    # 图片去背景
│   └── tts.py          # 文字转语音
└── README.md
```

## ❓ 常见问题

**Q：需要联网吗？**
- 首次运行下载依赖和模型需要联网。
- 音频转文字、图片去背景之后完全本地运行。
- 文字转语音使用微软在线接口，需要联网（但不需要任何 Key）。

**Q：需要 GPU 吗？**
- 不需要。默认用 CPU + int8 量化，普通笔记本就能跑。
- 如果有 NVIDIA 显卡，可以自行修改 `transcribe.py` 里的 device 参数提速。

**Q：会上传我的数据吗？**
- 不会。除 TTS 外，所有数据处理都在你本机完成，文件不会上传到任何服务器。

**Q：支持哪些音频格式？**
- faster-whisper 支持 ffmpeg 能解析的所有格式：mp3/wav/m4a/flac/ogg/webm 等。

## 🗺️ Roadmap

- [x] 音频转文字（Whisper）
- [x] 图片去背景（U2-Net）
- [x] 文字转语音（Edge TTS）
- [ ] 图片超分辨率（Real-ESRGAN）
- [ ] 视频自动字幕
- [ ] PDF 文档摘要
- [ ] 本地 RAG 问答
- [ ] 打包成 exe / dmg，免 Python 环境

## 🤝 贡献

欢迎提 Issue 和 PR！建议先开 Issue 讨论你想加的功能。

## ☕ 支持这个项目

如果这个工具帮到了你，可以请作者喝杯咖啡，支持继续维护：

- 🌟 在 GitHub 点个 Star（免费，对我们帮助很大）
- [ ] GitHub Sponsors（即将上线）
- [ ] 爱发电（即将上线）

## 📄 License

[MIT](LICENSE)
