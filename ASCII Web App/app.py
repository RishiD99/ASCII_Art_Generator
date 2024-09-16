from flask import Flask, render_template, request, redirect, url_for
from markupsafe import Markup
import os
from ASCII_Art_Generator import color_ascii_Generator  # Your ASCII art generator

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

# Ensure the upload folder exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

def parse_ansi_to_html(text):
    # ANSI color parsing logic as from your JS code, but now in Python
    import re

    ansi_regex = re.compile(r'\033\[38;5;(\d+)m')
    result = ''
    last_index = 0

    matches = list(ansi_regex.finditer(text))

    for match in matches:
        result += escape_html(text[last_index:match.start()])
        color_code = int(match.group(1))
        result += f'<span style="color: {get_color(color_code)};">'
        last_index = match.end()

    result += escape_html(text[last_index:])
    result = result.replace('\033[0m', '</span>')  # Reset ANSI color codes

    return result

def get_color(code):
    # Same color code logic as in your JS
    if code < 16:
        colors = [
            '#000000', '#800000', '#008000', '#808000', '#000080', '#800080', '#008080', '#c0c0c0',
            '#808080', '#ff0000', '#00ff00', '#ffff00', '#0000ff', '#ff00ff', '#00ffff', '#ffffff'
        ]
        return colors[code]
    elif code < 232:
        r = (code - 16) // 36
        g = ((code - 16) % 36) // 6
        b = (code - 16) % 6
        return f'rgb({r * 51}, {g * 51}, {b * 51})'
    else:
        gray = (code - 232) * 10 + 8
        return f'rgb({gray}, {gray}, {gray})'

def escape_html(text):
    return (text.replace('&', '&amp;')
                .replace('<', '&lt;')
                .replace('>', '&gt;')
                .replace('"', '&quot;')
                .replace("'", '&#39;'))

@app.route('/', methods=['GET', 'POST'])
def index():
    ascii_art = None
    if request.method == 'POST':
        if 'image' not in request.files:
            return redirect(request.url)

        image = request.files['image']
        
        if image.filename == '':
            return redirect(request.url)

        if image:
            # Save the image file
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
            image.save(image_path)

            # Call your external ASCII art generator function
            ascii_art_path = color_ascii_Generator(image_path)  # Your function

            # Read the generated ANSI ASCII art
            with open(ascii_art_path, 'r') as f:
                ansi_art = f.read()

            # Convert ANSI escape sequences to HTML
            ascii_art = parse_ansi_to_html(ansi_art)

    return render_template('index.html', ascii_art=Markup(ascii_art))

if __name__ == '__main__':
    app.run(debug=True)
