# Review accessibilità, SEO e performance

## Sintesi

Il sito è visivamente coerente e adatto a una landing page premium/wellness. La struttura è stata riorganizzata per Netlify con asset separati e diversi miglioramenti accessibilità/SEO già applicati. Restano alcuni consigli opzionali per privacy/performance avanzate.

## Punti positivi

- Sito statico, senza backend e quindi con superficie d'attacco ridotta.
- Meta viewport presente.
- Meta description presente.
- Layout responsive sotto 768px.
- Navigazione ad anchor semplice.
- Brand visuale coerente: navy, oro, font eleganti, immagini atmosferiche.
- CTA chiara verso contatto/prenotazione.
- Supporto multilingue IT/DE/EN implementato senza framework.

## Rischi e problemi rilevati

### 1. Prezzi non allineati

Le card principali, la tabella `#prezzi` e le option del form sono state allineate per massaggio classico, linfodrenaggio, testa/collo, massaggio prenatale e RESET. La nota prezzi include anche i pacchetti gravidanza.

### 2. Link telefono non valido

Il link `tel:` è stato normalizzato in formato E.164 senza spazi, coerente con il numero visibile.

Raccomandazione: verificare una volta su smartphone che il click-to-call apra correttamente telefono/WhatsApp.

### 3. HTML molto grande

`index.html` è stato alleggerito estraendo le immagini base64 in `assets/images/inline-*.jpg`.

Risultato:

- HTML più piccolo;
- caching degli asset più efficace su Netlify;
- manutenzione immagini più semplice.

### 4. Dipendenze esterne non pin/self-hosted

Il sito dipende da:

- Google Fonts;
- CDNJS QRCode.js;
- immagine hero Unsplash remota.

Impatto: se una risorsa esterna non risponde, font/QR/hero possono degradare.

Raccomandazione: valutare self-hosting di font, QRCode.js e immagine hero per massima affidabilità.

### 5. Accessibilità del language switcher

I bottoni IT/DE hanno `aria-label` e `aria-pressed`.

### 6. Form senza attributi `name`

Gli input hanno `id`, `name`, `autocomplete` e label collegate via `for`.

### 7. Stato successo form potenzialmente fuorviante

Dopo `window.location.href = mailto:...`, il messaggio chiarisce che si aprirà l'app email con testo precompilato. L'invio finale resta nel client email dell'utente.

## SEO

### Presente

- `<title>` descrittivo: `Michela Massage – Zürich`.
- Meta description utile in tedesco.
- Un solo `<h1>`.
- Sezioni con heading coerenti.

### Miglioramenti consigliati

- Aggiungere meta description anche italiana non è direttamente possibile nello stesso meta standard; valutare landing separate o `hreflang` se si creano URL dedicati.
- Aggiungere dati strutturati JSON-LD per LocalBusiness/HealthAndBeautyBusiness.
- Aggiungere Open Graph/Twitter Card per condivisione social.
- Migliorare `alt` delle immagini decorative/servizio. Molte immagini base64 non hanno descrizioni specifiche.

## Performance

Priorità consigliate:

1. Estrarre immagini base64 in file separati.
2. Ottimizzare/comprimere immagini.
3. Self-host o preload dei font essenziali.
4. Usare `loading="lazy"` sulle immagini non above-the-fold.
5. Valutare `defer` per QRCode.js o caricamento solo quando la sezione contatti entra nel viewport.

## Sicurezza e privacy

- Nessuna raccolta dati server-side.
- Il form usa `mailto:`, quindi i dati restano nel client email dell'utente.
- La pagina carica risorse da terze parti, esponendo richieste a Google Fonts, CDNJS, Unsplash.

Raccomandazione privacy: se il sito è destinato a utenti in Svizzera/UE, valutare una privacy policy minima e self-hosting font/asset esterni.

## Checklist pre-pubblicazione

- [ ] Allineare prezzi in card, tabella e form.
- [ ] Correggere `tel:`.
- [ ] Verificare tutte le traduzioni IT/DE.
- [ ] Testare QR code in entrambe le lingue.
- [ ] Testare form su desktop e mobile.
- [ ] Ottimizzare immagini e valutare estrazione da base64.
- [ ] Aggiungere Open Graph e JSON-LD local business.
- [ ] Verificare Lighthouse mobile/desktop.
