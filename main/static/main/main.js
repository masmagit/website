// Google recaptcha call 
grecaptcha.ready(function() {
  const recaptcha_site_key = JSON.parse(document.getElementById('recaptcha_site_key').textContent);
  grecaptcha.execute(recaptcha_site_key, {action: "/contact/"})
    .then(function(token) {
      document.getElementById('grecaptcha-response').value = token;
    });
  });

document.addEventListener('DOMContentLoaded', function() {
  const cform = document.forms.namedItem("form_contact")
  const form_contact_inputs = cform.getElementsByTagName("input")
  const spinner = document.getElementById("spinner");

  // form_contact: remove "is-invalid" class once value is changed in an input field
  Array.prototype.forEach.call(form_contact_inputs, function(element) {
    element.onkeydown = function() { 
      if (element.classList.contains("is-invalid")) {
        element.classList.remove("is-invalid");
      }
    }
  });

  cform.addEventListener('submit', function() {
    cform.classList.toggle('fade-out');
    spinner.classList.replace('hide', 'show');
  });
});
