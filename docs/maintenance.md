# Guida manutenzione

## Regola generale

Il sito è tutto in `index.html`. Per modifiche piccole conviene editare direttamente il file, ma bisogna mantenere sincronizzate tre aree:

1. testi visibili negli elementi HTML;
2. attributi `data-i`, `data-d` e `data-e` per il cambio lingua;
3. eventuali valori duplicati in card servizi, tabella prezzi, form e QR/mailto.

## Modificare testi multilingue

Ogni testo traducibile segue questo schema:

```html
<p data-i="Testo italiano" data-d="Testo tedesco" data-e="English text">Testo tedesco</p>
```

Per modificare un testo:

1. aggiornare `data-i`;
2. aggiornare `data-d`;
3. aggiornare `data-e`;
4. aggiornare anche il contenuto interno dell'elemento con il testo tedesco, perché la lingua iniziale è DE.

Se il contenuto contiene HTML, come `<em>` o `<strong>`, va incluso anche dentro gli attributi `data-i`, `data-d` e `data-e`.

## Modificare i prezzi

Controllare e allineare sempre:

- card servizio in `#servizi`;
- tabella principale in `#prezzi`;
- option del select nel form contatto;
- testo della mail se il trattamento o la durata cambia.

I prezzi sono duplicati in card, tabella prezzi e option del form. Quando cambia un prezzo, aggiornare sempre tutte le occorrenze e verificare anche i pacchetti gravidanza nella nota prezzi.

## Aggiungere un servizio

Passi consigliati:

1. duplicare una `.service-card` dentro `.services-grid`;
2. aggiornare `.svc-num`;
3. aggiornare `.svc-name`, `.svc-desc` e `.price-table`;
4. aggiungere righe corrispondenti in `#prezzi`;
5. aggiungere option nel select `#inp-svc`;
6. verificare gli attributi `data-i`, `data-d` e `data-e`;
7. testare desktop e mobile.

## Modificare contatti

Punti da aggiornare:

- telefono visibile in info band;
- link `tel:` nella sezione contatti;
- testo visibile del telefono;
- email visibile;
- link `mailto:`;
- variabili JS `QR_IT`, `QR_DE`;
- `handleSubmit()` se cambia indirizzo email di destinazione.

Nota: il link `tel:` attuale è mascherato come `tel:+417****5061`, mentre il testo visibile mostra il numero completo. Per click-to-call reale, il valore `href` dovrebbe contenere un numero valido, ad esempio senza spazi.

## Modificare immagini

- Logo: sostituire `logo.png`, mantenendo nome e proporzioni simili.
- Sfondo atmosferico: sostituire `atmo-bg.jpg`.
- Hero: URL remoto Unsplash dentro `.hero-bg-img` nel CSS.
- Gallerie/card: molte immagini sono data URI base64 dentro `index.html`; per manutenzione migliore conviene estrarle in file separati, ad esempio `assets/`, e usare path relativi.

## Test manuale dopo modifiche

Checklist minima:

- aprire `index.html` o servire con `python3 -m http.server 8000`;
- verificare lingua DE iniziale;
- cliccare IT e verificare testi/placeholder/select/QR;
- cliccare EN e verificare testi/placeholder/select/QR;
- cliccare DE e verificare ritorno corretto;
- cliccare navigazione;
- provare submit form e controllare bozza email;
- provare QR code;
- verificare layout sotto 768px;
- controllare link telefono/email.

## Deploy

Essendo sito statico, può essere pubblicato su qualunque hosting statico:

- Netlify;
- Vercel static;
- GitHub Pages;
- server Nginx/Apache;
- bucket statico cloud.

È sufficiente caricare:

- `index.html`;
- `logo.png`;
- `atmo-bg.jpg`.

Se in futuro si estraggono immagini base64 in file separati, includere anche la cartella asset.
