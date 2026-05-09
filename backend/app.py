from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__, template_folder="frontend", static_folder="static")

# ─────────────────────────────────────────────
# Existing routes
# ─────────────────────────────────────────────

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return "<h2>About the Program</h2><p>A 2-day full-stack bootcamp covering HTML, CSS, Python, SQL, and deployment.</p>"


@app.route("/register", methods=["POST"])
def register():
    full_name = request.form.get("full_name", "").strip()
    email = request.form.get("email", "").strip().lower()
    course = request.form.get("course", "")
    enroll_date = request.form.get("enroll_date", "")
    phone = request.form.get("phone", "").strip()
    remarks = request.form.get("remarks", "").strip()

    errors = []
    if not full_name or len(full_name) < 2:
        errors.append("Full name must be at least 2 characters.")
    if not email or "@" not in email:
        errors.append("Valid email address is required.")
    if not course:
        errors.append("Please select a course.")

    if errors:
        return (
            f"<h2>Validation Failed</h2><ul>{''.join(f'<li>{e}</li>' for e in errors)}</ul><a href='/'>Go Back</a>",
            400,
        )

    submission_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"NEW REGISTRATION: {full_name} | {email} | {course} | {enroll_date} | {phone}")

    return f"""
        <h2>Registration Successful!</h2>
        <p>Thank you, <strong>{full_name}</strong>!</p>
        <p><strong>Email:</strong> {email}<br>
        <strong>Course:</strong> {course}<br>
        <strong>Enrollment:</strong> {enroll_date or 'Not specified'}<br>
        <strong>Submitted:</strong> {submission_time}</p>
        <hr>
        <p><em>Remarks:</em> {remarks if remarks else 'None provided'}</p>
        <a href="/"><button>Register Another Student</button></a>
    """, 200


# ─────────────────────────────────────────────
# Bonus Task 3 – Custom /intro endpoint
# Using a wrapper function as instructed
# ─────────────────────────────────────────────

def create_intro_route(flask_app):
    """Wrapper function that registers the /intro route on the given Flask app."""

    @flask_app.route("/intro")
    def intro():
        html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>About Me – Sai Ram</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --accent: #6366f1;
            --accent2: #ec4899;
            --bg: #0f0f1a;
            --card: #1a1a2e;
            --text: #e2e8f0;
            --muted: #94a3b8;
        }
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Inter', sans-serif;
            background: var(--bg);
            color: var(--text);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 2rem;
            background-image:
                radial-gradient(ellipse at 20% 50%, rgba(99,102,241,0.15) 0%, transparent 60%),
                radial-gradient(ellipse at 80% 20%, rgba(236,72,153,0.1) 0%, transparent 50%);
        }
        .card {
            background: var(--card);
            border: 1px solid rgba(99,102,241,0.25);
            border-radius: 24px;
            padding: 3rem 3.5rem;
            max-width: 560px;
            width: 100%;
            text-align: center;
            box-shadow: 0 25px 60px rgba(0,0,0,0.5), 0 0 0 1px rgba(255,255,255,0.04);
            animation: fadeUp 0.7s ease both;
        }
        @keyframes fadeUp {
            from { opacity:0; transform: translateY(30px); }
            to   { opacity:1; transform: translateY(0);    }
        }
        .avatar-wrap {
            position: relative;
            display: inline-block;
            margin-bottom: 1.75rem;
        }
        .avatar-wrap::before {
            content: '';
            position: absolute;
            inset: -4px;
            border-radius: 50%;
            background: linear-gradient(135deg, var(--accent), var(--accent2));
            z-index: 0;
            animation: spin 6s linear infinite;
        }
        @keyframes spin {
            to { transform: rotate(360deg); }
        }
        .avatar-wrap a {
            display: block;
            position: relative;
            z-index: 1;
            border-radius: 50%;
            overflow: hidden;
            width: 180px;
            height: 180px;
            border: 4px solid var(--card);
        }
        /* ---- using href on the <a> tag around the image as hinted ---- */
        .avatar-wrap a img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            object-position: top;
            display: block;
            transition: transform 0.4s ease;
        }
        .avatar-wrap a:hover img {
            transform: scale(1.07);
        }
        h1 {
            font-size: 2rem;
            font-weight: 700;
            background: linear-gradient(90deg, var(--accent), var(--accent2));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 0.4rem;
        }
        .role {
            color: var(--muted);
            font-size: 0.95rem;
            letter-spacing: 0.05em;
            text-transform: uppercase;
            margin-bottom: 1.5rem;
        }
        .bio {
            color: var(--text);
            line-height: 1.75;
            font-size: 1rem;
            margin-bottom: 2rem;
        }
        .tags {
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
            justify-content: center;
            margin-bottom: 2rem;
        }
        .tag {
            background: rgba(99,102,241,0.15);
            border: 1px solid rgba(99,102,241,0.35);
            color: #a5b4fc;
            padding: 0.3rem 0.85rem;
            border-radius: 999px;
            font-size: 0.8rem;
            font-weight: 500;
        }
        .back-link {
            display: inline-block;
            margin-top: 0.5rem;
            padding: 0.7rem 1.8rem;
            border-radius: 999px;
            background: linear-gradient(135deg, var(--accent), var(--accent2));
            color: #fff;
            text-decoration: none;
            font-weight: 600;
            font-size: 0.9rem;
            transition: opacity 0.2s, transform 0.2s;
            box-shadow: 0 4px 18px rgba(99,102,241,0.4);
        }
        .back-link:hover { opacity: 0.88; transform: translateY(-2px); }
    </style>
</head>
<body>
    <div class="card">
        <div class="avatar-wrap">
            <!-- href attribute used on the image anchor as per the hint -->
            <a href="/static/profile.png" target="_blank">
                <img src="/static/profile.png" alt="Sai Ram – profile photo">
            </a>
        </div>

        <h1>Hey, I'm Sai Ram! 👋</h1>
        <p class="role">Full-Stack Developer &amp; Python Enthusiast</p>

        <p class="bio">
            I'm a passionate developer who loves building real-world web applications
            with Python &amp; Flask on the backend and clean, responsive HTML/CSS on the
            frontend. Currently sharpening my skills through hands-on bootcamps and
            open-source projects.
        </p>

        <div class="tags">
            <span class="tag">Python</span>
            <span class="tag">Flask</span>
            <span class="tag">HTML &amp; CSS</span>
            <span class="tag">SQL</span>
            <span class="tag">Git &amp; GitHub</span>
        </div>

        <a class="back-link" href="/">← Back to Registration</a>
    </div>
</body>
</html>"""
        return html

# Register the route via the wrapper
create_intro_route(app)


if __name__ == "__main__":
    app.run(debug=True, port=8000)