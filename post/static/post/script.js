// hover 시 border 생기게
function addHoverEffect(iconId, boxId) {
    const icon = document.getElementById(iconId);
    const box = document.getElementById(boxId);

    // icon에 호버 시 rectangle 스타일 변경
    icon.addEventListener('mouseover', function () {
        box.style.border = '1px solid #CCCCCC';
    });

    // box에 hover한 경우 border 설정, 아닌 경우 none으로 변경
    box.addEventListener('mouseover', function () {
        box.style.border = '1px solid #CCCCCC';
    });

    box.addEventListener('mouseout', function () {
        if (!icon.matches(':hover')) {
            box.style.border = 'none';
        }
    });

    // 호버가 해제될 때 스타일 원래대로
    icon.addEventListener('mouseout', function () {
        box.style.border = 'none';
    });
}

//box color
// 사이드바 클릭시 배경색 변경
let prevClicked = null;

function bgColor(boxId) {
    var box = document.getElementById(boxId);
    if (prevClicked) {
        // 이전에 클릭된 요소의 배경색을 초기 상태로 복원
        prevClicked.style.backgroundColor = '#FFFFFF';
    }

    // 클릭된 요소의 배경색을 변경
    box.style.backgroundColor = '#EDEDED';

    // 이전에 클릭된 요소 저장
    prevClicked = box;
}


// 클릭 이벤트 핸들러를 등록하는 함수
function addClickEvent(boxId, icon) {
    var box = document.getElementById(boxId);
    var icon = document.getElementById(icon);

    box.addEventListener('click', function() {
        bgColor(boxId);
    });

    icon.addEventListener('click', function() {
        bgColor(boxId);
    });
}

// 맨 왼쪽 3개 메뉴 클릭 이벤트 핸들러 함수
let sidePrev = null;
function sideColor(boxId) {
    var box = document.getElementById(boxId);
    if (sidePrev) {
        // 이전에 클릭된 요소의 배경색을 초기 상태로 복원
        sidePrev.style.backgroundColor = '#FFFFFF';
    }

    // 클릭된 요소의 배경색을 변경
    box.style.backgroundColor = '#EDEDED';

    // 이전에 클릭된 요소 저장
    sidePrev = box;
}

function sideClickEvent(boxId, icon) {
    var box = document.getElementById(boxId);
    var icon = document.getElementById(icon);

    box.addEventListener('click', function() {
        sideColor(boxId);
    });

    icon.addEventListener('click', function() {
        sideColor(boxId);
    });
}

// 각 요소에 클릭 이벤트 핸들러 등록
addClickEvent('rectangle19', 'facility');
addClickEvent('rectangle20', 'administration');
addClickEvent('rectangle21', 'welfare');
addClickEvent('rectangle45', 'education');
addClickEvent('rectangle46', 'other');
sideClickEvent('rectangle32', 'description');
sideClickEvent('rectangle37', 'bar_chart');
sideClickEvent('rectangle40', 'action_key');


// hover
addHoverEffect('facility','rectangle19');
addHoverEffect('administration','rectangle20');
addHoverEffect('welfare','rectangle21');
addHoverEffect('education','rectangle45');
addHoverEffect('other','rectangle46');
addHoverEffect('description','rectangle32');
addHoverEffect('bar_chart','rectangle37');
addHoverEffect('action_key','rectangle40');
