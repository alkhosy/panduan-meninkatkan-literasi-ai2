# Panduan Literasi AI (Teknikal & Praktikal)

Proyek ini adalah panduan komprehensif untuk memahami dan menerapkan Kecerdasan Buatan (AI) secara praktis, ditulis dalam format LaTeX. Buku ini dirancang untuk mencapai 200+ halaman, mencakup teori, tutorial coding, dan lembar kerja (workbook) yang siap dicetak.

## Cara Mengompilasi

1.  Pastikan Anda memiliki distribusi LaTeX yang lengkap (misalnya, TeX Live).
2.  Jalankan perintah berikut dari direktori root proyek:

```bash
pdflatex ai_literacy_guide/main.tex
pdflatex ai_literacy_guide/main.tex
```

(Dua kali kompilasi diperlukan untuk memastikan *Table of Contents* dan referensi silang dibuat dengan benar).

## Struktur Proyek

*   `main.tex`: File utama LaTeX.
*   `chapters/`: Berisi file konten per bab.
*   `styles/`: File style custom (`.sty`).
*   `images/`: Gambar dan diagram.

## Fitur Utama

*   **Pembelajaran Berjenjang:** Dari konsep dasar hingga implementasi RAG (Retrieval Augmented Generation).
*   **Praktikal:** Disertai contoh kode Python dan prompt yang siap pakai.
*   **Workbook Terintegrasi:** Appendix B berisi lebih dari 75 templat "AI Project Canvas" dan "Prompt Log" yang dapat dicetak untuk mendokumentasikan eksperimen AI Anda, menjadikan buku ini alat kerja nyata.

## Catatan Penulis

Panduan ini menggunakan teknik "Self-Bootstrapping" di mana struktur buku dibangun terlebih dahulu, kemudian diisi dengan konten praktis yang dapat diskalakan. Workbook di bagian akhir sengaja diperbanyak untuk memenuhi kebutuhan dokumentasi proyek jangka panjang pembaca.
