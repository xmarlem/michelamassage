# Snapshot Netlify per confronto visivo dopo il deploy

Questa procedura serve a mantenere online due versioni del sito per un confronto visivo:

- la versione precedente, pubblicata su un secondo progetto Netlify di snapshot;
- la versione nuova, pubblicata sul progetto Netlify principale.

Lo snapshot non è un vero ambiente di preproduzione continuo. È solo una copia temporanea della versione attuale, utile per aprire i due siti affiancati e controllare cosa è cambiato dopo il deploy.

## Nomi usati

| Scopo | Progetto Netlify | URL |
| --- | --- | --- |
| Produzione | `michelamassage` | `https://michelamassage.netlify.app` |
| Snapshot precedente | `michelamassage-old` | `https://michelamassage-old.netlify.app` |

Il progetto snapshot esiste già su Netlify:

- Project name: `michelamassage-old`
- Project ID: `c8ab4977-964e-4404-a941-e79cd95aeabc`
- Site URL: `https://michelamassage-old.netlify.app`

Se `michelamassage-old` non fosse disponibile in futuro, usare un nome simile, ad esempio:

- `michelamassage-snapshot`
- `michelamassage-before-update`
- `michelamassage-old-2026`

## Quando usare questa procedura

Usarla prima di pubblicare una nuova versione in produzione, quando vuoi poter consultare anche la versione precedente dopo il deploy.

Ordine corretto:

1. creare o aggiornare lo snapshot della versione attuale;
2. verificare che lo snapshot sia online;
3. pubblicare la nuova versione sul sito principale;
4. confrontare visivamente i due URL.

## Prerequisiti

Da terminale, entrare nella cartella del progetto:

```bash
cd /home/hermes/workspace/michela-site
```

Verificare lo stato Git:

```bash
git status
```

Idealmente il working tree deve essere pulito, oppure devi sapere esattamente quali modifiche stai includendo nello snapshot.

Verificare Netlify CLI:

```bash
netlify status
```

Se non sei autenticato:

```bash
netlify login
```

## 1. Verificare il progetto Netlify snapshot

Il progetto `michelamassage-old` esiste già, quindi normalmente non va creato.

Per verificarlo:

```bash
netlify sites:list
```

Nell'elenco deve comparire:

```text
michelamassage-old - c8ab4977-964e-4404-a941-e79cd95aeabc
  url:  https://michelamassage-old.netlify.app
```

Se in futuro il progetto non esistesse più, ricrearlo con:

```bash
netlify sites:create --name michelamassage-old
```

In alternativa, puoi crearlo dalla dashboard Netlify:

1. apri Netlify;
2. crea un nuovo sito/progetto;
3. usa il nome `michelamassage-old`;
4. non serve collegarlo a Git se il deploy resta manuale.

## 2. Eseguire i controlli locali

Prima di salvare lo snapshot, eseguire i controlli del progetto:

```bash
make check
```

Se il controllo fallisce, correggere prima il problema. Lo snapshot deve rappresentare una versione consultabile e funzionante.

## 3. Creare una copia temporanea dello stato attuale

Non deployare direttamente la cartella di lavoro sul progetto snapshot, perché per lo snapshot vogliamo aggiungere `noindex` senza modificare il sito principale.

Creare una directory temporanea:

```bash
SNAPSHOT_DIR="$(mktemp -d)"
```

Copiare il sito nella directory temporanea:

```bash
rsync -a --delete ./ "$SNAPSHOT_DIR"/ \
  --exclude .git \
  --exclude node_modules \
  --exclude .netlify
```

## 4. Aggiungere `noindex` allo snapshot

Questo evita che Google o altri motori di ricerca indicizzino la copia precedente del sito.

Creare il file `_headers` solo nella copia temporanea:

```bash
cat > "$SNAPSHOT_DIR/_headers" <<'EOF'
/*
  X-Robots-Tag: noindex, nofollow
EOF
```

Questa modifica non tocca il sito principale, perché viene fatta solo dentro `SNAPSHOT_DIR`.

## 5. Pubblicare la versione precedente sul progetto snapshot

Deploy produzione dello snapshot:

```bash
netlify deploy \
  --prod \
  --no-build \
  --dir "$SNAPSHOT_DIR" \
  --site michelamassage-old \
  --message "Snapshot before production update"
```

Alla fine Netlify mostrerà l'URL dello snapshot, ad esempio:

```text
https://michelamassage-old.netlify.app
```

Aprire l'URL e verificare che mostri ancora la versione precedente del sito.

## 6. Pubblicare la nuova versione sul sito principale

Dopo aver preparato la nuova versione del sito, eseguire di nuovo i controlli:

```bash
make check
```

Poi pubblicare in produzione sul progetto principale:

```bash
make deploy-prod
```

Il target usa internamente il progetto Netlify `michelamassage` e la directory di pubblicazione `.`.

Comando equivalente, se serve eseguirlo direttamente:

```bash
netlify deploy \
  --prod \
  --no-build \
  --dir . \
  --site michelamassage \
  --message "Production update"
```

## 7. Fare il confronto visivo

Aprire i due siti affiancati:

- snapshot precedente: `https://michelamassage-old.netlify.app`
- produzione nuova: `https://michelamassage.netlify.app`

Controllare almeno:

- home page desktop;
- home page mobile;
- testi principali;
- prezzi;
- lingua italiana/tedesca;
- immagini;
- form di contatto;
- link telefono/email;
- QR code, se presente.

## 8. Pulizia opzionale

Quando lo snapshot non serve più, puoi lasciarlo online oppure eliminarlo dalla dashboard Netlify.

Se vuoi rimuovere solo la directory temporanea locale:

```bash
rm -rf "$SNAPSHOT_DIR"
```

Attenzione: eseguire questo comando solo se `SNAPSHOT_DIR` è ancora valorizzata correttamente nella stessa sessione terminale.

## Sequenza rapida completa

Questa è la sequenza breve da usare quando il progetto snapshot esiste già:

```bash
cd /home/hermes/workspace/michela-site

git status
make check

SNAPSHOT_DIR="$(mktemp -d)"

rsync -a --delete ./ "$SNAPSHOT_DIR"/ \
  --exclude .git \
  --exclude node_modules \
  --exclude .netlify

cat > "$SNAPSHOT_DIR/_headers" <<'EOF'
/*
  X-Robots-Tag: noindex, nofollow
EOF

netlify deploy \
  --prod \
  --no-build \
  --dir "$SNAPSHOT_DIR" \
  --site michelamassage-old \
  --message "Snapshot before production update"
```

Poi, quando la nuova versione è pronta:

```bash
make check
make deploy-prod
```

URL da confrontare:

```text
Snapshot precedente: https://michelamassage-old.netlify.app
Produzione nuova:   https://michelamassage.netlify.app
```

## Note importanti

- Lo snapshot va creato prima del deploy nuovo, altrimenti salverebbe già la nuova versione.
- Lo snapshot non deve essere usato come ambiente di lavoro continuo.
- Il file `_headers` con `X-Robots-Tag: noindex, nofollow` viene aggiunto solo alla copia temporanea.
- Per il progetto principale usare `make deploy-prod`, come documentato in `docs/netlify-deploy.md`.
- In questo progetto il deploy Netlify funziona in modo affidabile usando il nome sito `michelamassage` come valore di `--site`.
