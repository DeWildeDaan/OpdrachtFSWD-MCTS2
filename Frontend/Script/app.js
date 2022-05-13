'use strict';
const lanIP = `${window.location.hostname}:5000`;
const backend = backend_IP + '/api/v1';
const socketio = io(lanIP);

//#region ***  DOM references                           ***********
//#endregion

//#region ***  Callback-Visualisation - show___         ***********
//#endregion

//#region ***  Callback-No Visualisation - callback___  ***********
//#endregion

//#region ***  Data Access - get___                     ***********

// const get__ = function () {
// 	let url = `${backend}'/...'`;
// 	handleData(url, ..., null, 'GET');
// };

//#endregion

//#region ***  Event Listeners - listenTo___            ***********

// Event listeners: click, mouseover, mouseout
// const listenTo__ = function () {
// 	for (let btn of document.querySelectorAll('.js-...')) {
// 		btn.addEventListener('...', function () {
// 		});
// 	}
// };

// Socketio listener
// const listenToSocket = function () {
// 	socketio.on('B2F_welcome', function (msg) {
// 		console.log(msg);
// 	});
// };

//#endregion

//#region ***  Init / DOMContentLoaded                  ***********
const init = function () {
	console.log('DOM Content Loaded.');
};

document.addEventListener('DOMContentLoaded', init);
//#endregion
