var helloApp = angular.module('helloApp', []);

helloApp.controller('resultListCtrl', ['$scope', '$http',
  function ($scope) {
      $http.get('phones/' + $routeParams.phoneId + '.json').success(function(data) {
          $scope.restaurants = [
            {'name': 'Round Table'},
              {'name': 'McDonalds'},
              {'name': 'Burger King'},
              {'name': 'Carls Jr'}
          ];
    });
}]);

