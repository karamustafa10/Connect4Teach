#CONNECT4TEACH
# PROJE AFİŞİ
![afiş 1](https://github.com/dilarauns/connect4teach/assets/91975311/ad4f1690-024b-4512-98a6-a0e8ec1a3fa2) 
![afiş 2](https://github.com/dilarauns/connect4teach/assets/91975311/33f2a639-1b17-4db0-8d7a-ee7410e7fc83)



# GEREKSİNİM DÖKÜMANI

## **Proje Adı:** <br />
Connect4Teach

## **Proje Video Tanıtımı** <br />
[Video Tanıtım Linki](https://www.youtube.com/watch?v=D49BuBSJvW8)

## **Projenin amacı:** <br />
Bu projenin amacı, site üzerinden öğretmen ve öğrenci arasındaki eğitim etkileşimini arttırmayı hedeflemektir. Öğrencilerin soru sorma, özel ders ve öneri alma ihtiyaçlarını tek bir sitede toplamayı amaçlamaktadır. Site girişinin öğrenci ve öğretmen olarak ikiye ayrılıp öğretmen ve öğrencilerin site üzerinde yapacakları işlemler kendi içlerinde ayrılacaktır. Öğretmenler site içerisinde kendi bilgilerini girerek, öğrencilerin onlara ulaşmasını sağlayabilmektedir. Aynı zamanda öğrencilerin yüklediği soruları cevaplandırabilmektedir. Öğretmenler bu işlemlerin sonrasında öğrenciler tarafından değerlendirmeye tabi tutulurlar.
Öğrenciler kendi profillerine ilgili alandaki dersler için sorularını yükleyebilirler. Sorulara gelen cevapları değerlendirebilirler. Öğrenci anasayfasında öğretmenleri görüntüleyebilir ve öğretmenlere özel ders talebinde bulunabilir. Aynı zamanda diğer öğrencilerin sorduğu soruları görüntüleyebilir. Öğrenciler, öğretmenlerden aldıkları etkileşim sonucunda öğretmenleri değerlendirebilir.

## **Stakeholder:** <br />
 Projenin başarısı için yöneticiler, eğitmenler ve öğrenciler ana kişilerdir. Bu projenin başarılı şekilde devam etmesi için; yöneticilerin eğitmenleri kontrolü, eğitmenlerin öğrenciler ile iletişimi, öğrencilerin doğru şekilde soruları aktarabilmesi gibi olanaklar sağlanmalıdır.

## **Kullanıcı Gereksinimleri:** <br />
Connect4Teach sitesi eğitmenlerin ve öğrencilerin kullanabileceği bir eğitim platformudur. Öğrenciler günlük hayatta karşılaştığı ders sorularına hızlı bir çözüm bulamamaktadır. Bu yüzden çoğu zaman cevabına ulaşamadıkları sorularla sınavlara girmek zorunda kalırlar. Ayrıca özel ders fiyatlarının konum bazlı değişmesinden kaynaklı çok fazla maddi sıkıntı yaşanmaktadır. Bunların hepsine bir çözüm bulmak için soruların sisteme yüklenip eğitmenler tarafından çözülebilmesi ve özel ders adına fiyat/performans eğitmenlerin tercih edilebilmesi için Connect4Teach kullanılabilir. Ayrıca eğitmenler de kendilerine bir gelir katkısı olarak burada özel ders verebilecekleri öğrencileri bulabilirler ve kendilerinin eğitim kalitesini site üzerinden tanıtabilirler.

## **Güvenlik Gereksinimleri:** <br />
•	**Şifreleme (Encryption):** Kullanıcıların parolalarını depolarken güçlü şifreleme algoritmalarını kullanılacak. <br /> <br />
•	**Yetkilendirme ve Kimlik Doğrulama:** Django'nun yerleşik yetkilendirme ve kimlik doğrulama sistemi olan Django Authentication Framework'ü kullanılacak. Bu, kullanıcıların kayıt olmalarını, giriş yapmalarını ve oturum açmalarını yönetir. <br /> <br />
•	**CSRF Koruması (Cross-Site Request Forgery):** Django'nun varsayılan olarak sunulan CSRF koruma mekanizması, formlar aracılığıyla saldırıları önlemeye yardımcı olur. <br /> <br />


## **Teknoloji Gereksinimleri** <br />
•	**Django Framework (versiyon 4.2.7):** Web sitesi, Django web framework'ü kullanılarak geliştirilecektir. Projenin, Django'nun belirli bir versiyonu ile uyumlu olarak geliştirilmesi gerekmektedir. <br /> <br />
•	**Python (versiyon 3.12):** Django web framework'ü Python programlama dili ile uyumludur. Bu nedenle, proje için belirli bir Python versiyonu belirlenmelidir. <br /> <br />
•	**Veritabanı Yönetim Sistemi (DB Browser for SQLite):** Proje için kullanılacak olan veritabanı yönetim sistemi belirlenmelidir. Django, çeşitli veritabanı sistemleriyle uyumludur ve proje gereksinimlerine en uygun olanı seçilmelidir. <br /> <br />
•	**Frontend Teknolojileri (HTML, CSS, JavaScript, Bootstrap):** Web sitesinin kullanıcı arayüzü HTML, CSS ve JavaScript ile oluşturulacaktır. Bu teknolojiler, kullanıcıya interaktif ve etkileşimli bir deneyim sunmak için kullanılacaktır. <br /> <br />
•	**Geliştirme Ortamı Araçları (Git, IDE):** Proje geliştirme sürecinde kullanılacak olan araçlar belirlenmelidir. Bu araçlar, kod yönetimi, sürüm kontrolü, hata ayıklama ve geliştirme sürecini kolaylaştırmak için kullanılacaktır. <br /> <br />
•	**Güvenlik Araçları (Django Security Middleware):** Web sitesinin güvenliği için belirli güvenlik araçları ve kütüphaneler kullanılacaktır. Bu araçlar, kullanıcı verilerini korumak, kimlik doğrulama sağlamak ve saldırılara karşı koruma sağlamak için kullanılacaktır. <br /> <br />


## **Kabul Kriterleri:** <br />
•	**Tasarım Uyumluluğu:** Web sitesi, onaylanmış tasarım belgelerine uygun olarak geliştirilmelidir. Tüm sayfalar, tasarımın gerektirdiği şekilde düzenlenmelidir. <br /> <br />
•	**Kullanılabilirlik Testi:** Web sitesi, kullanıcı dostu ve kolay kullanılabilir olmalıdır. Kullanılabilirlik testlerinde, kullanıcıların web sitesini gezinme ve işlevleri kullanma deneyimleri değerlendirilecektir. <br /> <br />
•	**Fonksiyonel Testler:** Tüm web sitesi işlevleri, belirlenen gereksinimlere uygun olarak çalışmalıdır. Tüm formlar, düğmeler, bağlantılar ve diğer etkileşimli öğeler işlevsellik açısından test edilmelidir. <br /> <br />
•	**Performans Testleri:** Web sitesinin yanıt süresi ve yüklenme hızı belirli bir kabul edilebilir düzeyde olmalıdır. Performans testleri, web sitesinin yoğun trafik altında nasıl performans gösterdiğini değerlendirecektir. <br /> <br />
•	**Güvenlik Değerlendirmesi:** Web sitesinin güvenlik açıkları, saldırı noktaları ve zayıf noktaları belirlenmeli ve gerekli güvenlik önlemleri alınmalıdır. Güvenlik değerlendirmesi, web sitesinin siber saldırılara karşı ne kadar dirençli olduğunu değerlendirecektir. <br /> <br />
•	**Kullanıcı Testleri:** Web sitesi, gerçek kullanıcılar tarafından test edilmelidir. Kullanıcı testleri, web sitesinin kullanıcı deneyimini ve kullanılabilirliğini değerlendirecektir. <br /> <br />
•	**Kullanıcı Geri Bildirimleri:** Web sitesi, kullanıcıların geri bildirimlerine açık olmalıdır. Kullanıcı geri bildirimleri, web sitesinin kullanıcıların ihtiyaçlarına nasıl yanıt verdiğini değerlendirecektir. <br /> <br />
•	**İçerik Kalitesi:** Web sitesinin içeriği, doğru, güncel ve kaliteli olmalıdır. İçerik kalitesi testleri, web sitesinin içeriğinin doğruluğunu ve uygunluğunu değerlendirecektir. <br /> <br />


## **Fonksiyonel Gereksinimler:** <br />
Connect4Teach sitesi fonksiyonel gereksinim açısından eğitmen ve öğrenci hesapları, hesap bilgileri değiştirme, soru yükleme, soru cevaplama, soru değerlendirme, eğitmen değerlendirme ve özel ders planlama fonksiyonlarını yerine getirmelidir. <br />

## Projemizin Proje Teslimatı ve Zaman Çizelgesi: <br />
•	**Proje Amaçları ve Kapsamı Belirleme:** <br />
Zaman Çerçevesi: 1 hafta <br />
Teslimat: Proje kapsamı belirlendikten sonra <br /> <br />
•	**Gereksinimlerin Analizi ve Planlama:** <br />
Zaman Çerçevesi: 1 hafta <br />
Teslimat: Gereksinim analizi raporu ve proje planı <br /> <br />
•	**Tasarım ve Prototip Geliştirme:** <br />
Zaman Çerçevesi: 4 hafta <br />
Teslimat: Prototip ve tasarım belgeleri <br /> <br />
•	**Geliştirme ve Test Aşamaları:** <br />
Zaman Çerçevesi: 3 hafta <br />
Teslimat: Test raporları ve kullanıcı geri bildirimleri <br /> <br />
•	**Düzeltmeler ve Son Dokümantasyon:** <br />
Zaman Çerçevesi: 1 hafta <br />
Teslimat: Son teslimat ve proje dokümantasyonu <br /> <br />

**Not:** Yukarıdaki zaman çizelgesi, Kanban yöntemi kullanılarak takip edilecektir. Görevlerin ilerlemesini ve tamamlanmasını izlemek için Kanban panosu tüm ekip üyeleri tarafından düzenli olarak güncellenecektir. <br />


## **TAKIM ÜYELERİ ve YETKİNLİKLERİ:**
> Mustafa Semih Bulut – 20360859022 - Front-end Developer <br />
Eğitmen anasayfası tasarlamak ve kodlamak.<br />
Dokümantasyon hazırlama ve düzenlemek<br /><br /><br />
> Semih Karamustafa – 20360859054 - Front-end Developer <br /> 
Projenin hangi ortamda geliştirileceğini önermek.<br />
Marka logosu hazırlamak.<br />
Öğrenci ana sayfası kodlarını yazmak.<br /><br /><br />
> Sude Telli – 21360859017 - Front-end Developer <br />
Tasarım aşamasında giriş ekranını oluşturmak.<br />
Öğretmen profilinin kodlarını yazmak.<br /><br /><br />
> Mehmet Taha Mehel - 21360859068 - Front-end Developer <br />
Giriş ekranının tasarlanmak ve kodlanmak.<br />
Kayıt ol ve giriş yap sayfalarının tasarlanmak ve kodlanmak.<br />
Domaini sunucuya aktarmak ve ayarlanmak.<br /><br /><br />
> Dilara Ünsal - 20360859070 - Front-end Developer <br />
Yazılımda kullanılacak dil için kaynak sunmak.<br />
Tasarım aşamasında öğrenciye ait profil sayfasının oluşturmak.<br />
Öğrencinin profil sayfasının kodlarını yazmak.<br /> <br /> <br />



# PROJE KULLANIM KILAVUZU.
Projenin güncel kullanım kılavuzuna buradan erişebilirsiniz. <br />

[Connect4Teach - Proje Kullanım Kılavuzu v2.0.pdf](https://github.com/dilarauns/connect4teach/files/15444226/Takim.11-.Proje.Kullanim.Kilavuzu.v2.0.pdf)
