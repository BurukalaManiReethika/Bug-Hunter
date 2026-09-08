let levels = [];

let currentLevel = 0;

let score = 0;

let time = 60;

let timer;


async function startGame() {

    const response =
        await fetch("/api/levels");

    levels = await response.json();

    document
        .getElementById("startScreen")
        .classList.add("hidden");

    document
        .getElementById("gameScreen")
        .classList.remove("hidden");

    loadLevel();
}


function loadLevel() {

    clearInterval(timer);

    time = 60;

    document
        .getElementById("time")
        .textContent = time;

    const level =
        levels[currentLevel];

    document
        .getElementById("level")
        .textContent =
        currentLevel + 1;

    document
        .getElementById("score")
        .textContent = score;

    document
        .getElementById("title")
        .textContent =
        level.title;

    document
        .getElementById("application")
        .textContent =
        level.app;

    document
        .getElementById("story")
        .textContent =
        level.story;

    document
        .getElementById("bug")
        .value = "";

    document
        .getElementById("severity")
        .value = "";

    document
        .getElementById("type")
        .value = "";

    document
        .getElementById("result")
        .textContent = "";

    document
        .getElementById("result")
        .className = "";

    timer = setInterval(() => {

        time--;

        document
            .getElementById("time")
            .textContent = time;

        if (time <= 0) {

            clearInterval(timer);

            showResult(
                "⏰ TIME OUT!",
                false
            );
        }

    }, 1000);
}


async function submitBug() {

    if (time <= 0) {
        return;
    }

    const data = {

        level_id:
            levels[currentLevel].id,

        bug:
            document.getElementById("bug").value,

        severity:
            document.getElementById("severity").value,

        type:
            document.getElementById("type").value
    };


    const response =
        await fetch("/api/check", {

            method: "POST",

            headers: {
                "Content-Type":
                    "application/json"
            },

            body:
                JSON.stringify(data)
        });


    const result =
        await response.json();


    if (result.correct) {

        score += result.points;

        document
            .getElementById("score")
            .textContent = score;

        showResult(
            "🐛 BUG FOUND! +" +
            result.points +
            " XP",
            true
        );

        clearInterval(timer);

        setTimeout(() => {

            currentLevel++;

            if (
                currentLevel >=
                levels.length
            ) {

                finishGame();

            } else {

                loadLevel();
            }

        }, 1500);

    } else {

        showResult(
            "❌ " + result.message,
            false
        );
    }
}


function showResult(message, correct) {

    const box =
        document.getElementById("result");

    box.textContent = message;

    box.className =
        correct ? "correct" : "wrong";
}


function finishGame() {

    document
        .getElementById("gameScreen")
        .classList.add("hidden");

    document
        .getElementById("finishScreen")
        .classList.remove("hidden");

    document
        .getElementById("finalScore")
        .textContent =
        score + " XP";
}
