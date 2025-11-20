import sys

try:
    from flask import Flask, request, jsonify, render_template
except Exception as e:
    # Friendly diagnostic when Flask is not available
    print("ERROR: Flask is not installed in this Python environment.")
    try:
        import sys as _sys
        print(f"Python executable: {_sys.executable}")
        print("Install Flask into this interpreter with:")
        print(f'  "{_sys.executable}" -m pip install -r "{__import__("os").path.join(__import__("os").getcwd(), "requirements.txt")}"')
        print("Or:")
        print(f'  "{_sys.executable}" -m pip install Flask')
    except Exception:
        # fallback message
        print("Install it with: pip install -r requirements.txt\nOr: pip install Flask")
    sys.exit(1)

from datetime import datetime

app = Flask(__name__)

# in-memory history (reset when the server restarts)
history = []

# The HTML UI is served from templates/index.html using Flask's template system.


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/save', methods=['POST'])
def save():
    try:
        payload = request.get_json(force=True)
    except Exception:
        return jsonify({'error': 'invalid json'}), 400

    expression = payload.get('expression') if payload else None
    result = payload.get('result') if payload else None
    if not expression or result is None:
        return jsonify({'error': 'missing fields'}), 400

    # minimal server-side validation
    if not isinstance(expression, str) or not isinstance(result, str):
        return jsonify({'error': 'invalid types'}), 400

    timestamp = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')
    entry = {'timestamp': timestamp, 'expression': expression, 'result': result}
    history.append(entry)

    return jsonify({'status': 'ok', 'timestamp': timestamp}), 201


@app.route('/history', methods=['GET'])
def get_history():
    return jsonify({'history': history})


if __name__ == '__main__':
    # Development server; not for production use
    # Optionally open the app in the default browser. Set AUTO_OPEN_BROWSER=0 to disable.
    import threading, webbrowser, os

    def _open_browser():
        webbrowser.open_new("http://127.0.0.1:5000")

    if os.environ.get('AUTO_OPEN_BROWSER', '1') != '0':
        threading.Timer(1.0, _open_browser).start()

    app.run(debug=True)
