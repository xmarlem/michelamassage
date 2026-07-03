# Documentazione sito Michela Massage

Questa cartella documenta il sito statico contenuto in `index.html`.

## Scopo del sito

Landing page multilingue italiano/tedesco/inglese per Michela Massage, attività di massaggi e linfodrenaggio a Zürich. Il sito presenta:

- identità e posizionamento del brand;
- trattamenti disponibili;
- prezzi e note su riconoscimento ASCA/EMR;
- informazioni pratiche su sede, disponibilità e contatti;
- form di richiesta appuntamento tramite `mailto:`;
- QR code per apertura rapida di una bozza email.

## File principali

| File | Ruolo |
| --- | --- |
| `README.md` | Guida principale per sviluppo, verifiche e deploy. |
| `index.html` | Markup principale della single page. |
| `assets/css/styles.css` | Stili del sito. |
| `assets/js/main.js` | Logica cambio lingua, QR code, reveal animation e form mailto. |
| `assets/images/` | Logo, sfondo e immagini decorative/servizi. |
| `netlify.toml` | Configurazione deploy Netlify senza build step. |
| `Makefile` | Target per sviluppo locale, lint, check e deploy Netlify. |
| `AGENTS.md` | Istruzioni operative caricate da Hermes per questo progetto. |
| `scripts/` | Script Python per validazioni e smoke test senza dipendenze esterne. |
| `docs/` | Documentazione tecnica e contenutistica del sito. |

## Stack tecnico

- HTML statico single page.
- CSS separato in `assets/css/styles.css`.
- JavaScript vanilla separato in `assets/js/main.js`.
- Font caricati da Google Fonts:
  - Cormorant Garamond;
  - Cinzel;
  - Lato.
- Libreria esterna QRCode.js da CDNJS.
- Nessun framework, nessun bundler, nessun package manager.

## Documenti disponibili

- `architecture.md` — struttura tecnica, componenti e dipendenze.
- `content-map.md` — mappa sezioni, testi, servizi e contatti.
- `maintenance.md` — come modificare testi, prezzi, lingua, immagini e contatti.
- `accessibility-seo-review.md` — analisi SEO/accessibilità/performance con rischi e miglioramenti.
- `netlify-deploy.md` — istruzioni e checklist per deploy Netlify.
- `netlify-snapshot-compare.md` — procedura per mantenere online uno snapshot precedente e confrontarlo visivamente dopo il deploy.
- `development-workflow.excalidraw` — diagramma editabile del workflow di sviluppo Hermes/AI.
- `session-log.md` — riepilogo conciso dell'ultima sessione di lavoro.
- `current-task.md` — prossimo passo operativo consigliato.

## Avvio locale

È possibile aprire direttamente `index.html` nel browser. Per testare come sito servito via HTTP:

```bash
python3 -m http.server 8000
```

Poi aprire:

```text
http://localhost:8000
```


## Workflow sviluppo

La guida principale per contributori/operatori è `README.md` nella root del progetto. Comandi principali:

```bash
make help
make serve
make check
make final-check
make deploy-prod
```

Usare `make final-check` prima di chiudere task/sessioni che hanno modificato codice, contenuti, configurazione, deploy, accessibilità, SEO o documentazione.

Vedi `docs/netlify-deploy.md` per dettagli sui target.
