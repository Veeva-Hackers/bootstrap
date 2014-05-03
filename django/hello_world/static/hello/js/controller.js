var helloApp = angular.module('helloApp', []);

helloApp.controller('resultListCtrl', ['$scope', '$http',
  function ($scope, $http) {
      $http.get('/searchrestaurant').success(function(data) {
          $scope.restaurants = data;
    });
}]);

