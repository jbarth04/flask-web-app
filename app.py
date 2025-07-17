from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template(
        'index.html',
        name="Josie Barth",
        tagline="Positioning Consultant",
        about="I'm a passionate consultant who helps companies define their product positioning and build winning go-to-market strategies.",
        help_items=[
            "Defining their product positioning.",
            "Build the GTM narrative.",
            "Enable your sales team."
        ],
        email="your.email@example.com"
    )

if __name__ == "__main__":
    app.run(debug=True)
