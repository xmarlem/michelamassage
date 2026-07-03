var QR_IT = "mailto:manzo.michela@gmail.com?subject=Prenotazione%20Michela%20Massage&body=Salve%20Michela%2C%0A%0AVorrei%20prenotare%20un%20appuntamento.%0A%0ANome%3A%20%0ATrattamento%3A%20%0AData%20preferita%3A%20%0A%0AGrazie!";
var QR_DE = "mailto:manzo.michela@gmail.com?subject=Terminanfrage%20Michela%20Massage&body=Guten%20Tag%20Michela%2C%0A%0Aich%20m%C3%B6chte%20einen%20Termin%20vereinbaren.%0A%0AName%3A%20%0ABehandlung%3A%20%0ADatum%2FUhrzeit%3A%20%0A%0AVielen%20Dank!";
var QR_EN = "mailto:manzo.michela@gmail.com?subject=Appointment%20request%20Michela%20Massage&body=Hello%20Michela%2C%0A%0AI%20would%20like%20to%20book%20an%20appointment.%0A%0AName%3A%20%0ATreatment%3A%20%0APreferred%20date%2Ftime%3A%20%0A%0AThank%20you!";
var lang = 'de';

function attrForLang(l, prefix) {
  if (l === 'it') return prefix + '-i';
  if (l === 'en') return prefix + '-e';
  return prefix + '-d';
}

function qrForLang(l) {
  if (l === 'it') return QR_IT;
  if (l === 'en') return QR_EN;
  return QR_DE;
}

function buildQR(l) {
  var el = document.getElementById('qrcode');
  if (!el) return;
  el.innerHTML = '';

  if (typeof QRCode === 'undefined') {
    var link = document.createElement('a');
    link.href = qrForLang(l);
    link.textContent = l === 'de' ? 'E-Mail öffnen' : (l === 'it' ? 'Apri email' : 'Open email');
    link.className = 'qr-fallback';
    el.appendChild(link);
    return;
  }

  new QRCode(el, {
    text: qrForLang(l),
    width: 130,
    height: 130,
    colorDark: '#0d1b2a',
    colorLight: '#ffffff',
    correctLevel: QRCode.CorrectLevel.M
  });
}

function setLang(l) {
  lang = l;
  document.documentElement.lang = l;
  var a = attrForLang(l, 'data');

  document.querySelectorAll('[data-i]').forEach(function(el) {
    var v = el.getAttribute(a);
    if (v !== null) el.innerHTML = v;
  });

  document.querySelectorAll('[data-ph-i]').forEach(function(el) {
    var v = el.getAttribute(attrForLang(l, 'data-ph'));
    if (v !== null) el.placeholder = v;
  });

  document.querySelectorAll('select option[data-i]').forEach(function(o) {
    var v = o.getAttribute(a);
    if (v) o.textContent = v;
  });

  buildQR(l);

  document.querySelectorAll('.lang-btn').forEach(function(b) {
    var active = b.textContent.trim().toLowerCase() === l;
    b.classList.toggle('active', active);
    b.setAttribute('aria-pressed', active ? 'true' : 'false');
  });
}

window.addEventListener('scroll', function() {
  var nav = document.getElementById('nav');
  if (nav) nav.classList.toggle('scrolled', window.scrollY > 60);
});

if ('IntersectionObserver' in window) {
  document.querySelectorAll('.reveal').forEach(function(el) {
    new IntersectionObserver(function(entries) {
      if (entries[0].isIntersecting) {
        entries[0].target.classList.add('visible');
        this.disconnect();
      }
    }.bind(this), { threshold: 0.1 }).observe(el);
  });
} else {
  document.querySelectorAll('.reveal').forEach(function(el) {
    el.classList.add('visible');
  });
}

function handleSubmit(e) {
  e.preventDefault();
  var n = document.getElementById('inp-nome').value;
  var m = document.getElementById('inp-mail').value;
  var s = document.getElementById('inp-svc').value;
  var t = document.getElementById('inp-msg').value;
  var phoneEl = document.getElementById('inp-phone');
  var phone = phoneEl ? phoneEl.value : '';
  var subj, body;

  if (lang === 'de') {
    subj = encodeURIComponent('Terminanfrage Michela Massage');
    body = encodeURIComponent('Guten Tag Michela,\n\nich möchte einen Termin vereinbaren.\n\nName: ' + n + '\nEmail: ' + m + '\nTelefon: ' + phone + '\nBehandlung: ' + s + '\n\nNachricht: ' + t + '\n\nVielen Dank!');
  } else if (lang === 'en') {
    subj = encodeURIComponent('Appointment request Michela Massage');
    body = encodeURIComponent('Hello Michela,\n\nI would like to book an appointment.\n\nName: ' + n + '\nEmail: ' + m + '\nPhone: ' + phone + '\nTreatment: ' + s + '\n\nMessage: ' + t + '\n\nThank you!');
  } else {
    subj = encodeURIComponent('Prenotazione Michela Massage');
    body = encodeURIComponent('Salve Michela,\n\nVorrei prenotare un appuntamento.\n\nNome: ' + n + '\nEmail: ' + m + '\nTelefono: ' + phone + '\nTrattamento: ' + s + '\n\nMessaggio: ' + t + '\n\nGrazie!');
  }

  window.location.href = 'mailto:manzo.michela@gmail.com?subject=' + subj + '&body=' + body;
  document.getElementById('form-ok').style.display = 'block';
}

window.addEventListener('load', function() { setLang('de'); });
