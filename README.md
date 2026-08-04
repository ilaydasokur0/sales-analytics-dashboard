# 📊 Satış Analiz Dashboard

Python ve Streamlit kullanılarak geliştirilen, satış verilerinin etkileşimli olarak analiz edilmesini sağlayan bir dashboard uygulamasıdır.

Proje kapsamında örnek satış verileri oluşturulmuş, bu veriler analiz için işlenmiş ve kullanıcıların farklı filtreler üzerinden satış performansını inceleyebileceği dinamik bir raporlama ekranı geliştirilmiştir.

## 🚀 Özellikler

- Toplam Ciro, Toplam Kilogram, Ortalama Fatura Tutarı, Fatura Sayısı ve Aktif Müşteri Sayısı gibi KPI göstergeleri
- Tarih, ay, çeyrek, il, müşteri ve ürün bazında dinamik filtreleme
- Önceki dönem ile karşılaştırmalı performans analizi
- Aylık satış trendi grafiği
- Ürün, müşteri ve il bazlı performans analizleri
- Ürün tipi ve PL dağılım grafikleri
- Filtrelere göre anlık güncellenen analiz kartları ve detay tabloları

## 🛠️ Kullanılan Teknolojiler

- Python
- Streamlit
- Pandas
- NumPy
- Altair
- HTML & CSS

## 📂 Proje Yapısı

```
app.py
components/
services/
charts/
config/
assets/
requirements.txt
```

## ▶️ Kurulum

```bash
git clone https://github.com/kullaniciadi/sales-dashboard.git

cd sales-dashboard

pip install -r requirements.txt

streamlit run app.py
```

## 📷 Ekran Görüntüleri

### Ana Dashboard

![Dashboard](images/dashboard.png)

### Filtreleme

![Filtreleme](images/filters.png)

### Analiz

![Analiz](images/analysis.png)

## 📝 Not

Bu projede kullanılan satış verileri örnek amaçlı oluşturulmuş olup gerçek ticari verileri temsil etmemektedir.