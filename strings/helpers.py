#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

HELP_1 = """✅ **<u>Admin Əmrləri:</u>**

**c** kanal oynatmağı nəzərdə tutur.

/pause və ya /cpause - Oxunan musiqini dayandırın.
/resume və ya /cresume - dayandırılmış musiqini davam etdirin.
/mute və ya /cmute - Oynanan musiqinin səsini söndürün.
/unmute və ya /cunmute - Səssiz musiqinin səsini açın.
/skip və ya /cskip - Cari ifa olunan musiqini keçin.
/stop və ya /cstop - Oynanan musiqini dayandırın.
/shuffle və ya /cshuffle - Növbəyə qoyulmuş çalğı siyahısını təsadüfi qarışdırır.
/seek və ya /cseek - İrəli Musiqini öz müddətinizə qədər axtarın.
/seekback və ya /cseekback - Geriyə Musiqini müddətinizə qədər axtarın.
/restart - Söhbətiniz üçün botu yenidən başladın.


✅ <u>**Xüsusi keçid:**</u>
/skip və ya /cskip [Nömrə(misal: 3)] - Müəyyən edilmiş növbəli nömrəyə musiqini keçir. Nümunə: /skip 3 musiqini üçüncü növbəli musiqiyə ötürəcək və növbədəki 1 və 2 musiqiyə məhəl qoymayacaq.

✅ <u>**Loop Play:**</u>
/loop və ya /clop [enable/disable] və ya [1-10 arası rəqəmlər] - Aktivləşdirildikdə, bot səsli söhbətdə cari ifa olunan musiqini 1-10 dəfə çevirir. Varsayılan olaraq 10 dəfə.

✅ <u>**Auth İstifadəçiləri:**</u>
Auth İstifadəçiləri söhbətinizdə admin hüquqları olmadan admin əmrlərindən istifadə edə bilərlər.

/auth [İstifadəçi adı] - Qrupun AUTH SİYAHISINA istifadəçi əlavə edin.
/unauth [İstifadəçi adı] - Qrupun AUTH LIST-dən istifadəçini çıxarın.
/authusers - Qrupun AUTH SİYAHISINI yoxlayın."""


HELP_2 = """✅ <u>**Play Əmrləri:**</u>

Mövcud Əmrlər = play , vplay , cplay

ForcePlay Əmrləri = playforce , vplayforce , cplayforce

**c** kanal oynatmağı nəzərdə tutur.
**v** video oynatma deməkdir.
**force** güc oyunu deməkdir.

/play və ya /vplay və ya /cplay - Bot verdiyiniz sorğunu səsli söhbətdə oynamağa başlayacaq və ya səsli söhbətlərdə canlı bağlantıları yayımlayacaq.

/playforce və ya /vplayforce və ya /cplayforce - **Force Play** səsli çatda cari ifa olunan treki dayandırır və növbəni pozmadan axtarılan treki dərhal ifa etməyə başlayır.

/channelplay [Söhbət istifadəçi adı və ya id] və ya [Disable] - Kanalı qrupa qoşun və qrupunuzdan kanalın səsli söhbətində musiqi yayımlayın.


✅ **<u>Botun Server çalğı siyahıları:</u>**
/playlist - Serverlərdə Saxlanmış Pleylistinizi Yoxlayın.
/deleteplaylist - Pleylistinizdə saxlanan hər hansı musiqini silin
/play - Serverlərdən Saxlanmış Pleylistinizi oynatmağa başlayın."""


