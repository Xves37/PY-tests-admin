"""HTML patterns.

This module has html components to create web pages.
"""


def search_header(header):
    """Search header (from Doctype to container open tag)"""
    return u"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>{header}</title>
    <link rel="stylesheet" href="../css/main.css">
</head>
<body>
    <h1>{header}</h1>
    <h2>Поиск по вопросам</h2>
    <div class='input-wrap'>
        <input id='filter-input' type='text' placeholder="Введите начало вопроса">
    </div>
    <div id='container'>""".format(header=header)


def search_footer():
    """Search footer (from container close tag to close html tag)"""
    return """
    </div>
    <script src="../js/jquery-3.3.1.min.js"></script>
    <script src="../js/main.js"></script>
</body>
</html>"""


def search_item(item):
    """One search item(question + answer)."""
    return """
        <p class="hidden">
            <span class="question">
                {question}
            </span>
            <span class="answer">
                {answer}
            </span>
        </p>""".format(question=item['question'], answer=item['answer'][0])
