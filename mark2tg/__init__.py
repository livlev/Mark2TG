def convert_markdown_to_telegram(markdown_text):
    """
    Converts Markdown to Telegram formatting.
    Supports: headings, bold, italic, strikethrough, links, code,
    blockquotes, spoilers, lists, tables (as code blocks).
    """
    lines = markdown_text.split('\n')
    result = []

    for line in lines:
        # Process headings
        if line.startswith('#') and ' ' in line:
            line = f"*{line[line.find(' ') + 1:]}*"

        # Process bold and italic
        line = line.replace('**', '*').replace('__', '*').replace('*', '_', 1)

        # Process strikethrough
        line = line.replace('~~', '~')

        # Process links
        if '[' in line and ']' in line and '(' in line and ')' in line:
            start, end = line.find('['), line.find(']')
            url_start, url_end = line.find('(', end), line.find(')', line.find('(', end))
            if start < end < url_start < url_end:
                text, url = line[start + 1:end], line[url_start + 1:url_end]
                line = line[:start] + f"[{text}]({url})" + line[url_end + 1:]

        # Process inline code
        line = line.replace('`', '`')

        # Process blockquotes
        if line.startswith('> '):
            line = f"┃ {line[2:]}"

        # Process spoilers
        line = line.replace('||', '||')

        # Process unordered lists
        if line.startswith(('- ', '* ', '+ ')):
            line = f"• {line[2:]}"

        # Process ordered lists
        if line.lstrip()[:2].isdigit() and line.lstrip()[2] == '.':
            line = line.lstrip()

        # Process tables (convert to code block)
        if '|' in line and ('---' in line or '--' in line):
            result.append('```')
            result.append(line)
            continue
        elif '|' in line:
            result.append(line)
            continue

        result.append(line)

    return '\n'.join(result)