HELP_3 = """✅ <u>**Bot Əmrləri:**</u>

/stats - Qlobal Statistikanın ən yaxşı 10 musiqisini əldə edin, botun ən yaxşı 10 istifadəçisi, botda ən yaxşı 10 söhbət, söhbətdə oynanan ən yaxşı 10 və s.

/sudolist - Bot-un Sudo İstifadəçilərini yoxlayın.

/lyrics [Musiqi Adı] - Vebdə xüsusi Musiqi üçün Lirikləri axtarır.

/song [Track Name] və ya [YT Link] - YouTube-dan mp3 və ya mp4 formatlarında istənilən treki yükləyin.

/player - İnteraktiv Oyun Paneli əldə edin.

**c** kanal oynatmağı nəzərdə tutur.

/queue və ya /cqueue - Musiqi növbə siyahısını yoxlayın."""

HELP_4 = """✅ <u>**Əlavə Əmrlər:**</u>
/start - Musiqi Botunu işə salın.
/help - Əmrlərin təfərrüatlı izahatları ilə Əmrlər Köməkçisi Menyu əldə edin.
/ping - Botu pingləyin və Botun Ram, CPU və s. statistikasını yoxlayın.

✅ <u>**Qrup Parametrləri:**</u>
/settings - Daxili düymələrlə tam qrup parametrlərini əldə edin.

🔗 **Parametrlərdəki Seçimlər:**

1️⃣ Siz səsli söhbətdə yayımlamaq istədiyiniz **Audio Keyfiyyətini** təyin edə bilərsiniz.

2️⃣ Siz səsli söhbətdə yayımlamaq istədiyiniz **Video Keyfiyyətini** təyin edə bilərsiniz.

3️⃣ **Auth İstifadəçiləri:** Siz buradan admin əmrləri rejimini hamıya və ya yalnız adminlərə dəyişə bilərsiniz. Əgər hər kəs, qrupunuzda olan hər kəs admin əmrlərindən istifadə edə biləcək (məsələn, /skip, /stop və s.)

4️⃣ **Təmiz Rejimi:** Aktiv olduqda, söhbətinizin təmiz və yaxşı qalmasına əmin olmaq üçün botun mesajlarını 5 dəqiqədən sonra qrupunuzdan silir.

5️⃣ **Command Clean:** Aktivləşdirildikdə, Bot yerinə yetirilmiş əmrləri (/play, /pause, /shuffle, /stop və s.) dərhal siləcək.

6️⃣ **Play Parametrləri:**

/playmode - Qrupunuzun oyun parametrlərini təyin edə biləcəyiniz düymələri olan tam oyun parametrləri paneli əldə edin.

<u>Oyun Rejimində Seçimlər:</u>

1️⃣ **Axtarış Rejimi:** [Birbaşa və ya Daxil] - Siz /play rejimini verərkən axtarış rejiminizi dəyişir.

2️⃣ **Admin Əmrləri:** [Hər kəs və ya Adminlər] - Qrupunuzda olan hər kəs admin əmrlərindən istifadə edə biləcək (məsələn, /skip, /stop və s.)

3️⃣ **Oyun Növü** [Hər kəs və ya Adminlər] - Adminlərsə, yalnız qrupda olan adminlər səsli çatda musiqi oxuya bilər."""

