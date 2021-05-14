// Google recaptcha call 
grecaptcha.ready(function() {
  const recaptcha_site_key = JSON.parse(document.getElementById('recaptcha_site_key').textContent);
  grecaptcha.execute(recaptcha_site_key, {action: "/contact/"})
    .then(function(token) {
      document.getElementById('grecaptcha-response').value = token;
    });
  });

document.addEventListener('DOMContentLoaded', function() {
  
  // form_contact: remove "is-invalid" class once value is changed in an input field
  var form_contact_inputs = document.forms.namedItem("form_contact").getElementsByTagName("input")
  Array.prototype.forEach.call(form_contact_inputs, function(element) {
    element.onkeydown = function() { 
      if (element.classList.contains("is-invalid")) {
        element.classList.remove("is-invalid");
      }
    }
  });

});
