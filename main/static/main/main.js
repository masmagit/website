grecaptcha.ready(function() {
  const recaptcha_site_key = JSON.parse(document.getElementById('recaptcha_site_key').textContent);
  grecaptcha.execute(recaptcha_site_key, {action: "/contact/"})
    .then(function(token) {
      document.getElementById('grecaptcha-response').value = token;
    });
  });
