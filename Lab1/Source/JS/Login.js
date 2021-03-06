/**
 * Created by BhavyaTeja on 2/7/2017.
 */
function check(form)/*function to check userid & password*/
    {
        /*the following code checkes whether the entered userid and password are matching*/
        if(form.userid.value == "vivek" && form.pswrd.value == "password")
        {
            window.open("Home.html")/*opens the target page while Id & password matches*/
        }
        else if (form.userid.value == "" || form.pswrd.value == "")
        {
            alert("Please enter Username & Password")/*displays error message*/
        }
        else
        {
            alert("Error Username or Password")
        }
    }

    // This is called with the results from from FB.getLoginStatus().
    function statusChangeCallback(response) {
        console.log(response);
        // The response object is returned with a status field that lets the
        // app know the current login status of the person.
        // Full docs on the response object can be found in the documentation
        // for FB.getLoginStatus().
        if (response.status === "connected") {
            // Logged into your app and Facebook.
            testAPI();
        } else if (response.status === "not_authorized") {
            // The person is logged into Facebook, but not your app.
            console.log("The person is logged into Facebook, but not your app.");
        }
    }
// This function is called when someone finishes with the Login
// Button.  See the onlogin handler attached to it in the sample
// code below.
function checkLoginState()
{
    FB.getLoginStatus(function(response) {
        statusChangeCallback(response);
    });
}
window.fbAsyncInit = function()
{
    FB.init({
        appId: "1947919255487599",
        cookie: true, // enable cookies to allow the server to access // the session
        xfbml: true, // parse social plugins on this page
        version: "v2.8" // use version 2.2
    });
    FB.Event.subscribe("auth.login", function () {
        window.location = "Home.html";
    });

    FB.getLoginStatus(function(response) {
        statusChangeCallback(response);
    });
};
// Load the SDK asynchronously
(function(d, s, id) {
    var js, fjs = d.getElementsByTagName(s)[0];
    if (d.getElementById(id)) return;
    js = d.createElement(s);
    js.id = id;
    js.src = "//connect.facebook.net/en_US/sdk.js";
    fjs.parentNode.insertBefore(js, fjs);
}(document, "script", "facebook-jssdk"));

// Here we run a very simple test of the Graph API after login is
// successful.  See statusChangeCallback() for when this call is made.
function testAPI()
{
    console.log("Welcome!  Fetching your information.... ");
    FB.api("/me", function(response) {
        console.log("Fb response");
        console.log(response);
        console.log("Successful login for: " + response.name);
        document.getElementById("status").innerHTML ="Thanks for logging in, " + response.name + "!";
    });
    window.location = "Home.html"
}
