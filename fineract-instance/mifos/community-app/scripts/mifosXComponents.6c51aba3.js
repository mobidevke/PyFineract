define(['Q', 'underscore', 'mifosX'], function (Q) {
    var components = {
        models: [
            'models.e41d3544'
        ],
        services: [
            'ResourceFactoryProvider',
            'HttpServiceProvider',
            'AuthenticationService',
            'SessionManager',
            'Paginator',
            'UIConfigService',
            'NotificationResponseHeaderProvider'
        ],
        controllers: [
            'controllers.7147f182'
        ],
        filters: [
            'filters.9206d4d0'
        ],
        directives: [
            'directives.0716fd7c'
        ]
    };

    return function() {
        var defer = Q.defer();
        require(_.reduce(_.keys(components), function (list, group) {
            return list.concat(_.map(components[group], function (name) {
                return group + "/" + name;
            }));
        }, [
            'routes-initialTasks-webstorage-configuration.bbf48eff'
        ]), function(){
            defer.resolve();
        });
        return defer.promise;
    }
});
