# 📊 Data Analysis Task – Conversion & Aggregated Join Study

## 👤 Author
**Zidan Kazali**  
Data Enthusiast | Electrical Engineering Graduate | Aspiring Data Analyst  

---

## 📌 Project Overview

Project ini merupakan studi analisis data berbasis Google Sheets untuk mengevaluasi:

- Same-day conversion rate (Search → Add to Cart)
- Join antar aggregated tables berdasarkan `user_id` dan `date`
- Perbandingan timestamp untuk validasi urutan event
- Pivot dan QUERY function optimization

Tujuan utama dari task ini adalah memahami:
- Bagaimana user behavior terjadi dalam satu hari yang sama
- Bagaimana mengolah event-based dataset menjadi insight bisnis
- Bagaimana melakukan data transformation hanya menggunakan Google Sheets

---

## 🎯 Problem Statement

1. Bagaimana cara menggabungkan dua tabel agregasi berdasarkan `user_id` dan `date`?
2. Bagaimana menghitung same-day conversion rate menggunakan QUERY dan pivot?
3. Bagaimana memastikan bahwa event `add_to_cart` terjadi setelah `search` berdasarkan timestamp?

---

## 🛠 Tools & Methods

- Google Sheets
- QUERY Function
- Pivot Table
- Timestamp Comparison Logic
- Aggregated Join (user_id + date)
- Conditional Filtering
- Conversion Rate Formula

---

## 📂 Dataset & Resources

📄 Spreadsheet (Data & Query):
> 🔗 [Paste Spreadsheet Link Here]

📊 Presentation Slides (Insight & Explanation):
> 🔗 [Paste Google Slides Link Here]

---

## 📈 Analysis Approach

### 1️⃣ Data Cleaning
- Formatting timestamp
- Extracting date from datetime
- Validating event types

### 2️⃣ Aggregation
- Count search per user per day
- Count add_to_cart per user per day

### 3️⃣ Join Logic
- Join by `user_id`
- Match by `date`
- Compare timestamps (search_time ≤ add_to_cart_time)

### 4️⃣ Conversion Calculation

\[
Conversion\ Rate = \frac{Users\ with\ Valid\ Add\ to\ Cart}{Users\ who\ Searched} \times 100\%
\]

---

## 📊 Key Insight (Example Section – Edit Later)

- X% dari user yang melakukan search melakukan add_to_cart di hari yang sama
- Terdapat pola bahwa conversion tertinggi terjadi pada jam tertentu
- Timestamp validation penting untuk menghindari false conversion

---

## 💡 Skills Demonstrated

- Data Aggregation
- Analytical Thinking
- Spreadsheet Query Optimization
- Business Metric Calculation
- Conversion Funnel Analysis
- Data Validation Logic

---

## 🚀 Why This Project Matters

Project ini menunjukkan kemampuan:

- Mengolah raw event data menjadi insight
- Membangun logic analitik tanpa SQL (Spreadsheet-based)
- Memahami behavior user dalam funnel conversion
- Menyusun analisis terstruktur dan sistematis

---

## 📬 Contact

Jika ingin berdiskusi lebih lanjut mengenai project ini atau kolaborasi data analysis:

LinkedIn: (Tambahkan Link)  
Email: (Tambahkan Email)

---

> This repository is part of my professional data analysis portfolio.
