var todoControllers = angular.module('todoControllers', []);

todoControllers.controller('TodoDetailController', ['$scope', '$routeParams', '$http',
	function($scope, $routeParams, $http) {
		console.log($routeParams);
		console.log('hi');
		$http.get('/api/todo/' + $routeParams.todoId + '/?format=json').success(function(data) {
			$scope.todo = data;
		});
	}
])