HELP_5 = """🔰 **<u>Sudo İstifadəçilərini Əlavə Edin Və Silin:</u>**
/addsudo [İstifadəçi adı və ya istifadəçiyə cavab]
/delsudo [İstifadəçi adı və ya istifadəçiyə cavab]

🛃 **<u>Heroku:</u>**
/usage - Dyno İstifadəsi.

🌐 **<u>Varları Confıg:</u>**
/get_var - Heroku və ya .env-dən konfiqurasiya var əldə edin.
/del_var - Heroku və ya .env-də hər hansı bir var silin.
/set_var [Var Adı] [Dəyər] - Heroku və ya .env-də Var təyin edin və ya Varı yeniləyin. Var və onun dəyərini boşluqla ayırın.
🤖 **<u>Bot Əmrələri:</u>**
/reboot - Botunuzu yenidən başladın.
/update - Botu yeniləyin.
/speedtest - Server sürətlərini yoxlayın.
/maintenance [enable / disable]
/logger [enable / disable] - Bot axtarış edilmiş sorğuları qeyd edən qrupda qeyd edir.
/get_log [Xətlərin sayı] - Heroku və ya vps-dən botunuzun qeydini əldə edin. Hər ikisi üçün işləyir.
/autoend [enable|disable] - Heç kim qulaq asmırsa, 3 dəqiqədən sonra avtomatik yayımın bitməsini aktiv edin.

📈 **<u>İstatistik Əmrlər:</u>**
/activevoice - Botda aktiv səsli söhbətləri yoxlayın.
/activevideo - Botda aktiv video zəngləri yoxlayın.
/stats - Botların statistikasını yoxlayın.

⚠️ **<u>Qara Siyahi Sahib Funksiyası:</u>**
/blacklistchat [CHAT_ID] - Musiqi Botundan istifadə etməklə bağlı istənilən söhbəti qara siyahıya salın.
/whitelistchat [CHAT_ID] - Music Bot-dan istifadə edərək qara siyahıya salınmış söhbətləri ağ siyahıya daxil edin.
/blacklistedchat - Bütün qara siyahıya alınmış söhbətləri yoxlayın.

👤 **<u>Blok Olunmuş Funksiya:</u>**
/block [İstifadəçi adı və ya istifadəçiyə cavab] - İstifadəçinin bot əmrlərindən istifadəsinin qarşısını alır.
/unblock [İstifadəçi adı və ya istifadəçiyə cavab] - İstifadəçini Botun Bloklanmış Siyahısından çıxarın.
/blockedusers - Bloklanmış İstifadəçi Siyahılarını yoxlayın.

👤 **<u>Gban Funksiyası:</u>**
/gban [İstifadəçi adı və ya istifadəçiyə cavab] - İstifadəçini bot server çatından qadağan edin və onun botunuzdan istifadəsini dayandırın.
/ungban [İstifadəçi adı və ya istifadəçiyə cavab] - İstifadəçini Botun qadağan olunmuş Siyahısından çıxarın və ona botunuzdan istifadə etməyə icazə verin.
/gbannedusers - Gbanned İstifadəçi Siyahılarını yoxlayın.

🎥 **<u>Videokallar Funksiyası:</u>**
/set_video_limit [Söhbətlərin sayı] - Eyni zamanda Video Zənglər üçün icazə verilən maksimum Söhbət sayını təyin edin. Defolt olaraq 3 söhbət.
/videomode [download|m3u8] - Yükləmə rejimi aktivdirsə, Bot videoları M3u8 formasında oynamaq əvəzinə endirəcək. Varsayılan olaraq M3u8-ə. Hər hansı sorğu m3u8 rejimində oxunmayanda yükləmə rejimindən istifadə edə bilərsiniz.

⚡️ **<u>Şəxsi Bot Funksiyası:</u>**
/authorize [CHAT_ID] - Botunuzdan istifadə etmək üçün söhbətə icazə verin.
/unauthorize [CHAT_ID] - Söhbətin botunuzdan istifadəsinə icazə verməyin.
/authorized - Botunuzun bütün icazə verilən söhbətlərini yoxlayın.

🌐 **<u>Yayım Funksiyası:</u>**
/broadcast [Mesaj və ya Mesaja Cavab] - Botun Xidmət Çatlarına istənilən mesajı yayımlayın.

📥 **<u>Yayım Seçimləri:</u>**
**-pin:** Bu, mesajınızı sabitləyəcək.
**-pinloud:** Bu, mesajınızı yüksək səsli bildirişlə bağlayacaq.
**-user:** Bu, mesajınızı botunuzu işə salmış istifadəçilərə yayımlayacaq.
**-assistant:** Bu, mesajınızı botun köməkçi hesabından yayımlayacaq.
**-nobot:** Bu, botunuzu mesaj yayımlamamağa məcbur edəcək.

**Misal:** `/broadcast -user -assistant -pin Salam, Test Edirəm.`

"""
