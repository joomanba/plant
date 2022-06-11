'use strict';

// import PopUp from '/static/popup.js';

// const popup = new PopUp();

// Update the list with the given items
function loadContents(url) {
  const container = document.querySelector('.contents');

  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      container.innerHTML = this.responseText;
    }
  };
  xhttp.open('GET', url, true);
  xhttp.send();
}

function search() {
  const q = document.querySelector('.search_txt').value;
  // if (q != null && q.length < 2) {
  //   popup.showWithTextshowWithText('두 글자 이상의 검색어를 입력해 주세요^^');
  // }
  loadContents('/search?q=' + q);
}

// Handle button click
function onButtonClick(event) {
  const dataset = event.target.dataset;
  const url = dataset.value;

  if (url == null) {
    return;
  }

  loadContents(url);
}

function setEventListeners() {
  console.log('setEventListeners');
  const logo = document.querySelector('.logo');
  const buttons = document.querySelector('.buttons');
  logo.addEventListener('click', () => loadContents('/list'));
  buttons.addEventListener('click', (event) => onButtonClick(event));
}

loadContents('/list');
setEventListeners();
