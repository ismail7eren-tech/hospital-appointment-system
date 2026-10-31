import sqlite3
from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)
app.secret_key = "hastane_yönetim_sistemi_gizli_anahtar"
DB_NAME = "database.db"

UZMANLIKLAR = [
    "Kardiyoloji", "Dahiliye", "Nöroloji", "Ortopedi",
    "Göz Hastalıkları", "Kulak Burun Boğaz", "Dermatoloji",
    "Psikiyatri", "Çocuk Sağlığı", "Genel Cerrahi",
    "Üroloji", "Kadın Doğum"
]

def get_db():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row  # Verilere isim bazlı erişim sağlar
    return conn

def init_db():
    with get_db() as db:
        cursor = db.cursor()
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS hastalar (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                isim TEXT NOT NULL,
                soyisim TEXT NOT NULL,
                tc TEXT UNIQUE NOT NULL
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS doktorlar (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                isim TEXT NOT NULL,
                soyisim TEXT NOT NULL,
                uzmanlik TEXT NOT NULL
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS randevular (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                tarih TEXT NOT NULL,
                hasta_id INTEGER NOT NULL,
                doktor_id INTEGER NOT NULL,
                FOREIGN KEY (hasta_id) REFERENCES hastalar (id) ON DELETE CASCADE,
                FOREIGN KEY (doktor_id) REFERENCES doktorlar (id) ON DELETE CASCADE
            )
        """)
        
        # Başlangıç verileri (Seed Data)
        if cursor.execute("SELECT COUNT(*) FROM hastalar").fetchone()[0] == 0:
            cursor.execute("INSERT INTO hastalar (isim, soyisim, tc) VALUES (?, ?, ?)", ("Ahmet", "Yılmaz", "12345678901"))
            cursor.execute("INSERT INTO hastalar (isim, soyisim, tc) VALUES (?, ?, ?)", ("Mehmet", "Demir", "98765432109"))

        if cursor.execute("SELECT COUNT(*) FROM doktorlar").fetchone()[0] == 0:
            cursor.execute("INSERT INTO doktorlar (isim, soyisim, uzmanlik) VALUES (?, ?, ?)", ("Ali", "Kaya", "Kardiyoloji"))
            cursor.execute("INSERT INTO doktorlar (isim, soyisim, uzmanlik) VALUES (?, ?, ?)", ("Ayşe", "Çelik", "Dahiliye"))

        db.commit()

init_db()

@app.route("/")
def home():
    with get_db() as db:
        hastalar = db.execute("SELECT * FROM hastalar ORDER BY isim ASC").fetchall()
        doktorlar = db.execute("SELECT * FROM doktorlar ORDER BY isim ASC").fetchall()

        randevular = db.execute("""
            SELECT 
                r.id, 
                r.tarih, 
                h.isim AS hasta_isim, 
                h.soyisim AS hasta_soyisim, 
                d.isim AS doktor_isim, 
                d.soyisim AS doktor_soyisim,
                d.uzmanlik
            FROM randevular r
            JOIN hastalar h ON r.hasta_id = h.id
            JOIN doktorlar d ON r.doktor_id = d.id
            ORDER BY r.tarih DESC
        """).fetchall()

    return render_template(
        "index.html",
        hastalar=hastalar,
        doktorlar=doktorlar,
        randevular=randevular,
        uzmanliklar=UZMANLIKLAR
    )

@app.route("/hasta_ekle", methods=["POST"])
def hasta_ekle():
    isim = request.form.get("isim", "").strip()
    soyisim = request.form.get("soyisim", "").strip()
    tc = request.form.get("tc", "").strip()

    if not isim or not soyisim or not tc:
        flash("Hasta eklemek için tüm alanları doldurmalısınız.", "error")
        return redirect("/")

    try:
        with get_db() as db:
            db.execute(
                "INSERT INTO hastalar (isim, soyisim, tc) VALUES (?, ?, ?)",
                (isim, soyisim, tc)
            )
            db.commit()
            flash("Hasta kaydı başarıyla oluşturuldu.", "success")
    except sqlite3.IntegrityError:
        flash("Bu TC Kimlik numarasına sahip hasta zaten kayıtlı.", "error")

    return redirect("/")

@app.route("/doktor_ekle", methods=["POST"])
def doktor_ekle():
    isim = request.form.get("isim", "").strip()
    soyisim = request.form.get("soyisim", "").strip()
    uzmanlik = request.form.get("uzmanlik", "").strip()

    if not isim or not soyisim or not uzmanlik:
        flash("Doktor eklemek için tüm alanları doldurmalısınız.", "error")
        return redirect("/")

    with get_db() as db:
        db.execute(
            "INSERT INTO doktorlar (isim, soyisim, uzmanlik) VALUES (?, ?, ?)",
            (isim, soyisim, uzmanlik)
        )
        db.commit()
        flash("Doktor kaydı başarıyla eklendi.", "success")

    return redirect("/")

@app.route("/randevu_al", methods=["POST"])
def randevu_al():
    tarih = request.form.get("tarih")
    hasta_id = request.form.get("hasta")
    doktor_id = request.form.get("doktor")

    if not tarih or not hasta_id or not doktor_id:
        flash("Randevu oluşturmak için lütfen tarih, hasta ve doktor seçimini yapın.", "error")
        return redirect("/")

    with get_db() as db:
        db.execute(
            "INSERT INTO randevular (tarih, hasta_id, doktor_id) VALUES (?, ?, ?)",
            (tarih, hasta_id, doktor_id)
        )
        db.commit()
        flash("Randevu başarıyla oluşturuldu.", "success")

    return redirect("/")

@app.route("/randevu_sil/<int:id>", methods=["POST", "GET"])
def randevu_sil(id):
    with get_db() as db:
        db.execute("DELETE FROM randevular WHERE id = ?", (id,))
        db.commit()
        flash("Randevu iptal edildi.", "info")

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)