let attempts = 9; //시도 횟수

function createRandomNumbers() {
    const randomNumbers = [];
    while (randomNumbers.length < 3) {
        const num = Math.floor(Math.random() * 10);
        if (!randomNumbers.includes(num)) {
            randomNumbers.push(num);
        }
    }
    return randomNumbers;
}

let solution = createRandomNumbers(); //난수 생성
let gameEnded = false; 

function resetInputFields() { 
    for (let i = 1; i <= 3; i++) {
        document.getElementById(`number${i}`).value = '';
    }
    document.getElementById('number1').focus();
}

function updateAttempts() { //시도 횟수 업데이트
    document.getElementById('attempts').textContent = attempts;
}

function generateResultDisplay(guess, strikes, balls) {
    const resultContainer = document.createElement('div');
    resultContainer.className = 'check-result';

    const guessDisplay = document.createElement('div'); // Display guessed numbers
    guessDisplay.className = 'left';
    guessDisplay.textContent = guess.join(' ') + '    :    ';

    const feedbackDisplay = document.createElement('div'); // Display result feedback
    feedbackDisplay.className = 'right';

    if (strikes === 0 && balls === 0) { //아웃
        const outIndicator = document.createElement('span');
        outIndicator.className = 'num-result out';
        outIndicator.textContent = 'O';
        feedbackDisplay.appendChild(outIndicator);
    } else {
        if (strikes > 0) { //스트라이크
            const strikeIndicator = document.createElement('span');
            strikeIndicator.className = 'num-result strike';
            strikeIndicator.textContent = 'S';
            feedbackDisplay.appendChild(document.createTextNode(strikes));
            feedbackDisplay.appendChild(strikeIndicator);
        }
        if (balls > 0) { //볼
            const ballIndicator = document.createElement('span');
            ballIndicator.className = 'num-result ball';
            ballIndicator.textContent = 'B';
            feedbackDisplay.appendChild(document.createTextNode(balls));
            feedbackDisplay.appendChild(ballIndicator);
        }
    }

    resultContainer.appendChild(guessDisplay);
    resultContainer.appendChild(feedbackDisplay);

    return resultContainer;
}

function check_numbers() {
    const inputs = [
        document.getElementById('number1').value,
        document.getElementById('number2').value,
        document.getElementById('number3').value
    ];
    console.log(inputs);
    const guess = inputs.map(Number);
    attempts--;

    updateAttempts();

    let strikes = 0;
    let balls = 0;

    for (let i = 0; i < 3; i++) {
        if (guess[i] === solution[i]) {
            strikes++;
        } else if (solution.includes(guess[i])) {
            balls++;
        }
    }

    const resultsSection = document.getElementById('results'); 
    resultsSection.appendChild(generateResultDisplay(guess, strikes, balls));

    if (strikes === 3 || attempts === 0) {
        gameEnded = true;
        const resultImage = document.getElementById('game-result-img');
        resultImage.src = strikes === 3 ? 'success.png' : 'fail.png';
        document.querySelector('.submit-button').disabled = true;
    }

    resetInputFields();
}

for (let i = 1; i <= 2; i++) { 
    document.getElementById(`number${i}`).addEventListener('input', function() {
        if (this.value) {
            document.getElementById(`number${i + 1}`).focus();
        }
    });
}

updateAttempts();
document.getElementById('game-result-img').src = '';
document.getElementById('results').innerHTML = '';