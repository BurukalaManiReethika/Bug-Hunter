from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

levels = [
    {
        "id": 1,
        "title": "LOGIN LOCKDOWN",
        "app": "Login Portal",
        "story": "The login accepts an empty password.",
        "bug": "Authentication bypass",
        "severity": "Critical",
        "type": "Security"
    },
    {
        "id": 2,
        "title": "ATM CRISIS",
        "app": "ATM Simulator",
        "story": "The ATM accepts a negative withdrawal amount.",
        "bug": "Negative withdrawal accepted",
        "severity": "High",
        "type": "Validation"
    },
    {
        "id": 3,
        "title": "CART CHAOS",
        "app": "E-Commerce",
        "story": "The shopping cart accepts an invalid quantity.",
        "bug": "Invalid quantity accepted",
        "severity": "High",
        "type": "Functional"
    },
    {
        "id": 4,
        "title": "PAYMENT LOOP",
        "app": "Payment Gateway",
        "story": "Clicking Pay twice creates two transactions.",
        "bug": "Duplicate payment",
        "severity": "Critical",
        "type": "Functional"
    },
    {
        "id": 5,
        "title": "REGISTRATION TRAP",
        "app": "Registration",
        "story": "The registration form accepts an invalid email.",
        "bug": "Invalid email accepted",
        "severity": "Medium",
        "type": "Validation"
    },
    {
        "id": 6,
        "title": "MARKS MYSTERY",
        "app": "Student Portal",
        "story": "Marks 80, 90 and 100 display an average of 100.",
        "bug": "Incorrect average calculation",
        "severity": "High",
        "type": "Functional"
    },
    {
        "id": 7,
        "title": "UI SHADOW",
        "app": "Employee Dashboard",
        "story": "Submit stays disabled after valid information is entered.",
        "bug": "Submit button state defect",
        "severity": "Medium",
        "type": "UI"
    },
    {
        "id": 8,
        "title": "FINAL BOSS",
        "app": "Banking Dashboard",
        "story": "A zero-value transaction is accepted successfully.",
        "bug": "Zero-value transaction accepted",
        "severity": "Critical",
        "type": "Security"
    }
]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/levels")
def get_levels():
    return jsonify(levels)


@app.route("/api/check", methods=["POST"])
def check_answer():

    data = request.json

    level_id = data["level_id"]
    bug = data["bug"]
    severity = data["severity"]
    bug_type = data["type"]

    level = next(
        (x for x in levels if x["id"] == level_id),
        None
    )

    if not level:
        return jsonify({"correct": False})

    if (
        bug == level["bug"]
        and severity == level["severity"]
        and bug_type == level["type"]
    ):
        points = 100

        if severity == "Critical":
            points = 150
        elif severity == "High":
            points = 120

        return jsonify({
            "correct": True,
            "points": points,
            "message": "BUG FOUND! Excellent QA analysis."
        })

    return jsonify({
        "correct": False,
        "points": 0,
        "message": "Incorrect bug classification."
    })


@app.route("/health")
def health():
    return "OK"


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
