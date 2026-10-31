🇹🇷 Türkçe
🌟 Proje Hakkında
Hastane Yönetim Sistemi, sağlık kurumlarının günlük operasyonel süreçlerini (hasta kaydı, uzmanlık alanlarına göre doktor yönetimi ve randevu takibi) dijital ortamda düzenli, güvenli ve hızlı bir şekilde yürütmelerini sağlayan full-stack bir web uygulamasıdır.

Bu proje; ilişkisel veritabanı mimarisi, güvenli parametre yönetimi (SQLite3 parametreli sorguları) ve modern kullanıcı arayüzü (UI/UX) standartları gözetilerek baştan sona yeniden yapılandırılmıştır. Mimarinin geliştirilme ve refactor edilme süreçlerinde modern Yapay Zeka (AI) kodlama asistanlarından (Gemini AI, Cursor IDE) faydalanılmış; backend veri doğrulamaları, Safari/iOS uç durum (edge-case) uyumlulukları ve responsive tasarım prensipleri insan odaklı yazılım disiplinleriyle projeye entegre edilmiştir.

✨ Temel Özellikler
👥 Hasta Yönetimi: Ad, soyad ve benzersiz TC Kimlik No ile güvenli hasta kayıt alma ve veritabanı düzeyinde benzersizlik (uniqueness) doğrulaması.

👨‍⚕️ Doktor & Poliklinik Tanımlama: 12 farklı tıp uzmanlık alanı (Kardiyoloji, Nöroloji, Dahiliye vb.) altında doktor profilleri oluşturabilme.

📅 Dinamik Randevu Otomasyonu: Seçilen uzmanlık alanına göre ilgili doktorları istemci (frontend) tarafında anlık ve akıcı bir şekilde süzme (filtering).

📋 Randevu Takibi ve İptali: Aktif randevuları poliklinik ve tarih detaylarıyla listeleme, tek tıkla onaylı randevu iptal mekanizması.

🎨 Modern & Responsive Arayüz: Kurumsal sağlık temasına uygun (mavi/beyaz tonlar), mobil cihazlar ve tabletlerle tam uyumlu esnek düzen (CSS Grid & Flexbox).

⚡ Entegre Bildirim Sistemi (Flash Messages): İşlem başarı durumları veya hatalı/eksik veri girişlerinde kullanıcıya anlık renk kodlu geri bildirimler.

🛠️ Teknolojik Altyapı
Backend: Python 3.x, Flask Framework

Veritabanı & ORM: SQLite3 (sqlite3.Row nesne eşlemesi ve ilişkisel tablolar)

Frontend: HTML5 (Semantik etiketler), CSS3 (CSS Variables, Grid, Flexbox)

İstemci Mantığı: Vanilla JavaScript (DOM Manipülasyonu, Dinamik Option Filtreleme)

🇬🇧 English
🌟 About The Project
The Hospital Management System is a modern, full-stack web application designed for healthcare facilities to digitize patient records, manage specialized medical staff, and facilitate real-time appointment scheduling.

Engineered with a focus on relational database integrity and clean separation of concerns, the platform ensures secure parameter handling and smooth user interactions. Contemporary Artificial Intelligence (AI) coding assistants (Gemini AI, Cursor IDE) were utilized throughout the refactoring process to enhance backend validation rules, resolve browser-specific select bugs (Safari/iOS compatibility), and enforce responsive design guidelines.

✨ Key Features
👥 Patient Record Management: Secure patient onboarding capturing full names and unique National ID numbers with database-level uniqueness constraints.

👨‍⚕️ Doctor & Department Categorization: Create medical staff profiles mapped across 12 medical specialties (Cardiology, Neurology, Internal Medicine, etc.).

📅 Dynamic Appointment Filtering: Real-time client-side doctor filtering based on selected medical departments without full-page reloads.

📋 Real-time Scheduling & Cancellation: Comprehensive active appointment dashboard complete with one-click confirmation modal cancellations.

🎨 Modern Responsive Interface: Professional healthcare-themed design system utilizing CSS Grid and Flexbox for seamless cross-device compatibility.

⚡ Real-time Flash Notifications: Instant feedback banners providing status updates for successful submissions or input validation rules.

🛠️ Technology Stack
Backend: Python 3.x, Flask Framework

Database: SQLite3 (Relational Schema with sqlite3.Row mapping)

Frontend: HTML5 (Semantic Structure), CSS3 (Variables, Grid, Flexbox)

Client Scripting: Vanilla JavaScript (DOM Manipulation, Dynamic Filter Handling)

⚙️ Kurulum ve Çalıştırma | Getting Started
1. Depoyu Klonlayın (Clone the Repository)
Bash
git clone https://github.com/kullanici-adin/hastane-projesi.git
cd hastane-projesi
2. Sanal Ortamı Oluşturun ve Çalıştırın (Virtual Environment)
Bash
# Windows
python -m venv venv
.\venv\Scripts\activate.bat

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
3. Gerekli Paketleri Yükleyin (Install Dependencies)
Bash
pip install flask
4. Uygulamayı Başlatın (Run the Application)
Bash
python app.py
Tarayıcınızdan [http://127.0.0.1:5000](http://127.0.0.1:5000) adresine giderek uygulamayı kullanmaya başlayabilirsiniz.

"Sağlık hizmetlerinde verimlilik, doğru yönetim ve güvenli altyapı ile başlar."