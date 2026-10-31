function silOnay(id) {
    if (confirm("Bu randevuyu iptal etmek istediğinize emin misiniz?")) {
        window.location.href = `/randevu_sil/${id}`;
    }
}

document.addEventListener("DOMContentLoaded", () => {
    const uzmanlikSec = document.getElementById("uzmanlikSec");
    const doktorSelect = document.getElementById("doktorSelect");
    
    // Orijinal doktor seçeneklerini hafızada tut (Safari/iOS bug'ını önlemek için)
    const orijinalDoktorlar = Array.from(doktorSelect.options).filter(opt => opt.value !== "");

    uzmanlikSec.addEventListener("change", function () {
        const secilen = this.value;
        
        // Select kutusunu temizle
        doktorSelect.innerHTML = '<option value="">Doktor Seçin</option>';

        // Seçilen uzmanlığa uyan doktorları geri yükle
        orijinalDoktorlar.forEach(opt => {
            if (secilen === "" || opt.dataset.uzmanlik === secilen) {
                doktorSelect.appendChild(opt.cloneNode(true));
            }
        });
    });
});