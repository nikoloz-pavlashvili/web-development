const playerMoveDiv = document.getElementById("playerMove");
const options = ["Rock", "Paper", "Scissors"];

const playerScoreDisplay = document.getElementById("playerScore");
const computerScoreDisplay = document.getElementById("computerScore");
const winnerDisplay = document.getElementById("winner");
const compMove = document.getElementById("compMove");

let playerScore = 0;
let computerScore = 0;

playerMoveDiv.onclick = function(eventObject) {
    let playerChoice = eventObject.target.textContent;
    let randomIndex = Math.floor(Math.random() * 3); 
    let computerChoice = options[randomIndex];

    if ((playerChoice === "Rock" && computerChoice === "Scissors") ||
        (playerChoice === "Paper" && computerChoice === "Rock") ||
        (playerChoice === "Scissors" && computerChoice === "Paper")) { 
        playerScore++;
        playerScoreDisplay.textContent = "Player Score: " + String(playerScore);
        winnerDisplay.textContent = "You won!";
    } else if (playerChoice === computerChoice) {
        winnerDisplay.textContent = "Draw!";
    } else {
        computerScore++;
        computerScoreDisplay.textContent = "Computer Score: " + String(computerScore);
        winnerDisplay.textContent = "Computer won!";
    }

    compMove.textContent = "Computer choice: " + computerChoice;
}