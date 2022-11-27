# N00bHack

**Auteur:** bWlrYQ  
**Catégorie:** Forensic  
**Enoncé:** En TP lors de la pause Louis laisse toujours son ordinateur déverrouillé et sans surveillance, il a confiance en ses camarades... Lorsqu'il revient de la cafétaria Maxence l'informe qu'il a vu quelqu'un rôder autour de son ordinateur. Dans le doute nous avons réalisé un dump de la RAM pour que vous puissiez l'analyser et identifier une trace d'un quelconque acte malveillant.

Pour commencer, identifiez l'OS ainsi que le Kernel associés au dump de mémoire qui vous est fourni. Le flag est de la forme FMCTF{OS:Version_Kernel}  

Afin de rester discret le pirate a sûrement trouvé un moyen de contrôler la machine à distance. Identifier le programme qui lui a servi à faire cela. Le flag est de la forme FMCTF{nom_du_programme}  

Maintenant que vous avez identifié le programme malveillant retrouvez l'adresse IP du C2 associé au programme. Le format du flag est FMCTF{ip}  
**Sources fournies:** Debian_4.19.0-22-amd64_profile.zip, dump.mem  
**Niveau:** Moyen  
**Flags:**  
FMCTF{Debian:4.19.0-22}  
FMCTF{TP_R314}  
FMCTF{51.75.247.236}  