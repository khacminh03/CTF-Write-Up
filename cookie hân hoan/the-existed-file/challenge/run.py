from flask import Flask, request, render_template_string
import os
import subprocess
import string

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    result = ""
    file_path = None
    if request.method == "POST":
        file_path = request.form.get("file_path")
        file_path = file_path.translate({ord(c): None for c in string.whitespace})

        # Blacklist filter
        blacklisted = [";", "&", "|", "&&", "cat", "head", "tail", "zip", "base64", "bash", "sh", "python", "`"]
        is_blacklisted = any(bl in file_path for bl in blacklisted)

        if is_blacklisted:
            result = "Blacklist characters detected!"
        else:
            try:
                command = f"ls -l {file_path}"
                result = subprocess.check_output(command, shell=True).decode()
                if result:
                    result = 'File is existed!'
            except Exception as e:
                result = 'File is not existed'

    return render_template_string('''
    <b>Enter the file path to check if it exists:</b><br>

    <form method="post">        
        <input type="text" id="file_path" name="file_path" value="/etc/passwd">
        <input type="submit" value="Submit">
    </form>
    {% if file_path %}
        <b> Checking {{file_path }}</b><br></br>
    {% endif %}
    <pre>{{ result }}</pre>
    ''', result=result, file_path=file_path)


if __name__ == "__main__":
    app.run("0.0.0.0", 1337)
