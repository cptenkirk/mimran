const canvas = document.getElementById("gameCanvas");
const ctx = canvas.getContext("2d");

const box = 20;
let snake = [];
snake[0] = { x: 9 * box, y: 10 * box };

let food = {
    x: Math.floor(Math.random() * 19 + 1) * box,
    y: Math.floor(Math.random() * 19 + 1) * box
};

let score = 0;
let d;

document.addEventListener("keydown", direction);

function direction(event) {
    const key = event.key;
    console.log("Drawing frame"); // Debug-Ausgabe
    console.log("Snake position: ", snake[0]); // Debug-Ausgabe
    console.log("Key pressed: ", key); // Debug-Ausgabe
    if (["ArrowLeft", "ArrowUp", "ArrowRight", "ArrowDown"].includes(key)) {
        event.preventDefault();  // Verhindert das Scrollen
    }
    if (key === "ArrowLeft" && d !== "RIGHT") {
        d = "LEFT";
    } else if (key === "ArrowUp" && d !== "DOWN") {
        d = "UP";
    } else if (key === "ArrowRight" && d !== "LEFT") {
        d = "RIGHT";
    } else if (key === "ArrowDown" && d !== "UP") {
        d = "DOWN";
    }
    console.log("Direction: ", d); // Debug-Ausgabe
}

function collision(head, array) {
    for (let i = 0; i < array.length; i++) {
        if (head.x == array[i].x && head.y == array[i].y) {
            return true;
        }
    }


    

    return false;

    
}

function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    for (let i = 0; i < snake.length; i++) {
        ctx.fillStyle = (i == 0) ? "green" : "white";
        ctx.fillRect(snake[i].x, snake[i].y, box, box);

        ctx.strokeStyle = "red";
        ctx.strokeRect(snake[i].x, snake[i].y, box, box);
    }

    ctx.fillStyle = "red";
    ctx.fillRect(food.x, food.y, box, box);

    let snakeX = snake[0].x;
    let snakeY = snake[0].y;

    if (d == "LEFT") snakeX -= box;
    if (d == "UP") snakeY -= box;
    if (d == "RIGHT") snakeX += box;
    if (d == "DOWN") snakeY += box;

    if (snakeX == food.x && snakeY == food.y) {
        score++;
        food = {
            x: Math.floor(Math.random() * 19 + 1) * box,
            y: Math.floor(Math.random() * 19 + 1) * box
        };
    } else {
        snake.pop();
    }

    let newHead = {
        x: snakeX,
        y: snakeY
    };

    if (snakeX < 0 || snakeY < 0 || snakeX >= canvas.width || snakeY >= canvas.height || collision(newHead, snake)) {
        clearInterval(game);
        document.getElementById("restart").style.display = "block"; // Zeige Neustart-Button
        return;
    }

    snake.unshift(newHead);

    ctx.fillStyle = "white";
    ctx.font = "45px Changa one";
    ctx.fillText(score, 2 * box, 1.6 * box);
}

function resetGame() {
    snake = [];
    snake[0] = { x: 9 * box, y: 10 * box };
    score = 0;
    d = "RIGHT";
    food = {
        x: Math.floor(Math.random() * 19 + 1) * box,
        y: Math.floor(Math.random() * 19 + 1) * box
    };
    document.getElementById("restart").style.display = "none"; // Verstecke Neustart-Button
    game = setInterval(draw, 100);
}

let game = setInterval(draw, 100);

document.getElementById("restart").addEventListener("click", resetGame);