# Clipboard Monitor 🖨️

[![Python 3.7+](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Windows平台的剪贴板历史记录工具，精准追踪每一次复制操作，生成结构化日志文件。

## ✨ 核心特性

- **精准监控**  
  采用Windows消息机制监听剪贴板更新事件（非轮询），CPU占用率<0.1%
- **智能去重**  
  SHA-256哈希比对技术，避免重复记录相同内容
- **来源追踪**  
  自动捕获复制来源的应用程序窗口标题
- **日志管理**  
  - 按天自动分割日志文件（`clipboard_YYYYMMDD.log`）
  - 默认保存至`./logs`目录
- **即装即用**  
  无需复杂配置，单文件运行支持

## 🚀 快速开始

### 环境要求
- Windows 7/10/11
- Python 3.7+

### 安装步骤
```bash
# 克隆仓库
git clone https://github.com/yourusername/clipboard-monitor.git

# 安装依赖
pip install -r requirements.txt
```

### 运行监控
```bash
python clipboard_monitor.py
```

## ⚙️ 配置选项

通过环境变量自定义行为：
```bash
# 修改日志保存路径（默认./logs）
export CLIPBOARD_LOG_DIR="D:/clip_logs"

# 设置检查间隔（秒，默认1）
export CHECK_INTERVAL=0.5

# 启用敏感词过滤（逗号分隔）
export BLACKLIST_KEYWORDS="password,secret"
```

## 📂 日志格式示例
```log
[2024-02-23 14:30:22] [Visual Studio Code] import numpy as np
[2024-02-23 14:31:45] [Microsoft Word] 项目需求文档草案
[2024-02-23 14:32:17] [Chrome] https://github.com
```

## 🛠️ 开发指南

### 项目结构
```
.
├── src/                 # 源代码
│   ├── monitor.py       # 剪贴板监控核心
│   └── logger.py        # 日志管理模块
├── logs/                # 日志存储目录
├── requirements.txt     # 依赖清单
└── README.md            # 项目文档
```

### 构建可执行文件
```bash
pip install pyinstaller
pyinstaller --onefile --icon=icon.ico src/clipboard_monitor.py
```

## 🤝 贡献指南

欢迎通过Issue提交建议或PR参与开发！  
请遵循以下流程：
1. Fork本仓库
2. 创建功能分支（`git checkout -b feature/xxx`）
3. 提交修改（`git commit -am 'Add some feature'`）
4. 推送分支（`git push origin feature/xxx`）
5. 新建Pull Request

## 📜 许可证

本项目基于 [MIT License](LICENSE) 授权，允许自由使用与修改。核心要求：
- 保留原始版权声明
- 明确标注修改内容

---

> 由Hao430开发 · 反馈建议请提交至 [Issues](https://github.com/yourusername/clipboard-monitor/issues)