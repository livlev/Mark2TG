# Mark2TG

[![PyPI](https://img.shields.io/pypi/v/mark2tg?color=blue)](https://pypi.org/project/mark2tg/)
[![License](https://img.shields.io/badge/license-MIT-green)](https://github.com/yourusername/mark2tg/blob/main/LICENSE)
[![Python](https://img.shields.io/badge/python-3.7%2B-blue)](https://www.python.org/)

**Mark2TG** is a lightweight Python library for converting Markdown to Telegram formatting. It supports all major Markdown features, including headings, bold, italic, strikethrough, links, code blocks, lists, tables, and more. Perfect for generating Telegram messages from Markdown content!

---

## Features

- **Headings**: Convert `# Heading` to `*Heading*` (supports h1-h6).
- **Bold**: Convert `**bold**` to `*bold*`.
- *Italic*: Convert `*italic*` to `_italic_`.
- ~~Strikethrough~~: Convert `~~strikethrough~~` to `~strikethrough~`.
- [Links](https://example.com): Convert `[link](https://example.com)` to `[link](https://example.com)`.
- **Code**: Convert ``` `code` ``` to ``` `code` ```.
- **Blockquotes**: Convert `> quote` to `┃ quote`.
- **Spoilers**: Convert `||spoiler||` to `||spoiler||`.
- **Lists**:
  - Unordered: Convert `- item` to `• item`.
  - Ordered: Convert `1. item` to `1. item`.
- **Tables**: Convert tables to code blocks for better readability in Telegram.

---

## Installation

Install **Mark2TG** via pip:

```bash
pip install mark2tg