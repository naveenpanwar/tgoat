var login_functions = function() {
  var initialize = function ( navigator, user, token, urls ) {
    $("#id_login").on("click", function() {
      navigator.id.request();
    });
    
    navigator.id.watch({
      loggedInUser: user,
      onlogin: function ( assertion ) {
        $.post(
          urls.login,
          {assertion: assertion, csrfmiddlewaretoken: token }
        );
      }
    });
  };

  window.Superlists = {
    Accounts: {
      initialize: initialize,
    },
  };
};

$(document).ready( function() {
  login_functions();
});
