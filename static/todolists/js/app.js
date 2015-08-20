var todoApp = angular.module('todoApp', ['ngRoute', 'todoControllers']);
todoApp.config(['$routeProvider',
	function($routeProvider) {
		$routeProvider.
		when('/api/todolists/:todoId', {
			templateUrl: 'localhost:8000/static/todolists/js/partials/todolist.html',
			controller: 'todoController'
		});
		}
]);

// because django has csrf tokens
todoApp.config([
	'$httpProvider', function ($httpProvider){
		$httpProvider.defaults.xsrfCookieName = 'csrftoken';
		$httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
	}
])