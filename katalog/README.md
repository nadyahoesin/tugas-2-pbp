Link aplikasi Heroku: https://tugas-2-pbp-nadya.herokuapp.com/katalog/

- Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html
    * [bagan.jpg](bagan.jpg)

- Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
    * Virtual environment digunakan agar pengaturan dan package dari aplikasi Django terisolasi dari pengaturan dan package dari hal lain di komputer. Dengan menggunakan virtual environment, modul yang digunakan untuk aplikasi tidak akan terpengaruhi dari perubahan di luar environment. Contohnya, jika kita melakukan update pada modul-modul tersebut di luar environment, modul di dalam environment tidak akan terpengaruh sehingga kita dapat melanjutkan development tanpa error yang disebabkan oleh perubahan version. Membuat aplikasi web berbasis Django tanpa menggunakan virtual environment sebenarnya bisa saja tetapi memungkinkan terjadinya error jika hal yang sudah disebutkan dll terjadi (adanya update modul).

- Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.
    1. Membuat sebuah fungsi pada views.py yang dapat melakukan pengambilan data dari model dan dikembalikan ke dalam sebuah HTML.
       - Melakukan import terhadap CatalogItem dari models.py
       - Membuat function show_katalog yang akan:
         * Membuat dictionary context yang mempunyai key nama, npm, dan catalog_items dan value nama saya, npm saya, dan semua objek dari model CatalogItems
         * Menampilkan file html berdasarkan template katalog.html yang sudah diisi context (dengan function render)


    2. Membuat sebuah routing untuk memetakan fungsi yang telah kamu buat pada views.py.
       - Menambahkan path('', show_katalog, name='show_katalog') pada urls.py dalam folder aplikasi katalog, yang berarti function show_katalog akan dijalankan ketika <link aplikasi> diakses
       - Menambahkan path('katalog/', include('katalog.urls')) pada urls.py dalam folder proyek django, yang berarti aplikasi katalog akan dijalankan dan di-routing ke urls dalam aplikasi katalog jika <link proyek>/katalog diakses


    3. Memetakan data yang didapatkan ke dalam HTML dengan sintaks dari Django untuk pemetaan data template.
       - Menambahkan {{nama}} dan {{npm}} di tempat dalam katalog.html di mana value dari item tersebut ingin ditampilkan
       - Menggunakan {% for item in catalog_items %} untuk mengiterasi semua objek item dan menampilkan masing-masing atributnya (nama, harga, dll) dengan mengakses menggunakan titik ({{item.<atribut>}}) dan diakhiri dengan {% endfor %}

    4. Melakukan deployment ke Heroku terhadap aplikasi yang sudah kamu buat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
       - Melakukan push ke repositori Github
       - Menambahkan API key dan nama aplikasi Heroku ke dalam secrets repositori
       - Menjalankan workflow untuk deployment yang sebelumnya gagal