# uW2ptx

## Scripts for converting UnfoldingWord Resources for use within Paratext
UnfoldingWord has published several BT related resources in several Gateway Languages. However these resources are available only through the uW suites. However these resources are released under a CC-BY-SA licenses. This repo is a collection of scripts that can be used for converting the uW resources in formats that are supported by Paratext, the popular Bible editing tool. 

### TranslationNotes (tN)
The tranlationNotes on the uW repo is found in primarily as .tsv (tab seperated values) files and to our best knowledge, the .tsv is going to be the standard uW going to maintain the files in the future. At the same time, some files are still kept in the .md (markdown) fomat. 

### parsetN-md2tN-usfm.ipynb
This script will convert the .md files on the uW repo into a usfm file. 

[Sample mark down file](https://git.door43.org/benVar/ml_tn/src/branch/master/1co/01/01.md)
```markdown
# നമ്മുടെ സഹോദരനായ സോസ്തെനെസ്

ഇതു സൂചിപ്പിക്കുന്നത് പൗലൊസിനും കൊരിന്ത്യർക്കും സോസ്തെനെസിനെ പരിചയമുണ്ടായിരുന്നു എന്നാണ് ഇതുകൊണ്ട് അർത്ഥമാക്കുന്നത്. AT: <<നീയും ഞാനും അറിയുന്നവനായ സോസ്ത്നെസ്>> [പേരുകളുടെ പരിഭാഷ കാണുക]

# വിശുദ്ധന്മാരാകുവാൻ വിളിക്കപ്പെട്ടവർ

AT: <<ദൈവം അവരെ വിശുദ്ധരാകുവനായി വിളിച്ചു>> {കാണുക: കർത്തരി പ്രയോഗം അല്ലെങ്കിൽ കർമ്മണിപ്രയോഗം]
```

Expected output
```usfm
\id 1CO
\c 1
\p
\tr \tc1 നമ്മുടെ സഹോദരനായ സോസ്തെനെസ്
\tr \tc1 ഇതു സൂചിപ്പിക്കുന്നത് പൗലൊസിനും കൊരിന്ത്യർക്കും സോസ്തെനെസിനെ പരിചയമുണ്ടായിരുന്നു എന്നാണ് ഇതുകൊണ്ട് അർത്ഥമാക്കുന്നത്. AT: <<നീയും ഞാനും അറിയുന്നവനായ സോസ്ത്നെസ്>> [പേരുകളുടെ പരിഭാഷ കാണുക]
\b
\tr \tc1 വിശുദ്ധന്മാരാകുവാൻ വിളിക്കപ്പെട്ടവർ
\tr \tc1 AT: <<ദൈവം അവരെ വിശുദ്ധരാകുവനായി വിളിച്ചു>> {കാണുക: കർത്തരി പ്രയോഗം അല്ലെങ്കിൽ കർമ്മണിപ്രയോഗം]
\b
```
