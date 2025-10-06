from django.shortcuts import render
from .models import InformationStatistics
from .models import Jurusan
from .models import Eskul
from .models import Berita
# Create your views here.
def beranda(request):
    statistik = InformationStatistics.objects.first()
    kelebihan = [
        {
            "icon": "bi bi-person-workspace",
            "title": "Guru Profesional",
            "description": "Dibimbing oleh tenaga pendidik profesional dan berpengalaman."
        },
        {
            "icon": "bi bi-award",
            "title": "Prestasi Akademik & Non-Akademik",
            "description": "Siswa menorehkan prestasi di tingkat kota hingga nasional."
        },
        {
            "icon": "bi bi-people",
            "title": "Lingkungan Belajar Positif",
            "description": "Menjunjung tinggi disiplin, toleransi, dan kerja sama."
        },
        {
            "icon": "bi bi-laptop",
            "title": "Fasilitas Lengkap & Modern",
            "description": "Ruang kelas nyaman, lab, perpustakaan digital, serta area olahraga mendukung."
        },
    ]
    jurusan = Jurusan.objects.all()
    berita_terbaru = Berita.objects.order_by('published_date')[:3]

    return render(request, 'pages/beranda.html', {
        'statistik': statistik,
        'kelebihan': kelebihan,
        'jurusan': jurusan,
        'berita_terbaru': berita_terbaru
    })

def profil(request):
    misi = [
        "Menyelenggarakan pendidikan menengah kejuruan yang berkualitas untuk menghasilkan lulusan yang kompeten di bidangnya.",
        "Membentuk karakter siswa yang disiplin, jujur, bertanggung jawab, dan berakhlak mulia.",
        "Mengembangkan potensi siswa melalui kegiatan ekstrakurikuler yang beragam.",
        "Meningkatkan profesionalisme tenaga pendidik dan kependidikan melalui pelatihan dan pengembangan diri secara berkelanjutan.",
        "Menjalin kerja sama yang erat dengan dunia industri, dunia usaha, dan institusi pendidikan lainnya untuk mendukung proses pembelajaran dan penempatan kerja bagi lulusan.",
        "Menciptakan lingkungan sekolah yang kondusif, aman, dan nyaman bagi seluruh warga sekolah.",
    ]
    informasi_sekolah = {
        "profil": {
            "Nama Sekolah": "SMK Negeri 4 Kota Tasikmalaya",
            "NPSN": "20279663",
            "Nomor Statistik Sekolah": "401327810004",
        },
        "alamat": {
            "Jalan": "Jl Depok RT 02 RW 05",
            "Kelurahan": "Sukamenak",
            "Kecamatan": "Purbaratu",
            "Kota": "Tasikmalaya",
            "Provinsi": "Jawa Barat",
            "Telp/Faks": "(0265) 7528881",
            "Website": "www.smkn4-tsm.sch.id",
            "Email": "info@smkn4-tsm.sch.id",
        },
        "pendirian": {
            "Tahun Berdiri/Operasi": "2010",
            "Nomor SK Pendirian": "420/Sk.BPPT/2012",
            "Tanggal": "06 Februari 2012",
        },
        "lahan bangunan": {
            "Kepemilikan": "Pemerintah Daerah",
            "Status Tanah": "Sertifikat Hak Milik",
            "Luas Tanah": "13.222 m²",
            "Status Bangunan": "Milik Pemerintah",
            "Luas Bangunan": "2.400 m²",
            "Nomor Rekening": "010001100048306",
            "Nama Bank": "BRI Cabang Tasikmalaya",
        },
        "akreditasi": {
            "No Sertifikat": "728/BAN-SM/SK/2019",
            "Lembaga": "BAN-SM",
            "Berlaku Sampai": "17 September 2024",
            "Nilai": "A (UNGGUL) dengan Nilai 92",
            "Nilai Satuan Pendidikan": "92",
            "Prog. Keahlian T. Otomotif": "91",
            "Prog. Keahlian T. Komputer & Informatika": "92",
        },
        "kepala sekolah": {
            "Nama": "Kurniawan, S.Pd., M.Pd.",
            "NIP": "19780209 197202 1 002",
        }
    }
    
    return render(request, 'pages/profil.html', {'misi': misi, 'informasi_sekolah': informasi_sekolah})

def ekstrakulikuler(request):
    eskul = Eskul.objects.all()
    return render(request, 'pages/ekstrakullikuler.html', {'eskul': eskul})

def berita(request):
    berita = Berita.objects.all()
    return render(request, 'pages/berita.html', {'berita': berita})

def galeri(request):
    return render(request, 'pages/galeri.html')

def jurusan_detail(request, jurusan_id):
    jurusan = Jurusan.objects.get(id=jurusan_id)
    return render(request, 'pages/jurusan/jurusan_detail.html', {'jurusan': jurusan})

def berita_detail(request, berita_id):
    berita = Berita.objects.get(id=berita_id)
    return render(request, 'pages/berita/berita_detail.html', {'berita': berita})