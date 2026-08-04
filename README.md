# 📊 Satış Analiz Dashboard

Python ve Streamlit kullanılarak geliştirilen bu proje, satış verilerinin etkileşimli olarak analiz edilmesini sağlayan bir dashboard uygulamasıdır. Kullanıcılar tarih (ay/çeyrek, çoklu seçim), il, müşteri ve ürün filtreleriyle verileri inceleyebilir; KPI kartları, performans grafikleri ve çeşitli analiz ekranları üzerinden satış performansını değerlendirebilir.

## 🚀 Özellikler

- **Dinamik filtreleme**: Ay ve Çeyrek bazında çoklu seçim (birden fazla ay/çeyrek aynı anda seçilebilir, seçilenlerin toplamı gösterilir), İl, Müşteri, Ürün
- **Karşılaştırmalı KPI kartları**: Toplam Ciro, Toplam Kilogram, Ortalama Fatura Tutarı, Fatura Sayısı, Aktif Müşteri, Satış Yapılan Şehir — tek dönem seçiliyken bir önceki döneme göre değişim yüzdesi ile birlikte
- **Aylık performans grafiği**: Ciro/Kilogram bazında çizgi grafiği; ortalama çizgisi, en yüksek/en düşük ay işaretleme; tek ay seçilince otomatik sütun grafiğine dönüşüm
- **Ürün Tipi ve PL dağılımı**: Yarım daire (gauge) grafiklerle görselleştirme
- **Ürün ciro dağılımı**: Donut grafik ve detaylı legend
- **Müşteri ve bölgesel performans analizi**: Yatay bar grafikler, tekil müşteri/il seçiliyken özel sıralama/karşılaştırma kartlarına dönüşüm
- **Dinamik sıralama (rank) kartları**: Seçili müşteri/il/ürünün ulusal/bölgesel sıralamadaki yerini gösteren özet kartlar
- **Daraltılabilir sidebar**: Filtre panelini açıp kapatma
- **Modüler proje yapısı**: Veri, servis ve arayüz katmanları ayrı klasörlerde

## 🗂️ Veri Kaynağı

Bu repoda dashboard, `generators/` altındaki script'lerle (`customer_generator.py`, `product_generator.py`, `invoice_generator.py`, `detail_generator.py`) üretilen **örnek/sahte veri** üzerinde çalışır. Tüm örnek veri seti, `main.py` çalıştırılarak tek seferde (sabit bir random seed ile, tekrarlanabilir şekilde) üretilir ve `data/` klasörüne CSV olarak yazılır.

> Projenin gerçek SAP REST API'lerinden (KPA/Customer/Product servisleri) canlı veri çeken bir entegrasyon sürümü de geliştirildi ve şirket içinde test edildi; ancak müşteri/şirket verisi içerdiği için o entegrasyon kodu ve gerçek veri **bu genel (public) repoya dahil edilmemiştir**. Bu repoda yalnızca örnek veriyle çalışan sürüm paylaşılmaktadır.

## 🛠️ Kullanılan Teknolojiler

- Python
- Streamlit
- Pandas
- NumPy
- Altair
- Requests (API entegrasyonu için)
- HTML & CSS (özel arayüz stilleri)

## 📷 Ekran Görüntüleri

### Ana Dashboard
<img width="1336" height="633" alt="Dashboard" src="https://github.com/user-attachments/assets/23b02084-da55-4e1d-afe2-5b3c7ea574ec" />

### Filtreleme Örneği
<img width="1340" height="626" alt="Filtered" src="https://github.com/user-attachments/assets/be0915cd-9da6-4ab2-ad89-1b72a4b86780" />

### Analiz Görünümü
<img width="1316" height="620" alt="Analysis" src="https://github.com/user-attachments/assets/50f9bfe1-49af-4466-bbba-e047f33f049c" />

## 📁 Proje Yapısı

```
sales_dashboard/
│
├── .streamlit/         # Streamlit yapılandırma dosyaları
├── components/         # Arayüz bileşenleri (sidebar, KPI, grafikler, genel görünüm)
├── config/              # Sabitler, dosya yolları, il kodu eşlemesi gibi yapılandırmalar
├── data/                 # Örnek/üretilmiş CSV veri dosyaları
├── generators/            # Sahte/örnek veri üretici script'ler
├── services/               # Veri yükleme, analiz ve dashboard veri hazırlama mantığı
├── utils/                   # Tablo/veri yardımcı fonksiyonları
├── .gitignore
├── app.py                    # Uygulamanın ana giriş noktası
├── main.py                    # Örnek veri setini (customers, products, invoices,
│                                 invoice_details) sabit bir seed ile sırayla üreten script
├── requirements.txt             # Bağımlılık listesi
├── styles.py                     # Özel CSS/tema tanımları
└── README.md
```

## ▶️ Çalıştırma

```bash
pip install -r requirements.txt

# Örnek veri setini üret (data/ klasörünü doldurur)
python main.py

# Dashboard'u başlat
streamlit run app.py
```