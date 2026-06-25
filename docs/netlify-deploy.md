# Deploy su Netlify

Il sito è configurato per essere deployato su Netlify senza build step.

## Struttura consigliata

```text
.
├── index.html
├── netlify.toml
├── assets/
│   ├── css/styles.css
│   ├── js/main.js
│   └── images/
│       ├── logo.png
│       ├── atmo-bg.jpg
│       └── inline-*.jpg
└── docs/
```

## Impostazioni Netlify

Se colleghi il repository da dashboard Netlify:

- Build command: lasciare vuoto
- Publish directory: `.`
- Base directory: vuota, se il repo contiene direttamente `index.html`

Il file `netlify.toml` imposta già:

- publish directory su `.`;
- nessun comando di build;
- security headers base;
- cache lunga per `/assets/*`;
- revalidation per `index.html`.

## Progetto Netlify collegato

Il sito è stato inizializzato con `netlify init` in modalità manuale, senza repository Git remoto.

Dettagli progetto:

| Campo | Valore |
| --- | --- |
| Team | Marco Lembo's team |
| Project name | `michelamassage` |
| Admin URL | `https://app.netlify.com/projects/michelamassage` |
| Site URL | `https://michelamassage.netlify.app` |
| Project ID | `ae891950-b3cc-4a6f-baa4-f483277b32f5` |
| CLI deploy target | `michelamassage` |
| Deploy mode | Manuale, senza Git remote |

Durante l'inizializzazione Netlify ha chiesto:

```text
No git remote was found, would you like to set one up?
```

È stata scelta l'opzione:

```text
Yes, create and deploy project manually
```

Questo significa che Netlify non farà deploy automatici da branch/PR. I deploy vanno lanciati localmente con Netlify CLI o tramite drag-and-drop/dashboard.

## Deploy manuale rapido

Prima di deployare, eseguire sempre i controlli locali:

```bash
make check
```

Deploy preview:

```bash
make deploy
```

Il target esegue internamente:

```bash
netlify deploy --no-build --dir . --site michelamassage
```

oppure direttamente:

```bash
netlify deploy
```

Deploy produzione:

```bash
make deploy-prod
```

Il target esegue internamente:

```bash
netlify deploy --prod --no-build --dir . --site michelamassage
```

oppure direttamente:

```bash
netlify deploy --prod
```

Quando Netlify chiede la directory da pubblicare, usare:

```text
.
```

Dopo il deploy produzione, il sito sarà disponibile su:

```text
https://michelamassage.netlify.app
```

## Cosa è stato migliorato per il deploy

- CSS separato in `assets/css/styles.css`.
- JavaScript separato in `assets/js/main.js`.
- Immagini base64 estratte in `assets/images/inline-*.jpg`.
- Logo e sfondo copiati in `assets/images/`.
- Configurazione Netlify aggiunta in `netlify.toml`.
- Dimensione di `index.html` ridotta molto rispetto alla versione con immagini inline.

## Cosa è stato migliorato per accessibilità/SEO

- Skip link verso il contenuto principale.
- Landmark `<main>`.
- `aria-label` per navigazione e cambio lingua.
- `aria-pressed` sui pulsanti lingua.
- Focus visibile per tastiera.
- `prefers-reduced-motion` per utenti sensibili alle animazioni.
- Label collegate ai campi form tramite `for`/`id`.
- Attributi `name` e `autocomplete` nei campi form.
- Messaggio chiaro: il form apre il client email, non invia direttamente.
- Link telefono normalizzato in formato `tel:` valido.
- Tabella prezzi allineata ai prezzi delle card principali.
- Meta Open Graph base.
- JSON-LD `HealthAndBeautyBusiness`.


## Development workflow con Makefile

Sono disponibili target per sviluppo locale, controlli e deploy:

```bash
make help          # mostra tutti i target
make serve         # avvia il sito locale su http://127.0.0.1:8000
make serve PORT=8080
make check         # refs + validate + lint + smoke test
make docs-check    # verifica documentazione e checklist project/agent
make final-check   # check + docs-check, da usare prima di chiudere il task
make lint          # lint HTML/CSS/JS con fallback built-in
make refs          # controlla riferimenti asset locali
make validate      # valida netlify.toml, JSON-LD e meta base
make smoke         # server temporaneo + richieste HTTP agli asset principali
make netlify-status # mostra account/sito Netlify collegato
make deploy         # deploy preview Netlify su directory .
make deploy-prod    # deploy produzione Netlify su directory .
make deploy-open    # stampa URL produzione Netlify
make clean          # rimuove cache temporanee
```

I target `lint-html` e `lint-css` usano `htmlhint`/`stylelint` se installati. Se non sono disponibili, usano i controlli Python in `scripts/check_site.py`, così il workflow funziona anche senza installare dipendenze Node.

I target `deploy` e `deploy-prod` usano il nome progetto `michelamassage` come valore `--site`, perché con Netlify CLI 26 il deploy autenticato funziona in modo affidabile con il nome progetto in questo ambiente. Il Project ID rimane documentato per identificare il sito nella dashboard/API, ma non è il valore usato dal Makefile per il deploy.

Usare `make final-check` prima di chiudere una sessione o un task che ha modificato codice, contenuti, configurazione, accessibilità, SEO, deploy o documentazione. Il target esegue i controlli tecnici e verifica che la documentazione/checklist di progetto sia presente e aggiornata.

## Checklist prima di andare online

- [ ] Verificare che i prezzi del massaggio prenatale siano corretti o lasciati volutamente come `— CHF`.
- [ ] Verificare che il numero telefono e l'email siano definitivi.
- [ ] Testare il form su mobile: deve aprire l'app email.
- [ ] Testare il QR code in tedesco e italiano.
- [ ] Eseguire Lighthouse da Chrome DevTools su mobile e desktop.
- [ ] Se vuoi massima privacy/performance, scaricare e servire localmente anche Google Fonts, QRCode.js e immagine hero Unsplash.
