const timeDisplay = document.querySelector('.time');
const startBtn = document.querySelector('.start_btn');
const stopBtn = document.querySelector('.stop_btn');
const resetBtn = document.querySelector('.reset_btn');
const trashcan = document.querySelector('.trashcan');
const checkBox = document.querySelector('.check_box');
const selectAllCheckbox = document.querySelector('.select_all');
const sortBtn = document.querySelector('.sort_btn');

// 스톱워치 상태 변수
let timerInterval = null;
let timePassed = 0; 

// 시간 리셋셋
function formatTime(milliseconds) {
    const totalSeconds = Math.floor(milliseconds / 1000);
    const minutes = Math.floor(totalSeconds / 60);
    const seconds = totalSeconds % 60;
    const centiseconds = Math.floor((milliseconds % 1000) / 10);

    return String(minutes).padStart(2, '0') + ':' +
           String(seconds).padStart(2, '0') + ':' +
           String(centiseconds).padStart(2, '0');
}

// 스톱워치 시작 
function startStopwatch() {
    if (!timerInterval) {
        const startTime = Date.now() - timePassed; 
        timerInterval = setInterval(() => {
            timePassed = Date.now() - startTime;
            timeDisplay.textContent = formatTime(timePassed);
        }, 10);
    }
}

// 스톱워치 정지
function stopStopwatch() {
    clearInterval(timerInterval);
    timerInterval = null; 

    if (timePassed > 0) {
        const recordItem = document.createElement('div');
        recordItem.classList.add('record_item');

        const checkbox = document.createElement('input');
        checkbox.type = 'checkbox';
        checkbox.classList.add('record_checkbox');

        const recordText = document.createElement('span');
        recordText.textContent = formatTime(timePassed);

        recordItem.appendChild(checkbox);
        recordItem.appendChild(recordText);
        checkBox.appendChild(recordItem);
        
        //추가기능 2 체크박스 이벤트리스너너
        checkbox.addEventListener('change', updateSelectAllCheckbox);
    }
}

// 스톱워치 리셋
function resetStopwatch() {
    clearInterval(timerInterval);
    timerInterval = null; 
    timePassed = 0;
    timeDisplay.textContent = '00:00:00'; 
    selectAllCheckbox.checked = false;
}

// 선택 기록 삭제
function clearSelectedRecords() {
    const selectedRecords = document.querySelectorAll('.record_item .record_checkbox:checked');
    selectedRecords.forEach((checkbox) => {
        const recordItem = checkbox.parentElement;
        recordItem.remove();
    });
    updateSelectAllCheckbox();
}

function toggleSelectAll() {
    const allCheckboxes = document.querySelectorAll('.record_checkbox:not(.select_all)');
    const isChecked = selectAllCheckbox.checked;

    allCheckboxes.forEach((checkbox) => {
        checkbox.checked = isChecked;
    });
    updateSelectAllCheckbox();
}
function updateSelectAllCheckbox() {
    const allCheckboxes = document.querySelectorAll('.record_checkbox:not(.select_all)');
    const checkedCheckboxes = document.querySelectorAll('.record_checkbox:checked:not(.select_all)');

    selectAllCheckbox.checked = allCheckboxes.length > 0 && allCheckboxes.length === checkedCheckboxes.length;
}

//추가 기능1 오름차순으로 배열
function sortRecords() {
    const records = Array.from(document.querySelectorAll('.record_item'));
    const sortedRecords = records.sort((a, b) => {
        const timeA = parseTime(a.querySelector('span').textContent);
        const timeB = parseTime(b.querySelector('span').textContent);
        return timeA - timeB;
    });
    checkBox.innerHTML = '';
    sortedRecords.forEach((record) => checkBox.appendChild(record));
}
function parseTime(timeString) {
    const [minutes, seconds, centiseconds] = timeString.split(':').map(Number);
    return minutes * 60000 + seconds * 1000 + centiseconds * 10;
}

//추가기능2 
function addCheckboxListeners() {
    const allCheckboxes = document.querySelectorAll('.record_checkbox:not(.select_all)');
    allCheckboxes.forEach((checkbox) => {
        checkbox.addEventListener('change', updateSelectAllCheckbox);
    });
}

startBtn.addEventListener('click', startStopwatch);
stopBtn.addEventListener('click', stopStopwatch);
resetBtn.addEventListener('click', resetStopwatch);
trashcan.addEventListener('click', clearSelectedRecords);
selectAllCheckbox.addEventListener('change', toggleSelectAll);
sortBtn.addEventListener('click', sortRecords);