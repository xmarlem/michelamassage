   Step 1 fatto e committato.
    
    Ho applicato il prompt senza introdurre nuovi pacchetti/prezzi non confermati.
    
    Modifiche principali:
    - Hero:
      - aggiunto “Oerlikon · Zürich”
      - nuova tagline:
        “Dein Raum, um langsamer zu werden, auf deinen Körper zu hören und Balance zu finden.”
    - About:
      - reso il tono più personale e meno “marketing”
      - aggiunta l’idea:
        “ogni trattamento parte da come arrivi oggi…”
      - aggiunta l’idea:
        “il tempo dedicato a te diventa cura”
      - aggiunta la frase sul prendersi cura di sé non come lusso superfluo
    - Blocco atmosferico:
      - nuova frase:
        “Wo die Zeit für dich zur Fürsorge wird.”
    - Linfodrenaggio:
      - aggiornato copy per dire che è uno strumento usato quando indicato e adattato alla persona.
    - SEO/metadati:
      - title/meta/OG/JSON-LD aggiornati con Oerlikon Zürich e nuovo posizionamento.
    - Documentazione:
      - aggiornati docs/README.md e docs/content-map.md
      - aggiunto e committato il prompt sorgente in docs/prompts/enrichment.prompt.md
    
    Verifiche:
    - make final-check → ok
    - preview locale:
      - http://127.0.0.1:8000/
    - marker verificati nel sito locale:
      - Oerlikon · Zürich · ASCA / EMR Anerkannt
      - Dein Raum, um langsamer zu werden
      - Wo die Zeit für dich zur Fürsorge wird
      - Ich biete keine Standardmassage an
      - Die manuelle Lymphdrainage hilft dem Körper
    
    Commit:
    881b006 feat: enrich brand positioning copy
    
    Restano fuori:
    - docs/analysis/competitor-comparison-ischia-massage.it.md
    - immagini analysis non tracciate.
    
    Prossimo step consigliato:
    Step 2 lo farei come analisi guidata dei nuovi percorsi:
    - RESET & BALANCE — CHF 495
    - RESTORE — CHF 690
    - Ciclo benessere mensile
    
    Prima di implementarli nel sito, ti propongo di preparare una mini-tabella decisionale: cosa è già compatibile con il listino attuale, cosa crea conflitto, e quali nomi/prezzi vanno confermati. Poi, solo se mi confermi, li trasformo in una sezione “Percorsi di benessere”.