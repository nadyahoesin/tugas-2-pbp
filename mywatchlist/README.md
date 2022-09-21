Link aplikasi Heroku: https://tugas-2-pbp-nadya.herokuapp.com/mywatchlist/<html/json/xml>

* Jelaskan perbedaan antara JSON, XML, dan HTML!
  > HTML adalah bahasa yang menampilkan webpage, sedangkan XML dan JSON adalah bahasa untuk menyimpan dan menukar data dengan dintaks yang berbeda. 

* Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
  > Untuk memberi respons yang sesuai terhadap requests dari client.

* Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

    1. Membuat suatu aplikasi baru bernama mywatchlist di proyek Django Tugas 2 pekan lalu
       > Menjalankan perintah `python manage.py startapp mywatchlist` dan menambahkan mywatchlist ke dalam list `INSTALLED-APPS` pada `settings.py` dalam folder project_django

    2. Menambahkan path mywatchlist sehingga pengguna dapat mengakses http://localhost:8000/mywatchlist
       > Menambahkan `path('mywatchlist/', include('mywatchlist.urls'))` ke dalam list `urlpatterns` pada `urls.py` dalam folder project_django

    3. Membuat sebuah model MyWatchList yang memiliki atribut sebagai berikut:
       - `watched` untuk mendeskripsikan film tersebut sudah ditonton atau belum
       - `title` untuk mendeskripsikan judul film
       - `rating` untuk mendeskripsikan rating film dalam rentang 1 sampai dengan 5
       - `release_date` untuk mendeskripsikan kapan film dirilis
       - `review` untuk mendeskripsikan review untuk film tersebut
       > Membuat class `MyWatchlist` yang merupakan subclass dari `models.Model` pada `models.py` dalam folder mywatchlist dengan variabel bernama atribut di atas dengan field yang sesuai

    4. Menambahkan minimal 10 data untuk objek MyWatchList yang sudah dibuat di atas
       > Membuat folder fixtures dalam folder mywatchlist dan membuat file `initial_mywatchlist_data.json` dalam folder fixtures yang memiliki objek-objek film dengan fields atribut di atas

    5. Mengimplementasikan sebuah fitur untuk menyajikan data yang telah dibuat sebelumnya dalam tiga format:
       - HTML
         > Membuat function `show_html` pada file `views.py` dalam folder mywatchlist yang akan:
         > - membuat dictionary context yang mempunyai key `nama`, `npm`, `watchlist`, dan `pesan` dan value nama saya, npm saya, semua objek dari model `MyWatchlist`, dan "Selamat, kamu sudah banyak menonton!" jika jumlah film yang sudah ditonton lebih banyak atau sama dengan jumlah film yang belum ditonton atau "Wah, kamu masih sedikit menonton!" jika jumlah film yang belum ditonton lebih banyak dari jumlah film yang sudah ditonton
         > - menampilkan file html berdasarkan template `mywatchlist.html` yang sudah diisi context (dengan function `render`)
       - XML
         > Membuat function `show_xml` yang akan menyimpan semua objek dari model `MyWatchlist` ke dalam variabel `watchlist_data` dan me-return `HttpResponse(serializers.serialize("xml", watchlist_data), content_type="application/xml")`
       - JSON
         > Membuat function `show_json` yang akan menyimpan semua objek dari model `MyWatchlist` ke dalam variabel `watchlist_data` dan me-return `HttpResponse(serializers.serialize("json", watchlist_data), content_type="application/json")`

    6. Membuat routing sehingga data di atas dapat diakses melalui URL:
       - http://localhost:8000/mywatchlist/html untuk mengakses mywatchlist dalam format HTML
       - http://localhost:8000/mywatchlist/xml untuk mengakses mywatchlist dalam format XML
       - http://localhost:8000/mywatchlist/json untuk mengakses mywatchlist dalam format JSON
       > Menambahkan `path('html/', show_html, name='show_html'), path('json/', show_json, name='show_json'), path('xml/', show_xml, name='show_xml'),` ke dalam list `urlpatterns` pada `urls.py` dalam folder mywatchlist 

    7. Melakukan deployment ke Heroku terhadap aplikasi yang sudah kamu buat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
       > Melakukan add, commit, dan push ke repositori Github (menambahkan secrets repositori sudah dilakukan dan workflows otomatis terulang)

Hasil akses URL menggunakan Postman:
* [html](html.png)
* [xml](xml.png)
* [json](json.png)
