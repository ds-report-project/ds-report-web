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

// 맨 왼쪽 3개 메뉴 클릭시 색상 변경 함수
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

// 맨 왼쪽 사이드바 클릭 시 각각 다른 html 불러오기
function changeSidebar() {
    var sidebar = document.getElementById("sidebar");
    var currentSidebar = sidebar.innerHTML;

    // Check the current sidebar and toggle to the other one
    if (currentSidebar.includes("This is Sidebar 1")) {
        sidebar.innerHTML = "{% include 'post/sidebar2_post.html' %}";
    } else {
        sidebar.innerHTML = "{% include 'post/sidebar_post.html' %}";
    }
}

// 게시물, 정보, 검색 선택에 따라 각각 다른 html 로드
document.addEventListener('DOMContentLoaded', function() {
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

    // Add click event listeners
    rectangle32.addEventListener('click', function() {
        toggleSidebarContent('post');
    });

    description.addEventListener('click', function() {
        toggleSidebarContent('post');
    });
    rectangle37.addEventListener('click', function() {
        toggleSidebarContent('info');
    });

    barChart.addEventListener('click', function() {
        toggleSidebarContent('info');
    });

    rectangle40.addEventListener('click', function() {
        toggleSidebarContent('search');
    });

    actionKey.addEventListener('click', function() {
        toggleSidebarContent('search');
    });

    sidebarPost.classList.add('active');

    function toggleSidebarContent(contentType) {

        // Reset all sidebar contents
        sidebarPost.classList.remove('active');
        sidebarInfo.classList.remove('active');
        sidebarSearch.classList.remove('active');

        // Toggle the clicked content
        if (contentType === 'post') {
            sidebarPost.classList.add('active');
        } else if (contentType === 'info') {
            sidebarInfo.classList.add('active');
        } else if (contentType === 'search') {
            sidebarSearch.classList.add('active');
        }

    }
});

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
