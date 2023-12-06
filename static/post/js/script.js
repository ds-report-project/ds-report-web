// url에 따라 스타일 변경
document.addEventListener('DOMContentLoaded', function () {
    // 현재 URL 경로 가져오기
    var currentPath = window.location.href;
    var currentPathPost = window.location.pathname;
    console.log(localStorage.getItem('is_clicked'));
    console.log(currentPath);
    document.getElementById('rectangle40').addEventListener('click', function() {
        localStorage.setItem('is_clicked', 'true');
    });
    document.getElementById('action_key').addEventListener('click', function() {
        localStorage.setItem('is_clicked', 'true');
    });
    document.getElementById('rule_btn').addEventListener('click', function() {
        localStorage.setItem('is_clicked', 'true');
    });

    // 규정 검색 페이지
    if (currentPath.includes('/post/?search=')) {
        document.getElementById('rectangle40').style.backgroundColor = '#EDEDED';
        document.getElementById('rectangle37').style.backgroundColor = '#FFFFFF';
        document.getElementById('rectangle32').style.backgroundColor = '#FFFFFF';
        document.getElementById('sidebar-info').classList.remove('active');
        document.getElementById('sidebar-post').classList.remove('active');
        document.getElementById('sidebar-search').classList.add('active');
        localStorage.setItem('is_clicked', 'false');
    }
    //Contact 페이지
    else if (currentPath.includes('/contact/')) {
        document.getElementById('rectangle37').style.backgroundColor = '#EDEDED';
        document.getElementById('rectangle32').style.backgroundColor = '#FFFFFF';
        document.getElementById('sidebar-info').classList.add('active');
        document.getElementById('sidebar-post').classList.remove('active');
        document.getElementById('sidebar-search').classList.remove('active');
        localStorage.setItem('is_clicked', 'false');
    }
    else if (currentPathPost ==='/post/') {
        document.getElementById('rectangle32').style.backgroundColor = '#EDEDED';
        document.getElementById('rectangle37').style.backgroundColor = '#FFFFFF';
        document.getElementById('sidebar-post').classList.add('active');
        document.getElementById('sidebar-info').classList.remove('active');
        document.getElementById('sidebar-search').classList.remove('active');
        localStorage.setItem('is_clicked', 'false');

    }
    // 게시물 페이지
    else if (currentPath.includes('/post/')) {
        document.getElementById('rectangle32').style.backgroundColor = '#EDEDED';
        document.getElementById('rectangle37').style.backgroundColor = '#FFFFFF';
        document.getElementById('sidebar-post').classList.add('active');
        document.getElementById('sidebar-info').classList.remove('active');
        document.getElementById('sidebar-search').classList.remove('active');
        localStorage.setItem('is_clicked', 'false');

    }
    // 규정 검색 페이지
    else if (localStorage.getItem('is_clicked')) {
        document.getElementById('rectangle40').style.backgroundColor = '#EDEDED';
        document.getElementById('rectangle37').style.backgroundColor = '#FFFFFF';
        document.getElementById('rectangle32').style.backgroundColor = '#FFFFFF';
        document.getElementById('sidebar-info').classList.remove('active');
        document.getElementById('sidebar-post').classList.remove('active');
        document.getElementById('sidebar-search').classList.add('active');
        localStorage.setItem('is_clicked', 'false');
    }
    else {
        // 검색창 비활성화
        document.getElementById('post-search').classList.remove('active');
    }
});


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



function sideClickEvent(boxId, icon) {
    var box = document.getElementById(boxId);
    var icon = document.getElementById(icon);

    box.addEventListener('click', function() {
        box.style.backgroundColor = '#EDEDED';
        document.getElementById('rectangle37').style.backgroundColor = '#FFFFFF';
        document.getElementById('rectangle32').style.backgroundColor = '#FFFFFF';
    });
    icon.addEventListener('click', function() {
        box.style.backgroundColor = '#EDEDED';
        document.getElementById('rectangle37').style.backgroundColor = '#FFFFFF';
        document.getElementById('rectangle32').style.backgroundColor = '#FFFFFF';
    });
}

// 토글 초기값 지정
document.addEventListener('DOMContentLoaded', function() {
    // 여기서 초기값을 지정할 요소의 ID를 사용하여 bgColor 함수 호출
    bgColor('rectangle19');
    // 초기값으로 설정한 rectangle19에 대해 클릭 이벤트 핸들러 등록
    addClickEvent('rectangle19', 'facility');

});

// 게시물, 정보, 검색 선택에 따라 각각 다른 html 로드
document.addEventListener('DOMContentLoaded', function() {
    // 배경색 초기값 지정
    // 여기서 초기값을 지정할 요소의 ID를 사용하여 bgColor 함수 호출
    bgColor('rectangle19');
    // 초기값으로 설정한 rectangle19에 대해 클릭 이벤트 핸들러 등록
    addClickEvent('rectangle19', 'facility');

    // Get sidebar elements
    var sidebarPost = document.getElementById('sidebar-post');
    var sidebarInfo = document.getElementById('sidebar-info');
    var sidebarSearch = document.getElementById('sidebar-search');

    // Get clickable elements
    var rectangle32 = document.getElementById('rectangle32');
    var description = document.getElementById('description');
    var rectangle37 = document.getElementById('rectangle37');
    var barChart = document.getElementById('bar_chart');
    var rectangle40 = document.getElementById('rectangle40');
    var actionKey = document.getElementById('action_key');


    rectangle40.addEventListener('click', function() {
        toggleSidebarContent('search');
    });

    actionKey.addEventListener('click', function() {
        toggleSidebarContent('search');
    });

        function toggleSidebarContent(contentType) {

        // Reset all sidebar contents
        sidebarPost.classList.remove('active');
        sidebarInfo.classList.remove('active');
        sidebarSearch.classList.add('active');

        if (contentType === 'post') {
            sidebarPost.classList.add('active');
        } else if (contentType === 'info') {
            sidebarInfo.classList.add('active');
        } else if (contentType === 'search') {
            sidebarSearch.classList.add('active');
        }

    }
});


// 클릭 시 배경색 변경
addClickEvent('rectangle19', 'facility');
addClickEvent('rectangle20', 'administration');
addClickEvent('rectangle21', 'welfare');
addClickEvent('rectangle45', 'education');
addClickEvent('rectangle46', 'other');

sideClickEvent('rectangle40', 'action_key');


// hover 시 border
addHoverEffect('facility','rectangle19');
addHoverEffect('administration','rectangle20');
addHoverEffect('welfare','rectangle21');
addHoverEffect('education','rectangle45');
addHoverEffect('other','rectangle46');
addHoverEffect('description','rectangle32');
addHoverEffect('bar_chart','rectangle37');
addHoverEffect('action_key','rectangle40');

