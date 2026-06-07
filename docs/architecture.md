# Architettura tecnica

## Panoramica

Il sito è una single page statica riorganizzata per deploy semplice su Netlify:

- `index.html` contiene il markup delle sezioni;
- `assets/css/styles.css` contiene lo stile visuale;
- `assets/js/main.js` contiene cambio lingua IT/DE, animazioni scroll/reveal, generazione QR code e gestione form `mailto:`;
- `assets/images/` contiene immagini e logo;
- `netlify.toml` contiene impostazioni di deploy, cache e security headers.

Non esiste backend: l'invio messaggio non salva dati e non chiama API server-side.

## Struttura della pagina

Ordine principale del documento:

1. `head`
   - metadata base;
   - meta description in tedesco;
   - Google Fonts;
   - QRCode.js da CDN;
   - stylesheet esterno `assets/css/styles.css`.
2. `body`
   - language switcher fisso;
   - navigazione fissa;
   - hero;
   - image strip;
   - about;
   - blocco atmosferico;
   - servizi;
   - prezzi;
   - info band;
   - gallery;
   - contatti/form/QR;
   - footer;
   - JavaScript esterno `assets/js/main.js`.

## Sezioni e anchor

| Anchor/ID | Scopo |
| --- | --- |
| `#top` | Hero iniziale. |
| `#about` | Profilo Michela e certificazioni. |
| `#servizi` | Card dei trattamenti. |
| `#prezzi` | Tabella prezzi e note ASCA/EMR. |
| `#info` | Posizione, disponibilità e telefono. |
| `#contatti` | Contatti, QR code e form mailto. |

## CSS

Il CSS è inline e basato su variabili nel `:root`:

| Variabile | Valore | Uso |
| --- | --- | --- |
| `--navy` | `#0d1b2a` | sfondo principale scuro. |
| `--navy-mid` | `#16263a` | sezioni alternate. |
| `--gold` | `#c9a84c` | accenti, bordi, linee. |
| `--gold-light` | `#e4c97e` | testi/accenti evidenziati. |
| `--cream` | `#faf7f0` | testo principale chiaro. |
| `--white` | `#fff` | titoli/logo contrasto. |
| `--muted` | `#8fa3b8` | testo secondario. |

Pattern CSS principali:

- layout a griglia per about, servizi, prezzi, contatti;
- media query mobile sotto `768px`;
- animazioni `fadeUp`, `drift`, `lineGrow`, `pulse`;
- classe `.reveal` attivata da IntersectionObserver;
- navbar con classe `.scrolled` dopo scroll verticale maggiore di 60px.

## JavaScript

Funzioni principali:

| Funzione | Responsabilità |
| --- | --- |
| `buildQR(l)` | Rigenera il QR code con URL `mailto:` italiano o tedesco. |
| `setLang(l)` | Cambia lingua, aggiorna `html.lang`, testi `data-i/data-d`, placeholder, option select e bottone attivo. |
| scroll listener | Aggiunge/rimuove `nav.scrolled`. |
| IntersectionObserver | Mostra gli elementi `.reveal` quando entrano nel viewport. |
| `handleSubmit(e)` | Costruisce una mail precompilata e imposta `window.location.href` su `mailto:`. |

## Dipendenze esterne

| Dipendenza | Fonte | Impatto |
| --- | --- | --- |
| Google Fonts | `fonts.googleapis.com` | Tipografia brand; richiede rete. |
| QRCode.js | `cdnjs.cloudflare.com` | Generazione QR code; se CDN non disponibile il QR non funziona. |
| Unsplash hero image | URL remoto `images.unsplash.com` | Immagine hero; se rete non disponibile resta overlay/scuro. |

## Asset locali

- `logo.png`: immagine PNG del logo, usata in navbar, hero e footer.
- `atmo-bg.jpg`: sfondo locale per blocco atmosferico.

Le immagini decorative precedentemente inline sono state estratte in `assets/images/inline-*.jpg`. Questo riduce la dimensione di `index.html`, migliora caching e manutenzione.
